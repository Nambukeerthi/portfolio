import streamlit as st
from PIL import Image
from sqlalchemy import create_engine


st.set_page_config(
        page_title="Portfolio",
        page_icon="",
         )

with st.sidebar :
    #st.write("portfolio")
    img = Image.open("images/WhatsApp.jpeg")
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
    st.link_button("GitHub", "https://github.com/Nambukeerthi")
    st.markdown(" ")
    st.markdown(" ")    
    st.markdown(" ")
    st.link_button("linkedin", "https://www.linkedin.com/in/keerthi-r-9b8839283/")



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
st.markdown(" ")    


st.subheader("PROJECTS")

col1, col2 = st.columns(2)
with col1:
        st.markdown("**1. YouTube Data Harvesting and Warehousing**")
        img = Image.open("images/youtube_project.jpeg")
        img_resized = img.resize((300, 300))
        st.image( img_resized,  channels="RGB" )
with col2:
        st.markdown(
            """
              [YouTube Data Harvesting and Warehousing](https://youtubedataproject-mkjagva9qhyswv8gukrxaq.streamlit.app/)
        
                 This Project that enables users to access, analyze, and visualize data from multiple YouTube channels.
                 
                 :small_blue_diamond: Data harvesting from YouTube.
                 
                 :small_blue_diamond: SQL integration for efficient data warehousing.
                 
                 :small_blue_diamond: Interactive data exploration and analysis through Streamlit. """)
 
st.markdown(" ")
st.markdown(" ") 
col3, col4 = st.columns(2)
with col3:
        st.markdown("**2. Phonepe Pulse Data Visualization and Exploration**")
        img = Image.open("images/phonpe.jpeg")
        img_resized = img.resize((300, 200))
        st.image( img_resized,  channels="RGB" )
with col4:
        st.markdown(
            """
              [Phonepe Pulse Data Visualization and Exploration](https://phonepeproject-np7vzyrwmrqn9jhyn94teg.streamlit.app/)

                 A user-friendly tool to visualize and analyze metrics from the PhonePe Pulse GitHub repository.
                 
                 :small_blue_diamond: Data extraction and preprocessing.
                 
                 :small_blue_diamond: Insight generation through visualizations.
                 
                 :small_blue_diamond: Interactive visualizations with Streamlit and Plotly. """)

st.markdown(" ")
st.markdown(" ") 
col5, col6 = st.columns(2)
with col5:
        st.markdown("**3. Airbnb Analysis**")
        img = Image.open("images/airbnb600.jpeg")
        img_resized = img.resize((300, 200))
        st.image( img_resized,  channels="RGB" )
with col6:
        st.markdown(
            """
              [Airbnb Analysis](https://airbnbproject-5gd42oftn3vyehwyha8ohd.streamlit.app/)

                 Comprehensive Analysis of Airbnb data using MongoDB Atlas and geospatial visualizations.
                 
                 :small_blue_diamond: Data cleaning and preparation.
                 
                 :small_blue_diamond: Interactive geospatial visualizations.
                 
                 :small_blue_diamond: Insights into pricing variations, availability, and location-based trends. """)

st.markdown(" ")
st.markdown(" ") 
col7, col8 = st.columns(2)
with col7:
        st.markdown("**4. Industrial Copper Model**")
        img = Image.open("images/copper-wire-1.jpg")
        img_resized = img.resize((300, 200))
        st.image( img_resized,  channels="RGB" )
with col8:
        st.markdown(
            """
              [Industrial Copper Model](https://copperproject-wlksjkfyhnyhhbnsyhkued.streamlit.app/)
    
                 A Machine Learning Regression model for sales and pricing analysis in the Copper Industry.
        
                 :small_blue_diamond: Handling skewness and noisy data through normalization and outlier detection.
                 
                 :small_blue_diamond: Improved pricing predictions using robust machine learning techniques.
                 
                 :small_blue_diamond: Automated decision-making for optimal pricing strategies. """)


st.markdown(" ")
st.markdown(" ") 
col9, col10 = st.columns(2)
with col9:
        st.markdown("**4. Singapore Resale Flat Prices Prediction**")
        img = Image.open("images/flat_pic.jpg")
        img_resized = img.resize((300, 200))
        st.image( img_resized,  channels="RGB" )
with col10:
        st.markdown(
            """
              [Singapore Resale Flat Prices Prediction](https://flatpriceproject-jripvgug8b43r2dwz8d2ta.streamlit.app/)

                 A predictive Machine Learning model for estimating Resale Flat prices in Singapore, deployed as a web application.
        
                 :small_blue_diamond: Historical transaction data analysis.
                 
                 :small_blue_diamond: User-friendly web app for buyers and sellers.
                 
                 :small_blue_diamond: Accurate price estimation to assist in decision-making. """)

