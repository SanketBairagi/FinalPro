
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

<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
* {box-sizing: border-box;}

body {
  font-family: Helvetica;
  margin: 0;
}

}
.site-header { 
  
  padding: 1.5em 1em;
}

.site-header::after {
  content: "";
  clear: both;
}

.site-identity {
  float: Center;
}

.site-identity h1 {
  font-size: 44px;
  margin: 1.2em 0 .3em 0;
  display: inline-block;
}

.site-identity img {
  max-width: 155px;
  float: left;
  margin: 0 10px 0 0;
}


</style>
</head>
<body>
<center>
<header class="site-header">
  <div class="site-identity">
    <a href="#"><img src="https://github.com/SanketBairagi/FinalPro/blob/main/images/dr%20logistic's%20logo.png?raw=true" /></a>
    <h1><a>Dr. Logistic's Heart Care</a></h1>
  </div>  
</header>
</center>
</body>
</html>



""")





selected = option_menu(None, ["Home", "Dashboard"], 
icons=['house', 'kanban'], 
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
<iframe title="Report Section" width="1300" height="750" src="https://app.powerbi.com/view?r=eyJrIjoiMDY0YzQ3NTMtODIyMy00YWY1LThmODYtM2RlNWMzYTYxZWI3IiwidCI6IjIzNDUyMjY1LTQ0NTItNDE0Zi1iMTIyLTllMjY0ZTU0ZGJiYiJ9" frameborder="0" allowFullScreen="true"></iframe>        
    """, height=780)

    st.header("Our Analysis On Data")
    st.markdown("""
    * In our sample, around 8 among 100 individuals suffer from heart disease.
    * The BMI of heart disease patients is slightly higher than that of healthy individuals.
    * The older the individual, the more susceptible they are to heart disease.
    * ~10% of males suffer from heart disease, while only ~7% of females do.
    * The pecentage of heart disease is highest (> 10%) among Native americans, followed by whites (~9%). The least percentage of heart disease (~3%) is among asians.
    * A lot more people who suffer from heart disease say they have poor or fair health compared to those who don't.
    * 79% of healthy individuals have been physically active in the past 30 days, compared to 64% in heart disease patients.
    *Abnormal sleeep duration is more prevalent in heart disease patients. Even though heart disease patients make 8.5% of the sample, they have higher percentages of sleep less than 6 hours or more than 9 hours, which is considered abnormal.
    * ~12% of people who smoke suffer from heart disease. In contrast, ~5% of non-smokers suffer from heart disease.
    * Surprisingly, people who drink alcohol have a lower percentage of heart disease (~4%) than those who do not (~9%).
    * Having a stroke is highly correlacted with heart disease. People who have had a stroke before have a heart disease percentage of around 48%. On the other hand, people who did not suffer a stroke had a significantly lower percentage of heart disease (~8%).
    * Diabetic people are at higher risk of heart disease (~25%).
    * Asthmatic people are at a slightly higher risk of heart disease.
    * Those who have suffered from kidney disease are at a sginificantly higher risk of heart disease. With a percentage of ~30% compared to ~9% in healthy people.
    * People who suffered from skin cancer are at a moderately higher risk of heart disease (~18% vs ~9%).
    * Difficilty of walking is present in ~18% of heart disease patients vs ~7% in healthy individuals.
    * The BMI distribution differs slightly in patients of different diseases. With diabetic people having the highest BMI mode, and stroke victims having the lowest BMI mode.
    * Mental health, sleep duration, and physical health are similar among people who suffer from different dieseases.
    * ~64% of people who say they have poor health are smokers. While people who say they have excellent health are 30% smokers.
    """)
    
    

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
    st.markdown("<h1 style='text-align: center; color: black;'>Heart Health Checkup</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: black;'>THE BEST WAY TO FIGHT A DISEASE IS TO PREVENT IT.", unsafe_allow_html=True)
    st.subheader("Are you wondering about the condition of your heart? This app will help you to diagnose it!")
    
        
    
    st.markdown("""
        **In this app, you can estimate your chance of heart disease (yes/no) in seconds!**
        
        **To predict your heart disease status, simply follow the steps bellow:**  
        1. Enter the parameters that best describe you;  
        2. Press the "Predict" button and wait for the result.
            
        **Keep in mind that this results is not equivalent to a medical diagnosis!
        This model would never be adopted by health care facilities because of its less
        than perfect accuracy, so if you have any problems, consult a human doctor.**
         
        """)
    
    c1,c2,c3=st.columns([1,6,1])
    with c2:
        st.markdown("<h2 style='text-align: center; color: black;'>Fill The Following Form To Check Your Heart Health</h2>", unsafe_allow_html=True)
    
        env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())
        template = env.get_template("template.html")    

        model = pickle.load(open('model/4may.sav','rb'))

        


        with st.form(key="My form",clear_on_submit=True):
            Name =st.text_input("Enter Your Name", "")
            coll1, coll2,coll3 = st.columns(3,gap="small")
            with coll1:
                birth = st.date_input("Select Your Birth Date",
                        value = datetime.date(2000, 6, 12),
                        min_value = datetime.date(1950, 1, 1),
                        max_value = datetime.date(2010, 12, 31)
                        )
                birth=str(birth)
            with coll2:    
                Adds =st.text_input("Enter Your City","")
            with coll3:    
                ph =st.text_input("Enter Your Phone Number","")

            col1, col2 = st.columns(2,gap="small")
           
             
            sex = st.selectbox("Sex", options=('Female', 'Male'))

            with col1:    
                age_cat = st.selectbox("Age category",options=('18-24','25-29','30-34','35-39','40-44','45-49','50-54','55-59','60-64','65-69','70-74','75-79','80 or older'))
            with col2:
                bmi_cat = st.selectbox("BMI category",options=('Under_weight', 'Normal_weight', 'Over_weight', 'Obese'))
            
            with col1: 
                sleep_time = st.number_input("How Many Hours On Average Do You Sleep?", 4,10,6)
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


        PhysicalHealth= ((phys_health-0)/(30-0))
        
        MentalHealth= ((ment_health-0)/(30-0))


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
            GenHealthx = 0
        elif gen_health == "Fair":
            GenHealthx = 1
        elif gen_health == "Good":
            GenHealthx = 2
        elif gen_health == "Very good":
            GenHealthx = 3
        else :
            GenHealthx = 4

        GenHealth=((GenHealthx-0)/(4-0))

        if diabetic == "No":
            Diabeticx = 0
        elif diabetic == "No, borderline diabetes":
            Diabeticx = 1
        elif diabetic == "Yes (during pregnancy)":
            Diabeticx = 2
        else :
            Diabeticx = 3

        Diabetic=((Diabeticx-0)/(3-0))




        if age_cat == "18-24":
            AgeCategoryx = 0
        elif age_cat == "25-29":
            AgeCategoryx = 1
        elif age_cat == "30-34":
            AgeCategoryx = 2
        elif age_cat == "35-39":
            AgeCategoryx = 3
        elif age_cat == "40-44":
            AgeCategoryx = 4 
        elif age_cat == "45-49":
            AgeCategoryx = 5
        elif age_cat == "50-54":
            AgeCategoryx = 6
        elif age_cat == "55-59":
            AgeCategoryx = 7
        elif age_cat == "60-64":
            AgeCategoryx = 8        
        elif age_cat == "65-69":
            AgeCategoryx = 9
        elif age_cat == "70-74":
            AgeCategoryx = 10 
        elif age_cat == "75-79":
            AgeCategoryx = 11
        else :
            AgeCategoryx = 12

        AgeCategory=((AgeCategoryx-0)/(12-0))

        SleepTime= ((sleep_time-4)/(10-4))

        if bmi_cat == "Under_weight":
            BMICategoryx = 0
        elif bmi_cat == "Normal_weight":
            BMICategoryx = 1
        elif bmi_cat == "Over_weight":
            BMICategoryx = 2
        else :
            BMICategoryx = 3  


        BMICategory=((BMICategoryx-0)/(3-0))


        p=[[Smoking,AlcoholDrinking,Stroke,float(PhysicalHealth),
        float(MentalHealth),DiffWalking,Sex,AgeCategory,Diabetic,
        PhysicalActivity,GenHealth,float(SleepTime),Asthma,KidneyDisease,
        SkinCancer,BMICategory]]





        if submit:
            prediction = model.predict(p)
            prediction_prob = model.predict_proba(p)
            if prediction == 0:
                st.success(f""" 
                    * Name : {Name}
                    * D.O.B : {birth}
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
                html = template.render(Name=Name,Sex=sex,date=date.today().strftime("%B %d, %Y"),birth =birth,Adds=Adds,ph=ph,
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
                html = template.render(Name=Name,Sex=sex,date=date.today().strftime("%B %d, %Y"),birth =birth,Adds=Adds,ph=ph,
                                        sex=sex,age_cat=age_cat,bmi_cat=bmi_cat,sleep_time=sleep_time,gen_health=gen_health,phys_health=phys_health
                                        ,phys_act=phys_act,smoking=smoking,alcohol_drink=alcohol_drink,stroke=stroke,ment_health=ment_health,
                                        diff_walk=diff_walk,diabetic=diabetic,asthma=asthma,kid_dis=kid_dis,skin_canc=skin_canc,prob=prob,)
                pdf = pdfkit.from_string(html)
    
                st.download_button(
                "Download Report",
                data=pdf,
                file_name="report.pdf",
                mime="application/octet-stream",)

    


            
