from fastapi import APIRouter, UploadFile, File, HTTPException
import cv2
import numpy as np
import mediapipe as mp
from datetime import datetime

router = APIRouter()
mp_face_mesh = mp.solutions.face_mesh

@router.post("/analyze-image")
async def analyze_image(file: UploadFile = File(...)):
    """
    Analyze a facial image and return predictions for:
    - Wrinkle severity
    - Dark spot intensity 
    - Puffy eye probability
    - Acne and Blackheads
    - Skin age estimation
    """
    # Validate file type
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File provided is not an image.")
    
    try:
        # 1. Read the image into OpenCV
        contents = await file.read()
        nparr = np.frombuffer(contents, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        if img is None:
            raise HTTPException(status_code=400, detail="Could not process the image.")
            
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Default baseline values if no face is clearly detected
        wrinkle, dark_spot, puffy_eye, acne, blackheads = 2.0, 15.0, 10.0, 5.0, 8.0
        confidence = 0.50
        
        # 2. Find the face using Google MediaPipe
        with mp_face_mesh.FaceMesh(static_image_mode=True, max_num_faces=1, min_detection_confidence=0.5) as face_mesh:
            results = face_mesh.process(img_rgb)
            
            if results.multi_face_landmarks:
                confidence = 0.95
                landmarks = results.multi_face_landmarks[0].landmark
                h, w, _ = img.shape
                
                # Extract Face Bounding Box
                x_coords = [int(l.x * w) for l in landmarks]
                y_coords = [int(l.y * h) for l in landmarks]
                x_min, x_max = max(0, min(x_coords)), min(w, max(x_coords))
                y_min, y_max = max(0, min(y_coords)), min(h, max(y_coords))
                
                if x_max > x_min and y_max > y_min:
                    face_roi = gray[y_min:y_max, x_min:x_max]
                    face_roi_color = img[y_min:y_max, x_min:x_max]
                    
                    # A) Wrinkles: Calculate Edge Density using Canny
                    edges = cv2.Canny(face_roi, 30, 100)
                    wrinkle = float(round(min(5.0, max(0.5, np.mean(edges > 0) * 40)), 2))
                    
                    # B) Dark Spots & Acne: Color variance in LAB space
                    lab = cv2.cvtColor(face_roi_color, cv2.COLOR_BGR2LAB)
                    l_channel, a_channel, b_channel = cv2.split(lab)
                    
                    color_variance = np.std(a_channel) + np.std(b_channel)
                    dark_spot = float(round(min(35.0, max(5.0, color_variance)), 2))
                    acne = float(round(min(20.0, max(1.0, np.mean(a_channel) - 125)), 2))
                    
                    # C) Puffy Eyes / Fatigue: Face luminance vs shadows
                    puffy_eye = float(round(min(30.0, max(5.0, (1 - (np.mean(l_channel)/255)) * 40)), 2))
                    
                    # D) Blackheads: High frequency noise / Laplacian variance
                    laplacian = cv2.Laplacian(face_roi, cv2.CV_64F)
                    blackheads = float(round(min(20.0, max(2.0, np.var(laplacian) / 100)), 2))

        # Calculate custom skin age and health score
        skin_age = float(round(20 + (wrinkle * 4) + (dark_spot * 0.3), 1))
        health_score = float(max(0, min(100, round(100 - (0.4 * (wrinkle/5*100) + 0.3 * dark_spot + 0.3 * puffy_eye), 2))))
        
        category = "Excellent" if health_score >= 80 else "Moderate" if health_score >= 60 else "Needs Care"

        return {
            "wrinkle_score": wrinkle,
            "dark_spot_score": dark_spot,
            "puffy_eye_score": puffy_eye,
            "acne_score": acne,
            "blackheads_score": blackheads,
            "predicted_skin_age": skin_age,
            "health_score": health_score,
            "confidence": confidence,
            "health_category": category,
            "filename": file.filename,
            "timestamp": datetime.utcnow().isoformat()
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
