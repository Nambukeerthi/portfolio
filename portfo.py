import streamlit as st
from PIL import Image
from sqlalchemy import create_engine


st.set_page_config(
        page_title="Portfolio",
        page_icon="",

    )

col1, col2 = st.columns(2)

with col1:
    #st.write("portfolio")
    img = Image.open("DSC_0226.jpg")
    img_resized = img.resize((300, 400))
    st.image( img_resized,  channels="RGB" )
    
with col2:
   
   st.header("NAMBU KEERTHI R")
   st.subheader("Data Scientist")
   #st.write("I have completed my Master Data Science course in guvi. ")
   st.markdown("I am a motivated Data Science fresher aiming to leverage my robust programming skills, analytical aptitude, and proficiency in data visualizations to effectively analyze, interpret, and present insights from extensive datasets accurately and meaningfully") 
   st.write("nambu935@gmail.com")
col1, col2,col3 = st.columns(3)
with col1: 
    with open("Nambu_Keerthi_Resume.pdf", "rb") as file:
        pdf_data = file.read()    
    st.download_button(
     label="Resume",
     data=pdf_data,
     file_name="Nambu_Keerthi_Resume.pdf", 
     mime="application/pdf",
        )     
   #st.button("Resume", type="secondary")
with col2:
   st.link_button("Git Hub", "https://github.com/Nambukeerthi")
   
with col3:
   st.link_button("linked in", "https://www.linkedin.com/in/keerthi-r-9b8839283/")        

st.subheader("Skills")
st.markdown(
    """
    :computer: Technologies - *Python, Streamlit, EDA, API integration, VBA, Github*  

    :books: Libraries - *Numpy, Pandas, Skikit-learn, Matplotlib, Seaborn, SQLAlchemy, Boto3*
    
    :triangular_ruler: ML Models - *Regression, Decision tree, Random Forest*
    
    :file_cabinet: Databases - *MySQL, PostrageSQL, MangoDB, AWS RDS*

    :chart_with_upwards_trend: Data Visualization - *Statistics, Power BI, MS Excel, Plotly*
    
    :sun_behind_cloud: Cloud - *AWS* 
    
    """
)
st.subheader("Projects")
st.markdown(
    """
    1. [YouTube Data Harvesting and Warehousing](https://youtubedataproject-mkjagva9qhyswv8gukrxaq.streamlit.app/)

         This Project that enables users to access, analyze, and visualize data from multiple YouTube channels.
         
             - Data harvesting from YouTube.
             - SQL integration for efficient data warehousing.
             - Interactive data exploration and analysis through Streamlit.
    
    2. [Phonepe Pulse Data Visualization and Exploration](https://phonepeproject-np7vzyrwmrqn9jhyn94teg.streamlit.app/)

         A user-friendly tool to visualize and analyze metrics from the PhonePe Pulse GitHub repository.
         
             - Data extraction and preprocessing.
             - Insight generation through visualizations.
             - Interactive visualizations with Streamlit and Plotly.
             
    
    3. [Airbnb Analysis](https://airbnbproject-5gd42oftn3vyehwyha8ohd.streamlit.app/)

         Comprehensive Analysis of Airbnb data using MongoDB Atlas and geospatial visualizations.
         
              - Data cleaning and preparation.
              - Interactive geospatial visualizations.
              - Insights into pricing variations, availability, and location-based trends.
              
              
    4. [Industrial Copper Model](https://copperproject-wlksjkfyhnyhhbnsyhkued.streamlit.app/)
    
           A Machine Learning Regression model for sales and pricing analysis in the Copper Industry.

              - Handling skewness and noisy data through normalization and outlier detection.
              - Improved pricing predictions using robust machine learning techniques.
              - Automated decision-making for optimal pricing strategies.
              
    
    5.  [Singapore Resale Flat Prices Prediction](https://flatpriceproject-brmudwq4p4ebhtwzrg6lkc.streamlit.app/)

         A predictive Machine Learning model for estimating Resale Flat prices in Singapore, deployed as a web application.

              - Historical transaction data analysis.
              - User-friendly web app for buyers and sellers.
              - Accurate price estimation to assist in decision-making.

    
    """
)

st.write("check out this [link](https://share.streamlit.io/mesmith027/streamlit_webapps/main/MC_pi/streamlit_app.py)")
