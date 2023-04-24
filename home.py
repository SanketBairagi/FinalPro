
import streamlit as st
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu
import webbrowser
import streamlit as st
import pandas as pd
import polars as pl
import numpy as np
import pickle
import sklearn
import streamlit.components.v1 as components
from PIL import Image
import pdfkit
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
from datetime import date
from streamlit.components.v1 import iframe
import datetime


st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"}
)





components.html(
"""
<center>
<p>
<img src="https://github.com/SanketBairagi/temp/blob/main/images/logo.png?raw=true" alt="Dr. Logistic's Heart Care System" style="float:left;width:130px;height:130px;">
<br>
<h1 style="font-size:41px">Dr. Logistic's Heart Care System
</h1>
</p>
</center>
<br>

""")


selected = option_menu(None, ["Home", "Dashboard", "Data And Analysis", 'Reports'], 
icons=['house', 'kanban', "book", 'gear'], 
menu_icon="cast", default_index=0, orientation="horizontal")


if selected=="Dashboard":
    st.markdown(
         f"""
         <style>
    .stApp {{
    background: url("https://img.freepik.com/free-vector/clean-medical-background_53876-116875.jpg?w=1380&t=st=1680014506~exp=1680015106~hmac=bbc3e8b1f08ba1a42924044a0dcab2932c5f5331a4d5d8bfd0a7be679f1b285d");background-size: cover
         }}
        </style>
         """,
         unsafe_allow_html=True
     )
    
    components.html(
    """
<iframe title="mydash1" width="1300" height="1200" src="https://app.powerbi.com/view?r=eyJrIjoiNTcwZDg3NjAtMTA2NS00MDQxLTg4MDItYzk3NTE3OTkyZTFmIiwidCI6IjIzNDUyMjY1LTQ0NTItNDE0Zi1iMTIyLTllMjY0ZTU0ZGJiYiJ9" frameborder="0" allowFullScreen="true"></iframe>
       
        """, height=1200)

if selected=="Data And Analysis":
    st.markdown(
         f"""
         <style>
    .stApp {{
    background: url("https://img.freepik.com/free-vector/clean-medical-background_53876-116875.jpg?w=1380&t=st=1680014506~exp=1680015106~hmac=bbc3e8b1f08ba1a42924044a0dcab2932c5f5331a4d5d8bfd0a7be679f1b285d");background-size: cover
         }}
        </style>
         """,
         unsafe_allow_html=True
     )
    st.header("About Dataset")
    st.markdown(""" 
    **2020 annual CDC survey data of 400k adults related to their health status**  \n
    
    **What topic does the dataset cover?** \n
    According to the CDC, heart disease is one of the leading causes of death for people of most races in the US (African Americans, American Indians and Alaska Natives, and white people). About half of all Americans (47%) have at least 1 of 3 key risk factors for heart disease: high blood pressure, high cholesterol, and smoking. Other key indicator include diabetic status, obesity (high BMI), not getting enough physical activity or drinking too much alcohol. Detecting and preventing the factors that have the greatest impact on heart disease is very important in healthcare. Computational developments, in turn, allow the application of machine learning methods to detect "patterns" from the data that can predict a patient's condition.

    
    **Where did the dataset come from and what treatments did it undergo?** \n
    Originally, the dataset come from the CDC and is a major part of the Behavioral Risk Factor Surveillance System (BRFSS), which conducts annual telephone surveys to gather data on the health status of U.S. residents. As the CDC describes: "Established in 1984 with 15 states, BRFSS now collects data in all 50 states as well as the District of Columbia and three U.S. territories. BRFSS completes more than 400,000 adult interviews each year, making it the largest continuously conducted health survey system in the world.". The most recent dataset (as of February 15, 2022) includes data from 2020. It consists of 401,958 rows and 279 columns. The vast majority of columns are questions asked to respondents about their health status, such as "Do you have serious difficulty walking or climbing stairs?" or "Have you smoked at least 100 cigarettes in your entire life? [Note: 5 packs = 100 cigarettes]". In this dataset, I noticed many different factors (questions) that directly or indirectly influence heart disease, so I decided to select the most relevant variables from it and do some cleaning so that it would be usable for machine learning projects.
    

    **What can you do with this dataset?** \n
    As described above, the original dataset of nearly 300 variables was reduced to just about 20 variables. In addition to classical EDA, this dataset can be used to apply a range of machine learning methods, most notably classifier models (logistic regression, SVM, random forest, etc.). You should treat the variable "HeartDisease" as a binary ("Yes" - respondent had heart disease; "No" - respondent had no heart disease). But note that classes are not balanced, so the classic model application approach is not advisable. Fixing the weights/undersampling should yield significantly betters results. Based on the dataset, I constructed a logistic regression model and embedded it in an application you might be inspired by: https://sanketbairagi-final-project-home-mg4j3l.streamlit.app/. 
    """)

    df=pd.read_csv("https://raw.githubusercontent.com/SanketBairagi/final_project/main/heart_2020_cleaned.csv")
    st.dataframe(df)
    st.markdown(""" [Download Dataset](https://www.kaggle.com/datasets/kamilpytlak/personal-key-indicators-of-heart-disease?datasetId=1936563) """)

if selected=="Reports":
    st.markdown(
         f"""
         <style>
    .stApp {{
    background: url("https://img.freepik.com/free-vector/clean-medical-background_53876-116875.jpg?w=1380&t=st=1680014506~exp=1680015106~hmac=bbc3e8b1f08ba1a42924044a0dcab2932c5f5331a4d5d8bfd0a7be679f1b285d");background-size: cover
         }}
        </style>
         """,
         unsafe_allow_html=True
     )
     
    st.header("will Update Soon.................")
    
    

if selected=="Home":
    st.markdown(f"""
    <style>
    .stApp {{
    background: url("https://img.freepik.com/free-vector/clean-medical-background_53876-116875.jpg?w=1380&t=st=1680014506~exp=1680015106~hmac=bbc3e8b1f08ba1a42924044a0dcab2932c5f5331a4d5d8bfd0a7be679f1b285d");background-size: cover
         }}
        </style>
         """,
        unsafe_allow_html=True
    )
    st.markdown("<h1 style='text-align: center; color: black;'>Heart Disease Prediction</h1>", unsafe_allow_html=True)
    st.subheader("Are you wondering about the condition of your heart? This app will help you to diagnose it!")
    
    col1, col2 = st.columns([3, 1])
    with col2:
        st.image("https://github.com/SanketBairagi/final_project/blob/main/images/mainwindowdoc.jpg?raw=true",
        caption="I'll help you diagnose your heart health! - Dr. Logistic",
        width=190)
        
    with col1:
        st.markdown("""
        **Did you know that machine learning models can help you
        predict heart disease pretty accurately? In this app, you can
        estimate your chance of heart disease (yes/no) in seconds!**
        
        **Here, a logistic regression model using an undersampling technique
        was constructed using survey data of over 300k US residents from the year 2020.
        This application is based on it because it has proven to be better than the random forest
        (it achieves an accuracy of about 80%, which is quite good).**
        
        **To predict your heart disease status, simply follow the steps bellow:**  
        1. Enter the parameters that best describe you;  
        2. Press the "Predict" button and wait for the result.
            
        **Keep in mind that this results is not equivalent to a medical diagnosis!
        This model would never be adopted by health care facilities because of its less
        than perfect accuracy, so if you have any problems, consult a human doctor.**
        
        
        You can see the steps of building the model, evaluating it, and cleaning the data itself
        on my GitHub repo [here](https://github.com/SanketBairagi/final_project.git). 
        """)
    
    c1,c2,c3=st.columns([1,6,1])
    with c2:
        st.markdown("<h2 style='text-align: center; color: black;'>Fill The Following Form To Predict Your Health</h2>", unsafe_allow_html=True)
    
        env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())
        template = env.get_template("template.html")    

        model = pickle.load(open('model/heart5.sav','rb'))

        


        with st.form(key="My form",clear_on_submit=True):
            Name =st.text_input("Enter Your Name", "Type Here ...")
            coll1, coll2,coll3 = st.columns(3,gap="small")
            with coll1:
                birth = st.date_input("Select Your Birth Date",
                        value = datetime.date(2000, 6, 12),
                        min_value = datetime.date(1950, 1, 1),
                        max_value = datetime.date(2010, 12, 31)
                        )
                birth=str(birth)
            with coll2:    
                Adds =st.text_input("Enter Your City", "Type Here ...")
            with coll3:    
                ph =st.text_input("Enter Your Phone Number", "Type Here ...")

            col1, col2 = st.columns(2,gap="small")
            with col1:
                race = st.selectbox("Race",options=('White', 'Black', 'Asian', 'American Indian/Alaskan Native','Other', 'Hispanic'))
            with col2:  
                sex = st.selectbox("Sex", options=('Female', 'Male'))

            with col1:    
                age_cat = st.selectbox("Age category",options=('18-24','25-29','30-34','35-39','40-44','45-49','50-54','55-59','60-64','65-69','70-74','75-79','80 or older'))
            with col2:
                bmi_cat = st.selectbox("BMI category",options=('Under_weight', 'Normal_weight', 'Over_weight', 'Obese','Extremly_Obese'))
            
            with col1: 
                sleep_time = st.number_input("How Many Hours On Average Do You Sleep?", 0, 24, 7)
            with col2: 
                gen_health = st.selectbox("How Can You Define Your General Health?",options=('Very good', 'Fair', 'Good', 'Poor', 'Excellent'))
            
            with col1:
                phys_health = st.number_input("For How Many Days During The Past 30 Days"
                                        " Your Physical Health Not Good?", 0, 30, 0)
            with col2:
                ment_health = st.number_input("For How Many Days During The Past 30 Days"
                                        " Your Mental Health Not Good?", 0, 30, 0)
            phys_act = st.selectbox("Have You Played Any Sports (running, biking, etc.)"
                                    " In The Past Month?", options=("No", "Yes"))
            smoking = st.selectbox("Have You Smoked At Least 100 Cigarettes In"
                                    " Your Entire Life (approx. 5 packs)?)",
                                    options=("No", "Yes"))
            alcohol_drink = st.selectbox("Do You Have More Than 14 Drinks Of Alcohol (men)"
                                            " Or More Than 7 (women) In A Week?", options=("No", "Yes"))
            

            colls1, colls2,colls3 = st.columns(3,gap="small")
            with colls1:
                stroke = st.selectbox("Did You Have A Stroke?", options=("No", "Yes"))
            with colls2:
                diff_walk = st.selectbox("Do You Face Difficulty Walking"
                                    " Or Climbing Stairs?", options=("No", "Yes"))
            with colls3:
                diabetic = st.selectbox("Have You Ever Had Diabetes?",
                                    options=('Yes', 'No', 'No, borderline diabetes', 'Yes (during pregnancy)'))
            
            with colls1:
                asthma = st.selectbox("Do You Have Asthma?", options=("No", "Yes"))
            with colls2:
                kid_dis = st.selectbox("Do You Have Kidney Disease?", options=("No", "Yes"))
            with colls3:
                skin_canc = st.selectbox("Do You Have Kkin Cancer?", options=("No", "Yes"))
        
    
            submit = st.form_submit_button("Predict")


        if smoking == "Yes":
            Smoking = 1
        else:
            Smoking = 0

        if alcohol_drink == "Yes":
            AlcoholDrinking = 1
        else:
            AlcoholDrinking = 0    

        if stroke == "Yes":
            Stroke = 1
        else:
            Stroke = 0 

        if stroke == "Yes":
            Stroke = 1
        else:
            Stroke = 0 


        PhysicalHealth= phys_health
        MentalHealth= ment_health


        if diff_walk == "Yes":
            DiffWalking = 1
        else:
            DiffWalking = 0 


        if phys_act == "Yes":
            PhysicalActivity = 1
        else:
            PhysicalActivity = 0 

        if asthma == "Yes":
            Asthma = 1
        else:
            Asthma = 0 

        if kid_dis == "Yes":
            KidneyDisease = 1
        else:
            KidneyDisease = 0 


        if skin_canc == "Yes":
            SkinCancer = 1
        else:
            SkinCancer = 0 

        if sex == "Female":
            Sex = 0
        else:
            Sex = 1 


        if gen_health == "Poor":
            GenHealth = 0
        elif gen_health == "Fair":
            GenHealth = 1
        elif gen_health == "Good":
            GenHealth = 2
        elif gen_health == "Very good":
            GenHealth = 3
        else :
            GenHealth = 4


        if diabetic == "No":
            Diabetic = 0
        elif diabetic == "No, borderline diabetes":
            Diabetic = 1
        elif diabetic == "Yes (during pregnancy)":
            Diabetic = 2
        else :
            Diabetic = 3


        if race == "White":
            Race = 0
        elif race == "Black":
            Race = 1
        elif gen_health == "Asian":
            Race = 2
        elif race == "American Indian/Alaskan Native":
            Race = 3
        elif gen_health == "Other":
            Race = 4   
        else :
            Race = 5




        if age_cat == "18-24":
            AgeCategory = 0
        elif age_cat == "25-29":
            AgeCategory = 1
        elif age_cat == "30-34":
            AgeCategory = 2
        elif age_cat == "35-39":
            AgeCategory = 3
        elif age_cat == "40-44":
            AgeCategory = 4 
        elif age_cat == "45-49":
            AgeCategory = 5
        elif age_cat == "50-54":
            AgeCategory = 6
        elif age_cat == "55-59":
            AgeCategory = 7
        elif age_cat == "60-64":
            AgeCategory = 8        
        elif age_cat == "65-69":
            AgeCategory = 9
        elif age_cat == "70-74":
            AgeCategory = 10 
        elif age_cat == "75-79":
            AgeCategory = 11
        else :
            AgeCategory = 12



        SleepTime= sleep_time

        if bmi_cat == "Under_weight":
            BMICategory = 0
        elif bmi_cat == "Normal_weight":
            BMICategory = 1
        elif bmi_cat == "Over_weight":
            BMICategory = 2
        elif bmi_cat == "Obese":
            BMICategory = 3
        else :
            BMICategory = 4  





        p=[[Smoking,AlcoholDrinking,Stroke,float(PhysicalHealth),
        float(MentalHealth),DiffWalking,Sex,AgeCategory,Race,Diabetic,
        PhysicalActivity,GenHealth,float(SleepTime),Asthma,KidneyDisease,
        SkinCancer,BMICategory]]





        if submit:
            prediction = model.predict(p)
            prediction_prob = model.predict_proba(p)
            if prediction == 0:
                st.success(f""" 
                    * Name : {Name}
                    * D.O.B : {birth}
                    * Race : {race}
                    * Sex : {sex}
                    * Age category : {age_cat}
                    * BMI category : {bmi_cat}
                    * Average Sleep Hrs. : {sleep_time}
                    * General Health : {gen_health}
                    * Physical Health Not Good In Days : {phys_health}
                    * Mental Health Not Good In Days : {phys_health}
                    * Physical Activity : {phys_act}
                    * Smokking : {smoking}
                    * Drinking of Alcohol : {alcohol_drink}
                    * Strock : {stroke}
                    * Difficulty Walking Or Climbing Stairs : {diff_walk}
                    * Diabetes : {diabetic}
                    * Asthma : {asthma}
                    * Kidney Disease : {kid_dis}
                    * Skin Cancer : {skin_canc}

                    """)
                st.success(f"**Hey {Name} "f"The probability that you'll have"f" heart disease is {round(prediction_prob[0][1] * 100, 2)}%."f" You are healthy!**")
    
                prob=round(prediction_prob[0][1] * 100, 2)
                html = template.render(Name=Name,Sex=sex,date=date.today().strftime("%B %d, %Y"),birth =birth,Adds=Adds,ph=ph,race=race,
                                        sex=sex,age_cat=age_cat,bmi_cat=bmi_cat,sleep_time=sleep_time,gen_health=gen_health,phys_health=phys_health
                                        ,phys_act=phys_act,smoking=smoking,alcohol_drink=alcohol_drink,stroke=stroke,ment_health=ment_health,
                                        diff_walk=diff_walk,diabetic=diabetic,asthma=asthma,kid_dis=kid_dis,skin_canc=skin_canc,prob=prob,)
                pdf = pdfkit.from_string(html)
    
                st.download_button(
                "Download Report",
                data=pdf,
                file_name="report.pdf",
                mime="application/octet-stream",)
    
            else:
                st.warning(f""" 
                * Name : {Name}
                * Race : {race}
                * Sex : {sex}
                * Age category : {age_cat}
                * BMI category : {bmi_cat}
                * Average Sleep Hrs. : {sleep_time}
                * General Health : {gen_health}
                * Physical Health Not Good In Days : {phys_health}
                * Mental Health Not Good In Days : {ment_health}
                * Physical Activity : {phys_act}
                * Smokking : {smoking}
                * Drinking of Alcohol : {alcohol_drink}
                * Strock : {stroke}
                * Difficulty Walking Or Climbing Stairs : {diff_walk}
                * Diabetes : {diabetic}
                * Asthma : {asthma}
                * Kidney Disease : {kid_dis}
                * Skin Cancer : {skin_canc}
                """)
                st.warning(f"**Hey {Name} "f"The probability that you will have"f" heart disease is {round(prediction_prob[0][1] * 100, 2)}%."f" It sounds like you are not healthy.**")
    
                prob=round(prediction_prob[0][1] * 100, 2)
                html = template.render(Name=Name,Sex=sex,date=date.today().strftime("%B %d, %Y"),birth =birth,Adds=Adds,ph=ph,race=race,
                                        sex=sex,age_cat=age_cat,bmi_cat=bmi_cat,sleep_time=sleep_time,gen_health=gen_health,phys_health=phys_health
                                        ,phys_act=phys_act,smoking=smoking,alcohol_drink=alcohol_drink,stroke=stroke,ment_health=ment_health,
                                        diff_walk=diff_walk,diabetic=diabetic,asthma=asthma,kid_dis=kid_dis,skin_canc=skin_canc,prob=prob,)
                pdf = pdfkit.from_string(html)
    
                st.download_button(
                "Download Report",
                data=pdf,
                file_name="report.pdf",
                mime="application/octet-stream",)

    


            
