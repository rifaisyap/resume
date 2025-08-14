import streamlit as st
from PIL import Image

# Header card and photo
image = Image.open('photo.JPEG')

col1, col2 = st.columns([1, 3])
with col1:
    st.image(image, use_container_width=True)

with col2:
    st.markdown("### **Rifa Aisya Putri**")
    st.markdown(
        "Business Analysis | E-commerce | Marketing & Campaign Strategy"
    )
    st.markdown(
        """
        📍 Singapore  
        📧 rifa.putriaisya@gmail.com  
        📞 (65) 9867 7022
        """
    )

# Summary section
st.subheader("💡 Summary")
st.markdown(
        """
        **•** More than four years of experience in the e-commerce industry, specialising in data analysis, affiliate marketing, and campaign strategy.  

        **•** Skilled in translating insights into action through budget management, performance optimisation, cross-functional campaigns, fraud prevention, and product development.  

        **•** Sole recipient of ByteDance Individual Spot Award in department for outstanding performance. Recognised as a reliable, collaborative, and data-driven team member with a passion for continuous improvement.  
        """
    )


# Skills section
st.subheader("🎯 Skills")
# Business & Marketing Skills
st.markdown(
    "**Business & Marketing Skills:** "
    "Affiliate marketing, campaign management, budgeting & target setting, "
    "data analysis & visualisation, stakeholder management, "
    "presentation & communication, team collaboration & leadership"
)

# Technical Skills
st.markdown(
    "**Technical Skills:** "
    "SQL, Python"
)

# Work Experience section
st.markdown("<br>", unsafe_allow_html=True) 
st.subheader("💼 Work Experiences")
# Shopee – Indonesia
st.markdown("**Shopee – Indonesia**")
st.markdown("_Senior Associate - Marketing Growth & Strategy_ | Nov 2024 – Jan 2025")
st.write(
    "- Acted as campaign lead, managing end-to-end marketing campaigns including strategy, budgeting, execution, and performance analysis. Partnered with cross-functional teams to deliver a campaign resulting in an 18% uplift in orders."
)
st.write(
    "- Teamed up with product team to develop new features, streamlining campaign operations and improving efficiency, resulting in a 39% increase in campaign registrations."
)

# ByteDance – Indonesia
st.markdown("**ByteDance – Indonesia**")
st.markdown("_Creator Strategy_ | Jul 2024 – Nov 2025")
st.write(
    "- Monitored performance and budget tracking for social commerce programs, delivering data-driven insights and recommendations that contributed to a 3 percentage point increase in monthly contribution to marketplace orders."
)
st.write(
    "- Collaborated with data science and engineering teams to integrate data between Tokopedia and ByteDance, streamlining reporting processes and reducing manual data requests via a new performance dashboard."
)
st.write(
    "- Defined key success metrics and collaborated with product and business teams to launch and drive adoption of a link-sharing program, enabling TikTok users to share product links outside the platform."
)

# Tokopedia – Affiliate Business Associate
st.markdown("_Affiliate Business Associate (Analysis & Budgeting) – Tokopedia_ | Dec 2012 – Jul 2024")
st.write(
    "- Led data operations for affiliate program from its public launch, overseeing performance monitoring, establishing reporting standards, and enhancing data accuracy, contributing to order growth and higher share of marketplace transactions."
)
st.write(
    "- Designed monthly and annual performance targets and budgets, achieving ~50% cost savings by optimising commission structures based on business priorities and market conditions."
)
st.write(
    "- Identified patterns and prevented fraudulent activities by developing fraud detection rules and mechanisms, saving over IDR 4 billion."
)
st.write(
    "- Worked on cross-functional initiatives including product development and campaign optimisation, contributing to a 15%+ increase in seller-funded commissions to improve program sustainability."
)

# Education section
st.markdown("<br>", unsafe_allow_html=True) 
st.subheader("🎓 Education")

st.markdown(
    "**MSc in Business Analytics, Nanyang Technological University, Singapore**  \n"
    "_Jul 2025 – Jun 2026 (expected)_"
)

st.markdown(
    "**Bachelor of Communication, Bakrie University, Indonesia**  \n"
    "_Jul 2016 – Feb 2020_"
)


# Create LinkedIn button# Title

# Shifted slightly to the right
col1, col2, col3 = st.columns([1.5, 2, 0.5])
with col2:
    st.link_button(
        "👋🏻 Connect on LinkedIn",
        "https://www.linkedin.com/in/rifaaisyaputri/"
    )