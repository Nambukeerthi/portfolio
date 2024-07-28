import streamlit as st
from tkinter import YES
from PIL import Image
from sqlalchemy import create_engine
import tkinter

st.set_page_config(
        page_title="Portfolio",
        page_icon="",

    )

col1, col2 = st.columns(2)

with col1:
    #st.write("portfolio")
    img = Image.open("logo.jpg")
    st.image( img, use_column_width=True,channels="RGB" )
    
with col2:
   
   st.header("NAMBU KEERTHI R")
   st.subheader("Data Scienctist")
#st.write("I have completed my Master Data Science course in guvi. ")
   st.markdown("I am a motivated Data Science fresher aiming to leverage my robust programming skills, analytical aptitude, and proficiency in data visualizations to effectively analyze, interpret, and present insights from extensive datasets accurately and meaningfully") 
   st.write("nambu935@gmail.com")
col1, col2,col3 = st.columns(3)
with col1:
  st.button("Resume", type="secondary")
with col2:
   st.link_button("Git Hub", "https://github.com/Nambukeerthi")
   
with col3:
   st.link_button("linked in", "https://www.linkedin.com/in/keerthi-r-9b8839283/")        

st.subheader("Skils")
st.markdown(
    """
    :computer: Programming Skils - *Python (Numpy,Pandas,Skikit-learn), SQL, VBA*                 
    
    :chart_with_upwards_trend: Data Visualization - *Statistics, Power BI, MS Excel, Plotly*
    
    :books: Models - *Regression, Decision tree, Random Forest*
    
    :file_cabinet: Databases - *MySQL, PostrageSQL, MangoDB*
    
    :sun_behind_cloud: Cloud - *AWS* 
    
    """
)
