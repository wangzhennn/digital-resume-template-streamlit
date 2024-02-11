from pathlib import Path

import streamlit as st
from PIL import Image
import streamlit.components.v1 as components

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile.png"
sdf_dig = current_dir / "assets" / "sdf_dig_Zhen_Vfinal.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Zhen Wang"
PAGE_ICON = "🌟"
NAME = "Zhen Wang"
DESCRIPTION = """
Master student majoring in Human Resource Management and minor in Data Science. Seeking for Ph.D. in People Analytics
"""
EMAIL = "wangzhen611@ruc.edu.cn"
SOCIAL_MEDIA = {
    "YouTube": "https://youtube.com/c/codingisfun",
    "LinkedIn": "https://linkedin.com",
    "GitHub": "https://github.com",
    "Twitter": "https://twitter.com",
}
PROJECTS = {
    "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
    "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
    "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
    "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)
sdf_dig=Image.open(sdf_dig)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream")
    
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- Research Interest ---
st.write('\n')
st.subheader("Reserach Interest")
st.write("---")
st.write(
    """
- 📈 **Human resource analytics**: Generate insights employing computational techniques on unstructured multimodal data
- 📊 **Individual outcome** (emotional/attitudinal/behavioral) from applying of advanced technologies in HRM, e.g., computerized performance monitoring system
"""
)

# --- Project Portfolio  ---
st.write('\n')
st.subheader("Project Portfolio")
st.write("---")
# --- Project Portfolio 1 ---
st.write("**Leadership: Research Progress of past 5 years**")
st.write("10/2022 - 11/2022")
st.write("Based on Scopus publication data, this project employed Natural Language Processing models to identify key research topics in the leadership field (Organizational Behavior area) and analyzed the dynamic trend over the past 5 years. Additionally, this project applied Network Analysis on top author/author corporation network analysis (Grade:12/12)")
components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vSFaYEd2daBIaExYXzmtnwazls35nTVOLztx4Yqv6-W-f3ls9-vfaU4XwL45FCM6A/embed?start=true&loop=false&delayms=3000", height=432)
st.write("---")
# --- Project Portfolio 2 ---
st.write("**Employee Attrition Analysis for company X**")
st.write("10/2022 - 11/2022")
st.write("Aiming at understanding the rationale for employees’ attrition, this project employed machine learning on employees' feature data to profile employee groups with various attrition levels and identify the attrition impact factors for the high attrition groups. After figuring out income as the rooted driven factor, this project further diagnosed and outlined income internal fairness problems (Grade: 12/12)")
components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vSOE_ScAWIoVZPNIyuLGhF_0O4PrFGQf6TW6sF7pCAfsl_mL7KLmSn0YE7VskCkLg/embed?start=true&loop=false&delayms=3000", height=432)
st.write("---")
# --- Project Portfolio 3 ---
st.write("**User Analysis for The Safe Delivery App of Maternity Foundation**")
st.write("11/2022 - 01/2023")
st.write("Aiming to identify and reactivate dormant App users, this project conducted user journey, profile and usage analysis with App footprint data. Specifically, this project employed machine learning on dormant user identification and feature analysis, and leveraged results with customized suggestions for different user profiles. For project management, this project applied a hybrid model of CRISP-DM and the agile method as the main guideline")
components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vQqmEq54pq2uxKTH_nTKvj0efOIL5gZ6CcR495oEKBxQj0sA8-yczeeqDzv3UUXGQ/embed?start=true&loop=false&delayms=3000", height=432)
st.write("---")
# --- Project Portfolio 4 ---
st.write("**Reducing Employees’ Time Theft through Supervisor Developmental Feedback: A Serial Multiple Mediation Model of Perceived Insider Status and Work Passion**")
st.write("09/2022 - 02/2024")
st.write("Drawing the intensified ‘cat-and-mouse game’ between leaders and employees in combating time theft with the evolution of technologies, this study aims to identify how to encourage employees to proactively perform work roles more appropriately instead of using punitive actions. Study 2 further employed NLP to analyze feedback topics and differential influence")
st.image(sdf_dig, width=700)
st.write("---")



# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
