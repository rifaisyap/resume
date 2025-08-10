import streamlit as st
from PIL import Image

# Header card and photo
image = Image.open('photo.JPEG')

col1, col2 = st.columns([1, 3])
with col1:
    st.image(image, use_container_width=True)

with col2:
    st.markdown("""
        <div style='font-size: 32px; font-weight: bold; margin-bottom: 5px;'>Rifa Aisya Putri</div>
        <p style='margin-top: 0; font-size: 19px;'>Business Analysis | E-commerce | Marketing & Campaign Strategy</p>
        <p style='color: gray; margin-top: 5px;'>📍 Singapore<br>📧 rifa.putriaisya@gmail.com<br>📞 (65)98677022, (62)81314080415</p>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# Gradient color style
gradient_background = "background: linear-gradient(135deg, #000000, #2c2c2c, #5c5c5c);"

# Summary section
summary_box_html = f"""
<div style='
    {gradient_background}
    padding: 20px;
    border-radius: 12px;
    color: white;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.2);
    font-size: 16px;
    line-height: 1.6;
'>
    <ul style='padding-left: 20px;'>
        <li>More than four years of experience in the e-commerce industry, specialising in data analysis, affiliate marketing, and campaign strategy.</li>
        <li>Skilled in translating insights into action through budget management, performance optimisation, cross-functional campaigns, fraud prevention, and product development.</li>
        <li>Sole recipient of ByteDance Individual Spot Award in department for outstanding performance. Recognised as a reliable, collaborative, and data-driven team member with a passion for continuous improvement.</li>
    </ul>
</div>
"""

st.markdown("<div style='font-size: 24px; font-weight: bold; margin-bottom: 10px;'>💡Summary</div>", unsafe_allow_html=True)
st.markdown(summary_box_html, unsafe_allow_html=True)

# Skills section (no box)
st.markdown("<br>", unsafe_allow_html=True) 

skills_html = """
<div style='
    font-size: 16px;
    line-height: 1.6;
'>
    <ul style='padding-left: 20px;'>
        <li><strong>Business & Marketing Skills:</strong> Affiliate marketing, campaign management, budgeting & target setting, data analysis & visualisation, stakeholder management, presentation & communication, team collaboration & leadership</li>
        <li><strong>Technical Skills:</strong> SQL, Python</li>
    </ul>
</div>
"""

st.markdown("<div style='font-size: 24px; font-weight: bold; margin-bottom: 10px;'>🎯 Skills</div>", unsafe_allow_html=True)
st.markdown(skills_html, unsafe_allow_html=True)

# Work Experience section
st.markdown("<br>", unsafe_allow_html=True) 
work_experience_html = """
<div style='font-size: 16px; line-height: 1.6;'>
    <div style='margin-bottom: 20px;'>
        <strong>Shopee – Indonesia</strong><br>
        <em>Senior Associate - Marketing Growth & Strategy</em> | Nov 2024 – Jan 2025
        <ul style='padding-left: 20px; margin-top: 5px;'>
            <li>Acted as campaign lead, managing end-to-end marketing campaigns, including strategy development, budgeting, execution, and performance analysis. Partnered with cross-functional teams to deliver campaign, resulting in an 18% uplift in orders.</li>
            <li>Teamed up with product team to develop new features, streamlining campaign operations and improving efficiency, resulting in a 39% increase in campaign registrations.</li>
        </ul>
    </div>
    </div>
        <strong>ByteDance – Indonesia</strong><br>
        <em>Creator Strategy</em> | Jul 2024 – Nov 2025
        <ul style='padding-left: 20px; margin-top: 5px;'>
            <li>Monitored performance and budget tracking for social commerce programs, delivering data-driven insights and strategic recommendations contributing to a 3 percentage point increase in monthly contribution to overall marketplace’s orders.</li>
            <li>Collaborated with data science and engineering teams to integrate data between Tokopedia and ByteDance, streamlining reporting processes and reducing reliance on manual data requests through a newly developed performance dashboard.</li>
            <li>Defined key success metrics and collaborated with product and business teams to launch and drive early adoption of link-sharing program, enabling TikTok users to share product links outside the platform.</li>
        </ul>
        <em>Affiliate Business Associate (Analysis & Budgeting) - Tokopedia</em> | Dec 2012 – Jul 2024
        <ul style='padding-left: 20px; margin-top: 5px;'>
            <li>Led data operations for affiliate program from its public launch, overseeing performance monitoring, establishing reporting standards, and enhancing data accuracy across systems, contributing to annual order growth and a higher share of overall marketplace transactions.</li>
            <li>Designed monthly and annual performance targets and budgets, achieving approximately 50% cost savings by optimising commission structures in response to business priorities and market dynamics.</li>
            <li>Identified patterns and prevented fraudulent activities by developing fraud detection rules and mechanisms, resulting in cost savings exceeding IDR 4 billion.</li>
            <li>Worked on cross-functional initiatives, including product development and campaign optimisation, contributing to a 15%+ increase in seller-funded commissions to improve sustainability of the program.</li>    
        </ul>
    </div>
"""
st.markdown("<div style='font-size: 24px; font-weight: bold; margin-bottom: 10px;'>💼 Work Experience</div>", unsafe_allow_html=True)
st.markdown(work_experience_html, unsafe_allow_html=True)

# Education section
st.markdown("<br>", unsafe_allow_html=True) 
education_html = """
<div style ='
    font-size: 16px;
    line_height: 1.6;
'>
    <ul style='padding-left: 20px;'>
        <li><strong>MSc in Business Analytics, Nanyang Technological University, Singapore</strong> | Jul, 2025 - Jun, 2026 (expected)</li>
        <li><strong>Bachelor of Communication, Bakrie University, Indonesia</strong> | Jul, 2016 - Feb, 2020</li>
    </ul>
</div>
"""
st.markdown("<div style='font-size: 24px; font-weight: bold; margin-bottom: 10px;'>🎓 Education</div>", unsafe_allow_html=True)
st.markdown(education_html, unsafe_allow_html=True)

# Create LinkedIn button
st.markdown("""
<div style="text-align: center; margin-top: 20px;">
    <a href="https://www.linkedin.com/in/rifaaisyaputri/" target="_blank" 
       style="display: inline-block; padding: 12px 25px; background-color: #0077B5; 
              color: white; border-radius: 30px; text-decoration: none; font-weight: bold;
              box-shadow: 0px 4px 8px rgba(0,0,0,0.2); transition: all 0.3s ease;">
        Let's Connect on LinkedIn 👋🏻
    </a>
</div>
""", unsafe_allow_html=True)

