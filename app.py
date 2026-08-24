import streamlit as st
import pandas as pd
import numpy as np

# Page Configuration
st.set_page_config(
    page_title="Yogita Dokh | Data Analyst Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Advanced CSS Injection for Modern Styling
st.markdown("""
    <style>
    /* Gradient Headers */
    .hero-title {
        font-size: 2.8rem;
        font-weight: 800;
        background: -webkit-linear-gradient(45deg, #1E3A8A, #3B82F6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.2rem;
    }
    .hero-subtitle {
        font-size: 1.3rem;
        color: #4B5563;
        font-weight: 500;
        margin-bottom: 1.5rem;
    }
    
    /* Highlight Card Styling */
    .metric-container {
        background-color: #FFFFFF;
        border: 1px solid #E5E7EB;
        border-radius: 12px;
        padding: 1.2rem;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        text-align: center;
    }
    .metric-value {
        font-size: 2rem;
        font-weight: 700;
        color: #1E3A8A;
    }
    .metric-label {
        font-size: 0.9rem;
        color: #6B7280;
    }
    
    /* Skills Badge Styling */
    .skill-badge {
        display: inline-block;
        background-color: #EFF6FF;
        color: #1E40AF;
        padding: 6px 14px;
        margin: 4px;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        border: 1px solid #BFDBFE;
    }
    
    /* Project Card Styling */
    .project-card {
        background: #FFFFFF;
        border-radius: 10px;
        padding: 1.5rem;
        border: 1px solid #E5E7EB;
        margin-bottom: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=110)
    st.title("Yogita Dokh")
    st.caption("📍 Pune, India")
    
    st.markdown("---")
    st.markdown("### 📬 Connect With Me")
    st.markdown("[💼 LinkedIn Profile](https://www.linkedin.com/in/Yogita-Dokh)")
    st.markdown("[💻 GitHub Profile](https://github.com/YogitaDokh)")
    st.markdown("📧 **dokhyogita20@gmail.com**")
    st.markdown("📞 **+91-8459341135**")
    st.markdown("---")
    
    # Read the PDF file from the repository to make it downloadable
    with open("Yogita_Dokh_Data_Analyst.pdf", "rb") as file:
         pdf_data = file.read()
      
    st.download_button(
        label="📄 Download Full Resume",
        data=pdf_data,
        file_name="Yogita_Dokh_Data_Analyst.pdf",
        mime="application/pdf",
        use_container_width=True
    )

# --- HERO SECTION ---
st.markdown('<div class="hero-title">Yogita Dokh</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-subtitle">Aspiring Data Analyst | Driving Business Value Through Data</div>', unsafe_allow_html=True)

st.write("""
B.Tech CS (Data Science) graduate specialized in turning complex, messy data into interactive business intelligence dashboards and predictive models. Proven track record in improving data accuracy, streamlining reporting pipelines, and uncovering high-value business trends[cite: 1].
""")

st.markdown("---")

# --- RECRUITER HIGHLIGHT METRICS ---
st.subheader("💡 Key Impact Metrics")
m1, m2, m3, m4 = st.columns(4)

with m1:
    st.markdown("""
    <div class="metric-container">
        <div class="metric-value">25%</div>
        <div class="metric-label">Data Accuracy Boost</div>
    </div>
    """, unsafe_allow_html=True)

with m2:
    st.markdown("""
    <div class="metric-container">
        <div class="metric-value">30%</div>
        <div class="metric-label">Report Time Saved</div>
    </div>
    """, unsafe_allow_html=True)

with m3:
    st.markdown("""
    <div class="metric-container">
        <div class="metric-value">85%+</div>
        <div class="metric-label">ML Model Accuracy</div>
    </div>
    """, unsafe_allow_html=True)

with m4:
    st.markdown("""
    <div class="metric-container">
        <div class="metric-value">50k+</div>
        <div class="metric-label">Records Analyzed</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# --- TECHNICAL SKILLS BADGES ---
st.subheader("🧰 Technical Arsenal")
skills = [
    "Python", "SQL", "Power BI", "Tableau", "Pandas", "NumPy", 
    "Scikit-Learn", "SMOTE", "Excel (VLOOKUP/XLOOKUP)", "MySQL", 
    "Git/GitHub", "EDA", "Statistical Analysis", "Dashboarding"
]
badge_html = "".join([f'<span class="skill-badge">{s}</span>' for s in skills])
st.markdown(badge_html, unsafe_allow_html=True)

st.markdown("---")

# --- MAIN CONTENT TABS ---
tab_proj, tab_exp, tab_interactive, tab_edu = st.tabs([
    "🚀 High-Impact Projects", 
    "💼 Internship Experience", 
    "📊 Live Interactive Demo", 
    "🎓 Education & Certifications"
])

# PROJECTS TAB
with tab_proj:
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.markdown("""
        <div class="project-card">
            <h3>🛒 E-Commerce Sales Analytics Dashboard</h3>
            <p><strong>Technologies:</strong> Python, Power BI, SMOTE, Hyperparameter Tuning</p>
            <ul>
                <li>Analyzed over <strong>50,00+ sales records</strong> to uncover regional revenue trends and product profitability metrics[cite: 1].</li>
                <li>Applied <strong>SMOTE</strong> and hyperparameter tuning via GridSearchCV to tackle class imbalance, increasing recall by <strong>12%</strong>[cite: 1].</li>
                <li>Designed an interactive Power BI dashboard displaying <strong>10+ core KPIs</strong> for executive decision-making[cite: 1].</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("[🔗 View GitHub Repository](https://github.com/YogitaDokh/ecommerce-sales-analytics)")

    with col_b:
        st.markdown("""
        <div class="project-card">
            <h3>👥 HR Attrition Analytics Dashboard</h3>
            <p><strong>Technologies:</strong> Python, Scikit-learn, Power BI Desktop, DAX</p>
            <ul>
                <li>Built a predictive machine learning pipeline with <strong>85%+ classification accuracy</strong> to forecast employee turnover[cite: 1].</li>
                <li>Cleaned and conducted EDA on <strong>1,400+ employee profiles</strong>, identifying root drivers behind staff attrition[cite: 1].</li>
                <li>Constructed <strong>5+ interactive visuals</strong> for HR executives to plan targeted retention strategies[cite: 1].</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("[🔗 View GitHub Repository](https://github.com/YogitaDokh/HR_Attrition_Analytics)")

# EXPERIENCE TAB
with tab_exp:
    st.markdown("### Data Analyst Intern")
    st.markdown("**Elevate Labs Pvt. Ltd.** | *Jan 2026 – Apr 2026*[cite: 1]")
    st.markdown("""
    - **Data Cleaning & Pipeline Optimization:** Handled 10,000+ raw records using Python (Pandas) and Excel, improving data accuracy by 25% across datasets[cite: 1].
    - **Exploratory Data Analysis (EDA):** Executed EDA across 5+ diverse datasets, isolating key trends that boosted decision-making efficiency by 20%[cite: 1].
    - **Dashboarding & Reporting:** Designed 8+ interactive dashboards using Power BI, Seaborn, and Matplotlib, cutting reporting overhead by 30%[cite: 1].
    """)

# LIVE INTERACTIVE DEMO TAB (Recruiters love testing real data interactions)
with tab_interactive:
    st.markdown("### 📈 Interactive Sample Data Visualizer")
    st.caption("Demonstrating real-time data handling capabilities within Streamlit.")
    
    # Generate Mock Sales Data
    np.random.seed(42)
    df = pd.DataFrame({
        "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        "Sales ($)": np.random.randint(20000, 50000, 6),
        "Transactions": np.random.randint(500, 1500, 6),
        "Customer Satisfaction (%)": np.random.randint(80, 99, 6)
    })
    
    col_d1, col_d2 = st.columns([1, 2])
    with col_d1:
        st.markdown("#### Sample Dataset")
        st.dataframe(df, use_container_width=True)
    
    with col_d2:
        st.markdown("#### Dynamic Revenue Trend")
        st.line_chart(df.set_index("Month")["Sales ($)"])

# EDUCATION & CERTIFICATIONS TAB
with tab_edu:
    col_e1, col_e2 = st.columns(2)
    with col_e1:
        st.markdown("### 🎓 Education")
        st.markdown("**B.Tech in CSE (Data Science)**")
        st.write("Shreeyash College of Engineering and Technology, Chh. Sambhajinagar")
        st.write("• **CGPA:** 8.45 / 10")
        st.write("• **Duration:** 2022 – 2026")
        
        st.markdown("---")
        st.markdown("**Higher Secondary Certificate (HSC)**")
        st.write("Swami Bramhanand Vidyalay")
        st.write("• **Percentage:** 82.15%")

    with col_e2:
        st.markdown("### 📜 Certifications")
        st.markdown("🏅 **Gen AI Mastermind** – Outskill")
        st.write("Specialized coursework in applied generative models and advanced AI workflows.")

# FOOTER CONTACT FORM
st.markdown("---")
st.subheader("📬 Send Me a Direct Message")
with st.form("contact_form"):
    name = st.text_input("Your Name / Recruiter Name")
    email = st.text_input("Your Email")
    message = st.text_area("Message")
    submit = st.form_submit_button("Submit Message")
    
    if submit:
        st.success("Thank you for reaching out! I will respond promptly.")
