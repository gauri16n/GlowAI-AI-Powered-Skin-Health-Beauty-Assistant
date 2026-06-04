# ✨ GLOWAI - Complete Product Documentation

## AI Skin Health & Facial Analysis Assistant

---

## 📋 TABLE OF CONTENTS

1. [Product Overview](#product-overview)
2. [Features List](#features-list)
3. [User Workflow](#user-workflow)
4. [UI/UX Design](#uiux-design)
5. [Screen-by-Screen Design](#screen-by-screen-design)
6. [Ayurvedic Products](#ayurvedic-products)
7. [Wellness & Exercises](#wellness--exercises)
8. [Technical Architecture](#technical-architecture)
9. [Data Flow](#data-flow)
10. [Database Schema](#database-schema)
11. [Implementation Guide](#implementation-guide)

---

## 🌟 PRODUCT OVERVIEW

### Vision
**GlowAI** is an AI-powered skincare assistant that helps women analyze their skin health daily using facial image analysis and provides personalized skincare recommendations, wellness guidance, and progress tracking.

### Target Audience
- Women aged 18-55
- Skincare enthusiasts
- People wanting to track skin improvement
- Beauty-conscious individuals

---

## 🎯 FEATURES LIST

### Core AI Features
| Feature | Description | Status |
|---------|-------------|--------|
| Face Image Upload | Upload selfie/photo for analysis | ✅ Ready |
| Wrinkle Detection | Detect fine lines and wrinkles | ✅ Ready |
| Dark Spot Detection | Identify pigmentation issues | ✅ Ready |
| Puffy Eye Detection | Analyze under-eye puffiness | ✅ Ready |
| Skin Age Prediction | AI predicts skin age vs real age | ✅ Ready |
| Health Score | Calculate overall skin health (0-100) | ✅ Ready |
| Heatmap Visualization | Show affected skin areas | 🔄 Coming |
| Acne Detection | Detect pimples and breakouts | 🔄 Coming |
| Blackhead Detection | Identify blackhead prone areas | 🔄 Coming |

### Skincare Features
| Feature | Description |
|---------|-------------|
| Morning Routine | Personalized AM skincare steps |
| Night Routine | Personalized PM skincare steps |
| Product Recommendations | Based on skin issues |
| Ingredient Advice | What to look for/avoid |
| Skin Type Detection | Oily/Dry/Combination/Sensitive |

### Wellness Features
| Feature | Description |
|---------|-------------|
| Face Yoga | Guided facial exercises |
| Meditation | Stress reduction sessions |
| Breathing Exercises | Relaxation techniques |
| Facial Massage | At-home massage routines |
| Lifestyle Tips | Daily health advice |

### Ayurvedic Features
| Feature | Description |
|---------|-------------|
| Ayurvedic Products | Natural/herbal recommendations |
| Dosha Analysis | Vata/Pitta/Kapha skin types |
| Herbal Remedies | Traditional solutions |
| Oil Massages | Abhyanga techniques |
| Diet Suggestions | Ayurvedic nutrition |

### Tracking Features
| Feature | Description |
|---------|-------------|
| Daily Scan History | Track each analysis |
| Weekly Progress | Compare week over week |
| Score Trends | Health score charts |
| Issue Improvement | Track specific issues |
| Export Data | Download as CSV |

---

## 🔄 USER WORKFLOW

### Daily User Journey

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        GLOWAI USER WORKFLOW                                 │
└─────────────────────────────────────────────────────────────────────────────┘

                              ┌──────────────┐
                              │   👋 OPEN    │
                              │     APP      │
                              └──────┬───────┘
                                     │
                                     ▼
                              ┌──────────────┐
                              │  👤 LOGIN   │
                              │ (Optional)   │
                              └──────┬───────┘
                                     │
                                     ▼
                              ┌──────────────┐
                              │   🏠 HOME   │
                              │   DASHBOARD │
                              └──────┬───────┘
                                     │
              ┌──────────────────────┴──────────────────────┐
              │                                               │
              ▼                                               ▼
       ┌──────────────┐                              ┌──────────────┐
       │  📸 SCAN     │                              │  📊 ANALYTICS│
       │    FACE     │                              │   HISTORY    │
       └──────┬───────┘                              └──────┬───────┘
              │                                               │
              ▼                                               │
       ┌──────────────┐                                       │
       │ 📤 UPLOAD   │                                       │
       │   PHOTO     │                                       │
       └──────┬───────┘                                       │
              │                                               │
              ▼                                               │
       ┌──────────────┐                                       │
       │ 🔬 ANALYZE  │                                       │
       │    AI       │                                       │
       └──────┬───────┘                                       │
              │                                               │
              ▼                                               │
       ┌──────────────┐                                       │
       │ 📊 GET      │                                       │
       │  RESULTS    │                                       │
       │ • Score    │                                       │
       │ • Issues   │                                       │
       │ • Age      │                                       │
       └──────┬───────┘                                       │
              │                                               │
              ▼                                               │
       ┌──────────────┐                              ┌──────────────┐
       │ 💊 GET      │                              │ 📈 VIEW      │
       │ RECOMMENDS  │                              │  PROGRESS    │
       │ • Routine   │                              └──────────────┘
       │ • Products  │
       │ • Lifestyle │
       └──────┬───────┘
              │
              ▼
       ┌──────────────┐
       │ 🧘 WELLNESS │
       │ • Yoga      │
       │ • Meditate  │
       │ • Exercises │
       └──────┬───────┘
              │
              ▼
       ┌──────────────┐
       │ 💾 DATA     │
       │   SAVED     │
       └──────────────┘
```

### Weekly Tracking Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       WEEKLY TRACKING FLOW                                   │
└─────────────────────────────────────────────────────────────────────────────┘

     ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐
     │  MON    │    │  TUE    │    │  WED    │    │  THU    │    │  FRI    │
     │ Scan 1  │    │ Scan 2  │    │ Scan 3  │    │ Scan 4  │    │ Scan 5  │
     └────┬────┘    └────┬────┘    └────┬────┘    └────┬────┘    └────┬────┘
          │              │              │              │              │
          └──────────────┴──────────────┴──────────────┴──────────────┘
                                         │
                                         ▼
                                  ┌─────────────┐
                                  │  📊 STORE  │
                                  │   IN DB    │
                                  └──────┬──────┘
                                         │
                                         ▼
                                  ┌─────────────┐
                                  │ 📈 WEEKLY  │
                                  │  REPORT    │
                                  └──────┬──────┘
                                         │
           ┌──────────────────────────────┼──────────────────────────────┐
           │                              │                              │
           ▼                              ▼                              ▼
    ┌─────────────┐              ┌─────────────┐              ┌─────────────┐
    │Health Score│              │Issue       │              │Comparison  │
    │Chart       │              │Trends      │              │vs Last Week│
    └─────────────┘              └─────────────┘              └─────────────┘
```

---

## 🎨 UI/UX DESIGN

### Color Palette

| Color Name | Hex Code | Usage |
|------------|----------|-------|
| **Primary Pink** | #E8B4BC | Main buttons, accents |
| **Secondary Lavender** | #C3AED6 | Secondary elements |
| **Soft Peach** | #FFB6C1 | Highlights |
| **Light Pink** | #FFE4E9 | Background tints |
| **Deep Rose** | #D4A5A5 | Active states |
| **White** | #FFFFFF | Cards, backgrounds |
| **Soft Gray** | #F8F8F8 | Page background |
| **Text Dark** | #4A4A4A | Primary text |
| **Text Light** | #8E8E8E | Secondary text |
| **Success Green** | #98D8C8 | Good scores |
| **Warning Yellow** | #F7DC6F | Moderate scores |
| **Alert Red** | #F1948A | Low scores |

### Typography

| Element | Font | Size | Weight |
|---------|------|------|--------|
| App Title | Poppins | 32px | Bold |
| Page Titles | Poppins | 24px | SemiBold |
| Section Headers | Poppins | 18px | Medium |
| Body Text | Inter | 14px | Regular |
| Small Text | Inter | 12px | Regular |
| Button Text | Poppins | 14px | SemiBold |

### Design Principles

1. **Soft & Feminine** - Rounded corners (16px), gentle shadows
2. **Clean Layout** - Plenty of white space
3. **Card-Based** - Information in beautiful cards
4. **Smooth Transitions** - Animated hover effects
5. **Beauty Icons** - Custom skincare icons

### UI Components

```
┌─────────────────────────────────────┐
│         CARD COMPONENT              │
│  ┌─────────────────────────────┐  │
│  │      🖼️ Image Area          │  │
│  └─────────────────────────────┘  │
│  ┌─────────────────────────────┐  │
│  │      Title Text             │  │
│  │      Description text       │  │
│  │      goes here nicely       │  │
│  └─────────────────────────────┘  │
│         💝 Rounded corners         │
│         📐 Soft shadow             │
└─────────────────────────────────────┘
```

---

## 📱 SCREEN-BY-SCREEN DESIGN

### 1. HOME DASHBOARD

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  ✨ GLOWAI                                              👤 Profile   ⚙️    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Good Morning, Beautiful! 💕                                               │
│  Let's check your skin today                                               │
│                                                                             │
│  ┌───────────────────────────────────────────────────────────────────┐    │
│  │                                                                   │    │
│  │                     💆 SKIN HEALTH SCORE 💆                      │    │
│  │                                                                   │    │
│  │                           85                                       │    │
│  │                                                                   │    │
│  │                      EXCELLENT 🟢                                 │    │
│  │                                                                   │    │
│  └───────────────────────────────────────────────────────────────────┘    │
│                                                                             │
│  Last Scan: Today, 10:30 AM                                                │
│                                                                             │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐     │
│  │   👵        │  │   🟤        │  │   👁️        │  │   😴        │     │
│  │  Wrinkles  │  │ Dark Spots │  │ Puffy Eyes │  │   Acne     │     │
│  │    12%     │  │    8%      │  │    5%      │  │    3%      │     │
│  │   Good     │  │   Good     │  │   Good     │  │   Good     │     │
│  └─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘     │
│                                                                             │
│  ╔═══════════════════════════════════════════════════════════════════════╗  │
│  ║                    📸 SCAN MY SKIN                                  ║  │
│  ║                   [ Take Photo / Upload ]                             ║  │
│  ╚═══════════════════════════════════════════════════════════════════════╝  │
│                                                                             │
│  ─────────────────── Today's Routine ───────────────────                   │
│                                                                             │
│  ☀️ Morning:  Gentle Cleanser → Vitamin C → Moisturizer → SPF           │
│  🌙 Night:   Oil Cleanser → Retinol → Night Cream                         │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 2. FACE SCAN SCREEN

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  ← Back         📸 Face Scan                                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Tips for best results:                                                    │
│  ✓ Natural lighting                                                        │
│  ✓ Face straight to camera                                                │
│  ✓ No makeup                                                              │
│  ✓ Clean face                                                             │
│                                                                             │
│  ┌───────────────────────────────────────────────────────────────────┐    │
│  │                                                                   │    │
│  │                                                                   │    │
│  │                                                                   │    │
│  │                    📷 DROP IMAGE HERE                            │    │
│  │                                                                   │    │
│  │                    or                                             │    │
│  │                                                                   │    │
│  │                    📸 Take Photo                                  │    │
│  │                                                                   │    │
│  │                                                                   │    │
│  └───────────────────────────────────────────────────────────────────┘    │
│                                                                             │
│  ┌───────────────────────────────────────────────────────────────────┐    │
│  │                                                                   │    │
│  │                    🔬 ANALYZE MY SKIN                            │    │
│  │                                                                   │    │
│  └───────────────────────────────────────────────────────────────────┘    │
│                                                                             │
│                      Analyzing... ████████░░ 80%                          │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 3. RESULTS SCREEN

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  ← Back              Your Skin Analysis                                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌───────────────────────────────────────────────────────────────────┐    │
│  │                     🎯 HEALTH SCORE                               │    │
│  │                           82                                      │    │
│  │                        EXCELLENT 🟢                              │    │
│  └───────────────────────────────────────────────────────────────────┘    │
│                                                                             │
│  Your Skin Age: 28 years    Real Age: 25 years    (+3 - You're glowing!)│
│                                                                             │
│  ┌──────────────────┐ ┌──────────────────┐ ┌──────────────────┐          │
│  │     👵          │ │      🟤         │ │      👁️         │          │
│  │   Wrinkles     │ │  Dark Spots     │ │  Puffy Eyes    │          │
│  │      15%       │ │      10%        │ │       5%       │          │
│  │    Low 🟢     │ │    Low 🟢      │ │    Low 🟢     │          │
│  └──────────────────┘ └──────────────────┘ └──────────────────┘          │
│                                                                             │
│  ┌──────────────────┐ ┌──────────────────┐                              │
│  │      😫         │ │     🫧          │                              │
│  │     Acne       │ │  Blackheads     │                              │
│  │       3%       │ │       2%        │                              │
│  │    Low 🟢    │ │    Low 🟢      │                              │
│  └──────────────────┘ └──────────────────┘                              │
│                                                                             │
│  [ View Heatmap ]  [ View Annotated Image ]  [ Share Results ]           │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 4. RECOMMENDATIONS SCREEN

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  ← Back         💊 Your Personalized Routine                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌───────────────────────────────────────────────────────────────────┐    │
│  │                    ☀️ MORNING ROUTINE                            │    │
│  │                                                                   │    │
│  │  1. 🧴 Gentle Cleanser - CeraVe Hydrating Cleanser              │    │
│  │  2. 💫 Vitamin C Serum - 15% L-Ascorbic Acid                     │    │
│  │  3. 💧 Moisturizer - Hyaluronic Acid                             │    │
│  │  4. ☀️ SPF 50 Sunscreen - Mineral Based                          │    │
│  └───────────────────────────────────────────────────────────────────┘    │
│                                                                             │
│  ┌───────────────────────────────────────────────────────────────────┐    │
│  │                    🌙 NIGHT ROUTINE                               │    │
│  │                                                                   │    │
│  │  1. 🫒 Oil Cleanser - Remove makeup                               │    │
│  │  2. 🧴 Gentle Cleanser                                            │    │
│  │  3. 🌟 Retinol 0.5% - Anti-aging                                 │    │
│  │  4. 💧 Night Cream - Niacinamide                                  │    │
│  └───────────────────────────────────────────────────────────────────┘    │
│                                                                             │
│  ┌───────────────────────────────────────────────────────────────────┐    │
│  │                    💡 LIFESTYLE TIPS                             │    │
│  │                                                                   │    │
│  │  💧 Drink 8 glasses water daily                                  │    │
│  │  😴 Get 7-8 hours of sleep                                       │    │
│  │  🌞 Apply sunscreen every 2 hours                                 │    │
│  │  🥗 Eat vitamin-rich foods                                        │    │
│  │  🚭 Avoid smoking                                                  │    │
│  │  🍺 Limit alcohol                                                  │    │
│  └───────────────────────────────────────────────────────────────────┘    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 5. WELLNESS SCREEN

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  🧘              WELLNESS & SELF-CARE                    💆              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌───────────────────────────────────────────────────────────────────┐    │
│  │                    🧘 FACE YOGA EXERCISES                        │    │
│  │                                                                   │    │
│  │  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ │    │
│  │  │  👄 Lip     │ │  👁️ Eye    │ │  😊 Cheek  │ │  🧖 Forehead│ │    │
│  │  │  Exercise  │ │  Exercise  │ │  Exercise  │ │  Exercise  │ │    │
│  │  │   2 min   │ │   3 min   │ │   2 min   │ │   2 min   │ │    │
│  │  └─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘ │    │
│  └───────────────────────────────────────────────────────────────────┘    │
│                                                                             │
│  ┌───────────────────────────────────────────────────────────────────┐    │
│  │                    🧘 GUIDED MEDITATION                          │    │
│  │                                                                   │    │
│  │  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐                 │    │
│  │  │  🌅 Morning │ │  😫 Stress │ │  😴 Sleep  │                 │    │
│  │  │  5 min     │ │  10 min    │ │  15 min   │                 │    │
│  │  └─────────────┘ └─────────────┘ └─────────────┘                 │    │
│  └───────────────────────────────────────────────────────────────────┘    │
│                                                                             │
│  ┌───────────────────────────────────────────────────────────────────┐    │
│  │                    💆 FACIAL MASSAGE                             │    │
│  │                                                                   │    │
│  │  • Daily 5-minute massage routine                                 │    │
│  │  • Acupressure points for glowing skin                           │    │
│  │  • Lymphatic drainage techniques                                 │    │
│  └───────────────────────────────────────────────────────────────────┘    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 6. PROGRESS TRACKER

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  📊                      PROGRESS TRACKER                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  This Week: Score 82 (+5 from last week) 🟢                               │
│                                                                             │
│  ┌───────────────────────────────────────────────────────────────────┐    │
│  │               📈 SKIN HEALTH SCORE TREND                         │    │
│  │                                                                   │    │
│  │      █                                                         │    │
│  │      █  █                                                     │    │
│  │  █  █  █  █  █  █  █                                       │    │
│  │  Mon Tue Wed Thu Fri Sat Sun                                  │    │
│  │  77  79  80  81  82  82  82                                 │    │
│  └───────────────────────────────────────────────────────────────────┘    │
│                                                                             │
│  ┌────────────────────────┐  ┌────────────────────────┐                   │
│  │   👵 Wrinkle Trend    │  │   🟤 Dark Spot Trend │                   │
│  │   -3% Improvement    │  │   -2% Improvement    │                   │
│  │   ████▓▓▓░░░░░       │  │   ████▓▓▓░░░░░       │                   │
│  └────────────────────────┘  └────────────────────────┘                   │
│                                                                             │
│  ┌────────────────────────┐  ┌────────────────────────┐                   │
│  │   👁️ Puffy Eye Trend │  │    😫 Acne Trend      │                   │
│  │   -1% Improvement    │  │   -2% Improvement    │                   │
│  │   ███▓▓▓░░░░░░░      │  │   ███▓▓▓░░░░░░░      │                   │
│  └────────────────────────┘  └────────────────────────┘                   │
│                                                                             │
│  Scan History: 15 scans this month                                         │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 🌿 AYURVEDIC PRODUCTS
   - Restart: `uvicorn src.api.main:app --reload`

3. **Dashboard not loading**
   - Check port availability
   - Try: `streamlit run src/dashboard/app.py --server.port 8501`

---

## License

MIT License

---

**GlowAI** - Your Personal AI Skin Health Assistant ✨


