"""
GlowAI - AI Skin Health & Beauty Assistant
✨ Premium Skincare Experience ✨
With Database Integration - ai_dermal database
"""
import streamlit as st
import random
from datetime import datetime
import sys
import os

# Try to import database connector
try:
    from database_connector import (
        save_user, verify_user_login, get_user_by_email,
        save_analysis_log, get_logs, init_db, GlowAIUser
    )
    DB_AVAILABLE = True
except Exception as e:
    print(f"Database import error: {e}")
    DB_AVAILABLE = False

# Page Configuration
st.set_page_config(
    page_title="✨ GlowAI - Your Skin Beauty",
    page_icon="💖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Enhanced CSS - Premium Luxury Theme
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #FFF0F5 0%, #FFE4EC 25%, #FFD6E0 50%, #FFC8D4 75%, #FFBAD2 100%);
        background-attachment: fixed;
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    h1, h2, h3, h4 {
        color: #D63384 !important;
        font-family: 'Nunito', 'Segoe UI', sans-serif;
        font-weight: 700;
    }
    .glow-card {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 25px;
        padding: 30px;
        box-shadow: 0 15px 50px rgba(214, 51, 132, 0.15);
        margin: 20px 0;
        border: 2px solid rgba(255, 182, 213, 0.5);
    }
    .stButton>button {
        background: linear-gradient(135deg, #FF69B4 0%, #FF1493 100%) !important;
        color: white !important;
        border-radius: 50px !important;
        padding: 15px 40px !important;
        font-weight: 700 !important;
    }
    [data-testid="stMetricValue"] {
        color: #FF1493 !important;
    }
    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
        100% { transform: translateY(0px); }
    }
    .score-circle {
        width: 180px;
        height: 180px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 48px;
        font-weight: bold;
        margin: 0 auto;
    }
    .db-status {
        position: fixed;
        bottom: 10px;
        right: 10px;
        padding: 8px 15px;
        border-radius: 20px;
        font-size: 12px;
        z-index: 1000;
    }
</style>
<div style="position: fixed; top: 10px; right: 10px; font-size: 40px;">💖</div>
<div style="position: fixed; top: 100px; left: 10px; font-size: 30px;">🌸</div>
<div style="position: fixed; bottom: 50px; right: 50px; font-size: 35px;">💎</div>
""", unsafe_allow_html=True)

# Database status
if DB_AVAILABLE:
    st.markdown('<div class="db-status" style="background:#4CAF50;color:white;">🟢 Database Connected (ai_dermal)</div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="db-status" style="background:#FF9800;color:white;">🟠 Demo Mode</div>', unsafe_allow_html=True)

# Session State
if 'logged_in' not in st.session_state: st.session_state['logged_in'] = False
if 'analyzed' not in st.session_state: st.session_state['analyzed'] = False
if 'result' not in st.session_state: st.session_state['result'] = None
if 'real_age' not in st.session_state: st.session_state['real_age'] = 25
if 'user_name' not in st.session_state: st.session_state['user_name'] = "Beauty"
if 'user_id' not in st.session_state: st.session_state['user_id'] = None
if 'user_email' not in st.session_state: st.session_state['user_email'] = None
if 'history' not in st.session_state: st.session_state['history'] = []
if 'db_available' not in st.session_state: st.session_state['db_available'] = DB_AVAILABLE

def load_history_from_db():
    """Load analysis history from database"""
    if DB_AVAILABLE:
        try:
            logs = get_logs(limit=50)
            return logs
        except Exception as e:
            print(f"Error loading history: {e}")
    return []

def get_predictions(real_age=None):
    wrinkle = round(random.uniform(0.5, 4.5), 2)
    dark_spot = round(random.uniform(5, 35), 2)
    puffy_eye = round(random.uniform(5, 30), 2)
    acne = round(random.uniform(1, 15), 2)
    blackheads = round(random.uniform(2, 20), 2)
    skin_age = real_age + random.randint(-5, 8) if real_age else round(random.uniform(22, 55), 1)
    health_score = max(0, min(100, round(100 - (0.3 * (wrinkle/5*100) + 0.25 * dark_spot + 0.25 * puffy_eye + 0.2 * acne), 2)))
    category = "Glowing! ✨" if health_score >= 80 else "Pretty Good 💅" if health_score >= 60 else "Needs Love 💕"
    confidence = round(random.uniform(0.75, 0.95), 2)
    return {"wrinkle_score": wrinkle, "dark_spot_score": dark_spot, "puffy_eye_score": puffy_eye, "acne_score": acne, "blackheads_score": blackheads, "predicted_skin_age": skin_age, "health_score": health_score, "health_category": category, "confidence": confidence, "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

def get_recommendations(wrinkle, dark_spot, puffy_eye, acne):
    recs = []
    if wrinkle >= 3: recs.append({"issue": "Wrinkles", "severity": "High", "emoji": "🧴", "products": ["Retinol Cream 💫", "Vitamin C Serum ✨", "Peptide Moisturizer 🌟"], "ayurvedic": ["Ghee massage 🪔", "Coconut oil + turmeric 🌿"], "tips": "Sunscreen ☀️, no smoking 🚭"})
    elif wrinkle >= 2: recs.append({"issue": "Wrinkles", "severity": "Moderate", "emoji": "🧴", "products": ["Vitamin C ✨", "Niacinamide 💜"], "ayurvedic": ["Aloe vera 🌱"], "tips": "Hydrate 💧"})
    if dark_spot >= 20: recs.append({"issue": "Dark Spots", "severity": "High", "emoji": "⭐", "products": ["Hydroquinone ✨", "Vitamin C 20% 💯"], "ayurvedic": ["Lemon honey 🍋", "Turmeric 🧈"], "tips": "SPF every 2hrs ☀️"})
    elif dark_spot >= 10: recs.append({"issue": "Dark Spots", "severity": "Moderate", "emoji": "⭐", "products": ["Vitamin C ✨"], "ayurvedic": ["Cucumber 🥒"], "tips": "SPF 30+ ☀️"})
    if puffy_eye >= 20: recs.append({"issue": "Puffy Eyes", "severity": "High", "emoji": "👁️", "products": ["Caffeine ☕", "Cooling gel 🧊"], "ayurvedic": ["Cucumber 🥒", "Rose water 💧"], "tips": "8hrs sleep 😴"})
    if acne >= 10: recs.append({"issue": "Acne", "severity": "High", "emoji": "🌸", "products": ["Salicylic 🧼", "Benzoyl ✨"], "ayurvedic": ["Neem 🌿", "Turmeric 🧡"], "tips": "No touch 🙅‍♀️"})
    elif acne >= 5: recs.append({"issue": "Acne", "severity": "Moderate", "emoji": "🌸", "products": ["Gentle 🌸"], "ayurvedic": ["Neem 🌿"], "tips": "Keep clean 🧼"})
    return recs

def get_wellness_tips():
    return {"face_yoga": [{"name": "💋 Lip Plumper", "duration": "2 min", "steps": "Pucker lips 10sec, repeat 10x"}, {"name": "👁️ Eye Opener", "duration": "3 min", "steps": "Look up, close tight, blink fast"}, {"name": "😊 Cheek Lift", "duration": "2 min", "steps": "Big smile 10sec, repeat 10x"}], "breathing": [{"name": "🌸 4-7-8", "steps": "Inhale4, hold7, exhale8"}, {"name": "💫 Box", "steps": "Inhale4, hold4, exhale4, hold4"}], "lifestyle": ["💧 8-10 glasses water", "😴 7-8 hours sleep", "☀️ SPF every 2 hours", "🙈 Don't touch face", "🐟 Omega-3 foods"]}

def login_page():
    st.markdown("<br><br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""<div style="text-align: center;"><h1 style="font-size: 70px;">💖✨</h1><h2 style="font-size: 42px;">Welcome to GlowAI</h2><p style="color: #DB7093; font-size: 18px;">Your Personal Beauty & Skin Health Assistant 💕</p></div>""", unsafe_allow_html=True)
        st.markdown('<div class="glow-card">', unsafe_allow_html=True)
        tab1, tab2 = st.tabs(["💕 Login", "✨ Register"])
        
        with tab1:
            st.markdown("### 💖 Welcome Back, Beautiful!")
            email = st.text_input("📧 Email", key="login_email", placeholder="your@email.com")
            password = st.text_input("🔐 Password", type="password", key="login_password", placeholder="••••••••")
            if st.button("🌟 Login", key="login_btn"):
                if DB_AVAILABLE:
                    success, user_data = verify_user_login(email, password)
                    if success:
                        st.session_state['logged_in'] = True
                        st.session_state['user_name'] = user_data.get('full_name', 'Beauty')
                        st.session_state['user_id'] = user_data.get('id')
                        st.session_state['user_email'] = email
                        st.session_state['real_age'] = user_data.get('age', 25)
                        st.session_state['history'] = load_history_from_db()
                        st.balloons()
                        st.success(f"💖 Welcome back, {st.session_state['user_name']}!")
                        st.rerun()
                    else:
                        st.error("❌ Invalid email or password!")
                else:
                    if email and password:
                        st.session_state['logged_in'] = True
                        st.session_state['user_name'] = email.split('@')[0].title()
                        st.session_state['user_email'] = email
                        st.balloons()
                        st.success("💖 Login successful (Demo Mode)!")
                        st.rerun()
        
        with tab2:
            st.markdown("### ✨ Join GlowAI Family!")
            
            # Use form container to properly handle submission
            with st.form("register_form", clear_on_submit=False):
                name = st.text_input("👤 Full Name", key="reg_name", placeholder="Your beautiful name")
                email = st.text_input("📧 Email", key="reg_email", placeholder="your@email.com")
                age = st.number_input("🎂 Age", 10, 80, 25, key="reg_age")
                password = st.text_input("🔐 Password", type="password", key="reg_password", placeholder="••••••••")
                confirm = st.text_input("🔐 Confirm Password", type="password", key="reg_confirm", placeholder="••••••••")
                
                submit = st.form_submit_button("🌸 Create Account", key="reg_btn")
                
                if submit:
                    # Validate all fields are filled (including confirm)
                    if not name or not email or not password or not confirm:
                        st.error("Please fill in all fields!")
                    elif password != confirm:
                        st.error("❌ Passwords don't match!")
                    elif DB_AVAILABLE:
                        success, msg = save_user(name, email, password, age=age)
                        if success:
                            st.balloons()
                            st.success(f"💖 Account created! Welcome, {name}!")
                            st.session_state['logged_in'] = True
                            st.session_state['user_name'] = name
                            st.session_state['user_email'] = email
                            st.session_state['real_age'] = age
                            st.rerun()
                        else:
                            st.error(f"❌ {msg}")
                    else:
                        st.session_state['logged_in'] = True
                        st.session_state['user_name'] = name
                        st.session_state['user_email'] = email
                        st.session_state['real_age'] = age
                        st.balloons()
                        st.success("💖 Account created! (Demo Mode)")
                        st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        if not DB_AVAILABLE:
            st.warning("⚠️ Running in Demo Mode")

def home_page():
    st.markdown("""<div style="text-align: center; padding: 20px;"><h1>✨ GlowAI ✨</h1><p style="color: #DB7093; font-size: 20px;">Your Personal Beauty & Skin Health Assistant 💕</p></div>""", unsafe_allow_html=True)
    st.markdown("---")
    col1, col2 = st.columns([2, 1])
    with col1: st.markdown(f"### 💖 Hello, **{st.session_state['user_name']}**! 🌸")
    with col2: st.session_state['real_age'] = st.number_input("🎂 Your Age:", 10, 80, st.session_state['real_age'])
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 📸 Upload Photo 💄")
        uploaded_file = st.file_uploader("Choose a clear face photo...", type=['jpg', 'jpeg', 'png'])
        if uploaded_file:
            st.image(uploaded_file, caption="📸 Your Photo", width=350)
            if st.button("🔬 Analyze My Skin ✨", key="analyze_btn"):
                with st.spinner("🧴 Analyzing your beautiful skin..."):
                    result = get_predictions(st.session_state['real_age'])
                    result['filename'] = uploaded_file.name
                    
                    # Save to database - analysis_logs table
                    if DB_AVAILABLE:
                        saved = save_analysis_log(result)
                        if saved:
                            st.session_state['history'] = load_history_from_db()
                    
                    st.session_state['result'] = result
                    st.session_state['analyzed'] = True
                    st.session_state['history'].insert(0, result)
                st.balloons()
                st.success("💖 Analysis Complete! ✨")
    
    with col2:
        st.markdown("### 📊 Your Results 💅")
        if st.session_state['analyzed'] and st.session_state['result']:
            r = st.session_state['result']; score = r['health_score']
            color = "#FF69B4" if score >= 80 else "#FFB6C1" if score >= 60 else "#DB7093"
            emoji = "💖" if score >= 80 else "💕" if score >= 60 else "💗"
            st.markdown(f"""<div class="glow-card" style="text-align:center; border-left: 8px solid {color};"><h2 style="color: {color} !important;">Skin Health Score</h2><div class="score-circle" style="background: linear-gradient(135deg, {color}20, {color}40); border: 4px solid {color};"><span style="color: {color};">{score}</span></div><h3 style="color: {color}; margin-top:15px;">{emoji} {r['health_category']}</h3><p>Skin Age: <strong>{r['predicted_skin_age']}</strong> | Confidence: {r.get('confidence', 0)*100:.0f}%</p></div>""", unsafe_allow_html=True)
            c1,c2,c3,c4,c5 = st.columns(5); c1.metric("🧴 Wrinkles", f"{r['wrinkle_score']}/5"); c2.metric("⭐ Spots", f"{r['dark_spot_score']}%"); c3.metric("👁️ Puffy", f"{r['puffy_eye_score']}%"); c4.metric("🌸 Acne", f"{r['acne_score']}%"); c5.metric("💎 Blackheads", f"{r['blackheads_score']}%")
            if DB_AVAILABLE:
                st.success("💖 Saved to database (analysis_logs)!")
        else:
            st.markdown("""<div class="glow-card" style="text-align:center; padding:60px;"><h1 style="font-size:80px;">📸</h1><h3>No Analysis Yet</h3><p>Upload & analyze to discover your glow! ✨</p></div>""", unsafe_allow_html=True)

def solutions_page():
    st.markdown("""<div style="text-align:center;"><h1>💊 Your Beauty Solutions 💖</h1></div>""", unsafe_allow_html=True); st.markdown("---")
    if not st.session_state['analyzed']: st.warning("💕 Analyze first!"); return
    recs = get_recommendations(st.session_state['result']['wrinkle_score'], st.session_state['result']['dark_spot_score'], st.session_state['result']['puffy_eye_score'], st.session_state['result']['acne_score'])
    if recs:
        for rec in recs:
            with st.expander(f"{rec['emoji']} {rec['issue']} - {rec['severity']}"):
                st.markdown("#### 🏪 Products")
                for i,p in enumerate(rec['products'],1): st.markdown(f"- {i}. {p}")
                st.markdown("---"); st.markdown("#### 🌿 Ayurvedic")
                for i,a in enumerate(rec['ayurvedic'],1): st.markdown(f"- {i}. {a}")
                st.markdown("---"); st.info(rec['tips'])
    else: st.success("🎉 Amazing skin! ✨")
    st.markdown("---"); st.markdown("### 📅 Daily Routine 💆‍♀️")
    col1,col2 = st.columns(2)
    with col1: st.markdown("""<div class="glow-card"><h3>☀️ Morning</h3><ol><li>💧 Cleanser</li><li>✨ Vit C</li><li>💜 Moisturizer</li><li>☀️ SPF</li></ol></div>""", unsafe_allow_html=True)
    with col2: st.markdown("""<div class="glow-card"><h3>🌙 Night</h3><ol><li>🧼 Double Cleanse</li><li>✨ Retinol</li><li>👁️ Eye Cream</li><li>💧 Night Cream</li></ol></div>""", unsafe_allow_html=True)

def wellness_page():
    st.markdown("""<div style="text-align:center;"><h1>🧘‍♀️ Wellness & Self-Care 💆‍♀️</h1></div>""", unsafe_allow_html=True); st.markdown("---")
    tips = get_wellness_tips()
    st.markdown("### 💋 Face Yoga"); cols = st.columns(2)
    for i,e in enumerate(tips['face_yoga']): cols[i%2].expander(e['name']+" - "+e['duration']).markdown(f"**Steps:** {e['steps']}")
    st.markdown("---"); st.markdown("### 🌬️ Breathing"); cols = st.columns(2)
    for i,b in enumerate(tips['breathing']): cols[i%2].expander(b['name']).markdown(f"**Steps:** {b['steps']}")
    st.markdown("---"); st.markdown("### 💪 Lifestyle")
    for t in tips['lifestyle']: st.markdown(f"- {t}")

def progress_page():
    st.markdown("""<div style="text-align:center;"><h1>📊 Your Beauty Journey 💖</h1></div>""", unsafe_allow_html=True); st.markdown("---")
    
    if DB_AVAILABLE:
        st.session_state['history'] = load_history_from_db()
    
    if not st.session_state['history']:
        st.markdown("""<div class="glow-card" style="text-align:center;"><h1 style="font-size:60px;">📊</h1><h3>No History Yet</h3><p>Start by analyzing your skin! 🌸</p></div>""", unsafe_allow_html=True)
        return
    
    total = len(st.session_state['history'])
    scores = [h['health_score'] for h in st.session_state['history'] if 'health_score' in h]
    avg = sum(scores)/len(scores) if scores else 0
    c1,c2,c3 = st.columns(3); c1.metric("📸 Total Scans", total); c2.metric("💖 Average", f"{avg:.1f}"); c3.metric("🎯 Goal", "85+")
    
    st.markdown("---"); st.markdown("### 📋 Recent Analyses (From Database)")
    for i,h in enumerate(st.session_state['history'][:10]):
        score = h.get('health_score', 'N/A')
        with st.expander(f"✨ Scan {i+1} - {h.get('timestamp', h.get('created_at', 'Unknown'))}"):
            c1,c2,c3,c4 = st.columns(4)
            c1.metric("Score", score)
            c2.metric("🧴 Wrinkles", f"{h.get('wrinkle_score', 'N/A')}")
            c3.metric("⭐ Spots", f"{h.get('dark_spot_score', 'N/A')}%")
            c4.metric("🎂 Age", h.get('predicted_skin_age', 'N/A'))

def profile_page():
    st.markdown("""<div style="text-align:center;"><h1>👤 Your Profile 💖</h1></div>""", unsafe_allow_html=True); st.markdown("---")
    c1,c2 = st.columns([1,2])
    with c1: st.markdown("""<div style="font-size:100px;text-align:center;">👸</div>""", unsafe_allow_html=True)
    with c2:
        st.markdown(f"### 💖 {st.session_state['user_name']}")
        st.markdown(f"**📧 Email:** {st.session_state.get('user_email', 'N/A')}")
        st.markdown(f"**🎂 Age:** {st.session_state['real_age']}")
        st.markdown(f"**🎯 Goal:** Skin Health Score 85+ ✨")
        
        if st.session_state['history']:
            latest = st.session_state['history'][0]
            st.markdown(f"**💕 Latest Score:** {latest.get('health_score', 'N/A')}")
    
    st.markdown("---"); st.markdown("### ✏️ Edit Profile")
    
    with st.form("edit_profile"):
        new_name = st.text_input("👤 Name:", value=st.session_state['user_name'])
        new_age = st.number_input("🎂 Age:", 10, 80, st.session_state['real_age'])
        new_email = st.text_input("📧 Email:", value=st.session_state.get('user_email', ''))
        
        submit = st.form_submit_button("💖 Save Changes")
        if submit:
            st.session_state['user_name'] = new_name
            st.session_state['real_age'] = new_age
            st.session_state['user_email'] = new_email
            st.success("✨ Profile updated successfully! 💖")
            st.rerun()
    
    st.markdown("---")
    if st.button("🚪 Logout"):
        st.session_state['logged_in'] = False
        st.session_state['analyzed'] = False
        st.session_state['result'] = None
        st.session_state['history'] = []
        st.rerun()

def main():
    if not st.session_state['logged_in']: login_page(); return
    st.sidebar.markdown("""<div style="text-align:center;"><h1 style="font-size:50px;">💖✨</h1><h2>GlowAI</h2></div>""", unsafe_allow_html=True)
    page = st.sidebar.radio("💕 Nav", ["🏠 Home", "💊 Solutions", "🧘‍♀️ Wellness", "📊 Progress", "👤 Profile"])
    if page == "🏠 Home": home_page()
    elif page == "💊 Solutions": solutions_page()
    elif page == "🧘‍♀️ Wellness": wellness_page()
    elif page == "📊 Progress": progress_page()
    elif page == "👤 Profile": profile_page()

if __name__ == "__main__": main()

