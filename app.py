from pathlib import Path

import streamlit as st
from PIL import Image
import streamlit.components.v1 as components

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile.png"
sdf_01 = current_dir / "assets" / "sdf_01.png"
sdf_02 = current_dir / "assets" / "sdf_02.png"
ceo_01 = current_dir / "assets" / "ceo_01.png"
sdf_04 = current_dir / "assets" / "sdf_04.png"

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
sdf_01=Image.open(sdf_01)
sdf_02=Image.open(sdf_02)
ceo_01=Image.open(ceo_01)
sdf_04=Image.open(sdf_04)

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
st.write("09/2022 - 02/2024 | Under SSCI Journal Review")
st.write("Time theft has become a growing issue in organizations, notably due to the rapid shift to remote work prompted by the pandemic. Existing studies demonstrate both authoritarian leadership and laissez-faire leadership can exacerbate time theft, putting leaders in a behavioral dilemma of neither being strict nor lenient. Additionally, the pervasive and covert nature of time theft diminishes the effectiveness of afterward corrective actions. Our study aims to investigate how to prevent time theft by mitigating employees’ inclinations. Based on role theory, our study examines if supervisor developmental feedback can encourage employees to perform work roles more appropriately. To uncover the complicated internalization process of role expectation, our study incorporates perceived insider status and work passion as serial mediators and considers the boundary effect of leaders’ word-deed consistency. In Study 1, a survey of 483 employees revealed that supervisor developmental feedback can negatively predict employee time theft through employees’ perceived insider status and work passion. Study 2 further identifies three topics of supervisor developmental feedback: skill learning, attitude learning, and social learning. Moreover, serial multiple mediating effects are affirmed across topics. The findings suggest that providing feedback information on employees’ learning and growth is an effective approach to prevent time theft")
st.image(sdf_01, width=700)
st.image(sdf_02, width=700)
st.write("---")
# --- Project Portfolio 5 ---
st.write("**Does Inside CEO Matter for Chinese Family Firm Innovative Performance: The Moderating Role of Market Turbulence and CEO Overconfidence**")
st.write("12/2023 - 02/2024 | Submitted to SSCI Journal")
st.write("While CEOs play crucial roles in shaping family firms’ innovation strategies, existing studies remain controversial on which CEO succession origin, i.e. inside CEOs or outside CEOs, can better increase family firms’ innovative performance. This study extends current research by considering the boundary effects of macro environmental contingency and micro CEO psychological bias. Using a sample of 194 Chinese family firms from 2007 to 2019, our findings suggest that inside CEOs perform better than outside CEOs in family firms’ innovative performance. Furthermore, the impact of CEO succession origin on innovative performance is weaker in the context of higher market turbulence")
st.image(ceo_01, width=600)
st.write("---")
# --- Project Portfolio 4 ---
st.write("**A Literature Review of Supervisor Developmental Feedback**")
st.write("01/2021 - 06/2021 | Bachelor's thesis, Grade: A")
st.write("Based on massive supervisor developmental feedback (SDF) studies published in SSCI/CSSCI journals over the past two decades, this study clarifies the concept and measurements of SDF, categorizes existing research theories and summarizes influential mechanisms. Following these, various future research directions are proposed")
st.image(sdf_04, width=700)
st.write("---")




# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
