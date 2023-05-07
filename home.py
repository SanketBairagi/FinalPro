
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





selected = option_menu(None, ["Home", "Dashboard", "Data And Analysis", 'Health tips'], 
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
<iframe title="Report Section" width="1300" height="750" src="https://app.powerbi.com/view?r=eyJrIjoiMDY0YzQ3NTMtODIyMy00YWY1LThmODYtM2RlNWMzYTYxZWI3IiwidCI6IjIzNDUyMjY1LTQ0NTItNDE0Zi1iMTIyLTllMjY0ZTU0ZGJiYiJ9" frameborder="0" allowFullScreen="true"></iframe>        """, height=1200)

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
    **2020 annual CDC survey data of 400k adults related to their health status** \n \n
    [Download Dataset](https://www.kaggle.com/datasets/kamilpytlak/personal-key-indicators-of-heart-disease?datasetId=1936563) \n
    **What topic does the dataset cover?** \n
    According to the CDC, heart disease is one of the leading causes of death for people of most races in the US (African Americans, American Indians and Alaska Natives, and white people). About half of all Americans (47%) have at least 1 of 3 key risk factors for heart disease: high blood pressure, high cholesterol, and smoking. Other key indicator include diabetic status, obesity (high BMI), not getting enough physical activity or drinking too much alcohol. Detecting and preventing the factors that have the greatest impact on heart disease is very important in healthcare. Computational developments, in turn, allow the application of machine learning methods to detect "patterns" from the data that can predict a patient's condition.

    
    **Where did the dataset come from and what treatments did it undergo?** \n
    Originally, the dataset come from the CDC and is a major part of the Behavioral Risk Factor Surveillance System (BRFSS), which conducts annual telephone surveys to gather data on the health status of U.S. residents. As the CDC describes: "Established in 1984 with 15 states, BRFSS now collects data in all 50 states as well as the District of Columbia and three U.S. territories. BRFSS completes more than 400,000 adult interviews each year, making it the largest continuously conducted health survey system in the world.". The most recent dataset (as of February 15, 2022) includes data from 2020. It consists of 401,958 rows and 279 columns. The vast majority of columns are questions asked to respondents about their health status, such as "Do you have serious difficulty walking or climbing stairs?" or "Have you smoked at least 100 cigarettes in your entire life? [Note: 5 packs = 100 cigarettes]". In this dataset, I noticed many different factors (questions) that directly or indirectly influence heart disease, so I decided to select the most relevant variables from it and do some cleaning so that it would be usable for machine learning projects.
    

    **What can you do with this dataset?** \n
    As described above, the original dataset of nearly 300 variables was reduced to just about 20 variables. In addition to classical EDA, this dataset can be used to apply a range of machine learning methods, most notably classifier models (logistic regression, SVM, random forest, etc.). You should treat the variable "HeartDisease" as a binary ("Yes" - respondent had heart disease; "No" - respondent had no heart disease). But note that classes are not balanced, so the classic model application approach is not advisable. Fixing the weights/undersampling should yield significantly betters results. Based on the dataset, I constructed a logistic regression model and embedded it in an application you might be inspired by: https://sanketbairagi-final-project-home-mg4j3l.streamlit.app/. 
    """)

    df=pd.read_csv("https://raw.githubusercontent.com/SanketBairagi/final_project/main/heart_2020_cleaned.csv")
    st.dataframe(df.head(10))
    
    st.header("Columns Description")
    st.markdown("""
* HeartDisease: Respondents that have ever reported having coronary heart disease (CHD) or myocardial infarction (MI).
* BMI: Body Mass Index (BMI).
* Smoking: Have you smoked at least 100 cigarettes in your entire life?
* AlcoholDrinking: Heavy drinkers (adult men having more than 14 drinks per week and adult women having more than 7 drinks per week
* Stroke: (Ever told) (you had) a stroke?
* PhysicalHealth: Now thinking about your physical health, which includes physical illness and injury, for how many days during the past 30 days was your physical health not good? (0-30 days).
* MentalHealth: Thinking about your mental health, for how many days during the past 30 days was your mental health not good? (0-30 days).
* DiffWalking: Do you have serious difficulty walking or climbing stairs?
* Sex: Are you male or female?
* AgeCategory: Fourteen-level age category. (then calculated the mean)
* Race: Imputed race/ethnicity value.
* Diabetic: (Ever told) (you had) diabetes?
* PhysicalActivity: Adults who reported doing physical activity or exercise during the past 30 days other than their regular job.
* GenHealth: Would you say that in general your health is...
* SleepTime: On average, how many hours of sleep do you get in a 24-hour period?
* Asthma: (Ever told) (you had) asthma?
* KidneyDisease: Not including kidney stones, bladder infection or incontinence, were you ever told you had kidney disease?
* SkinCancer: (Ever told) (you had) skin cancer?
    """)

    st.header("Our Analysis On Data")
    st.markdown("""
* In our sample, around 8 among 100 individuals suffer from heart disease.
* The BMI of heart disease patients is slightly higher than that of healthy individuals.
* The older the individual, the more susceptible they are to heart disease.
* ~10% of males suffer from heart disease, while only ~7% of females do.
* The pecentage of heart disease is highest (> 10%) among Native americans, followed by whites (~9%). The least percentage of heart disease (~3%) is among asians.
* A lot more people who suffer from heart disease say they have poor or fair health compared to those who don't.
* 79% of healthy individuals have been physically active in the past 30 days, compared to 64% in heart disease patients.
* Abnormal sleeep duration is more prevalent in heart disease patients. Even though heart disease patients make 8.5% of the sample, they have higher percentages of sleep less than 6 hours or more than 9 hours, which is considered abnormal.
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


if selected=="Health tips":
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
     
    st.header("Recomendations To Avoid Heart Disease")
    st.markdown("""
    #### 10 Essential Measures to Prevent Cardiovascular Disease

1. Healthy nutrition. The composition of the daily diet significantly affects the state of blood vessels and the heart. Frequent and excessive consumption of fatty and fried foods, coffee, chicken eggs, salt and sugar is a sure way to worsen the condition of blood vessels and develop heart attacks, strokes, hypertension and other dangerous ailments. The increased content of saturated fats, caffeine, salt and sugar increases the level of "bad" cholesterol and blood sugar. Under their influence, atherosclerotic plaques that calcify over time are formed on the vascular walls. There is a narrowing of the lumen of the vessels, leading to their wear. This factor increases the load on the heart, arterial hypertension develops. Hypertension, in turn, leads to the development of many serious diseases that can lead to disability and death.

2. Fighting excess weight. Obesity always increases the risk of vascular and heart pathologies - every extra 10 kg can increase blood pressure by 10-20 mm Hg. Art. All people need to be regularly weighed and have their abdominal circumference measured to determine abdominal obesity.

3. Fight against physical inactivity. Hypodynamia is one of the common causes of diseases of the heart and blood vessels. This is confirmed by the facts about the low physical activity of citizens and the elderly. Remember! Physical activity should be appropriate for age and general health. Be sure to check with your doctor if you have any contraindications for physical education, and what loads are acceptable for you!

4. Giving up bad habits. All studies on the effects of smoking, alcohol and drugs point to one indisputable fact - giving up these bad habits can reduce the risk of heart and vascular diseases by dozens of times. If you cannot get rid of addiction yourself, then to give up addictions, you should use the following methods: to quit smoking - acupuncture, nicotine patches or chewing gums, hypnosis; to refuse alcohol or drug addiction - a course of treatment and rehabilitation by a professional narcologist.

5. Fighting stress. Frequent stressful situations lead to wear of blood vessels and myocardium. During nervous tension, the level of adrenaline rises. In response to its impact, the heart begins to beat faster, and the vessels are constricted by spasm. As a result, there is a jump in blood pressure, and the myocardium wears out much faster.

6. Self-control of blood pressure and its timely reduction An increase in blood pressure leads to the development of coronary artery disease, heart attacks, strokes and other pathologies of the heart and blood vessels. That is why all people should regularly monitor pressure indicators.

7. Systematic preventive examination. Scheduled preventive examination and timely visits to a cardiologist should become the norm for people at risk for the development of pathologies of the heart and blood vessels. The same applies to people who report an increase in blood pressure when measured independently. Do not neglect the recommendations of your doctor!

8. Controlling blood cholesterol levels It is necessary to start annually to control the level of cholesterol in the blood after 30 years. In healthy people, its level should not exceed 5 mmol / l, and in patients with diabetes - 4-4.5 mmol / l.

9. Blood sugar control It is necessary to start monitoring blood sugar levels annually after 40-45 years. Its level should not exceed 3.3-5.5 mmol / l (in the blood from a finger), 4-6 mmol / l (in the blood from a vein).

10. Taking blood thinners For people at risk, a cardiologist may recommend taking blood thinners. The choice of the drug, its dose, the duration of the course of administration is determined only by the doctor, guided by the data of analyzes and other examinations.

**Compliance with these rules for the prevention of cardiovascular diseases will significantly reduce the risk of their development. Remember this and be healthy!**
    
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

        SleepTime= ((sleep_time-1)/(24-1))

        if bmi_cat == "Under_weight":
            BMICategoryx = 0
        elif bmi_cat == "Normal_weight":
            BMICategoryx = 1
        elif bmi_cat == "Over_weight":
            BMICategoryx = 2
        elif bmi_cat == "Obese":
            BMICategoryx = 3
        else :
            BMICategoryx = 4  


        BMICategory=((BMICategoryx-0)/(4-0))


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

    


            
