import streamlit as st
from PIL import Image
from sqlalchemy import create_engine


st.set_page_config(
        page_title="Portfolio",
        page_icon="",

    )
with st.sidebar :
    #st.write("portfolio")
    img = Image.open("WhatsApp.jpeg")
    img_resized = img.resize((500, 500))
    st.image( img_resized,  channels="RGB" )
     
    if st.button("Email"):    
     st.write("nambu935@gmail.com")
            
    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")    
    with open("Nambu_Keerthi_Data_Scientist (4).pdf", "rb") as file:
        pdf_data = file.read()    
    st.download_button(
     label="Resume",
     data=pdf_data,
     file_name="Nambu_Keerthi_Data_Scientist.pdf", 
     mime="application/pdf",        
        )     
    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")    
    st.link_button("Git Hub", "https://github.com/Nambukeerthi")
    st.markdown(" ")
    st.markdown(" ")    
    st.markdown(" ")
    st.link_button("linked in", "https://www.linkedin.com/in/keerthi-r-9b8839283/")


st.header("NAMBU KEERTHI R")

st.subheader(":blue[Data Scientist]")
st.markdown("I am a Data Science fresher aiming to leverage my robust programming skills, analytical aptitude, and proficiency in data visualizations to effectively analyze, interpret, and present insights from extensive datasets accurately and meaningfully") 
st.markdown(" ")

st.markdown(
    "<hr style='border: 3px solid skyblue; margin: 10px 0;'>",
    unsafe_allow_html=True
)

st.markdown(" ")

st.subheader("SKILLS")
st.markdown(
"""
:computer: :blue-background[Technologies] - *Python, Streamlit, EDA, API integration, VBA, Github*  

:books: :blue-background[Libraries] - *Numpy, Pandas, Skikit-learn, Matplotlib, Seaborn, SQLAlchemy, Boto3*

:triangular_ruler: :blue-background[ML Models] - *Regression, Decision tree, Random Forest*

:file_cabinet: :blue-background[Databases] - *MySQL, PostrageSQL, MangoDB, AWS RDS*

:chart_with_upwards_trend: :blue-background[Data Visualization] - *Statistics, Power BI, MS Excel, Plotly*

:sun_behind_cloud: :blue-background[Cloud] - *AWS*       """)

st.markdown(" ")
st.markdown(" ")   


st.markdown(
    "<hr style='border: 3px solid skyblue; margin: 10px 0;'>",
    unsafe_allow_html=True
)

