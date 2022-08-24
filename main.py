import pandas as pd
import streamlit as st
import plotly.express as px

#######################################



st.set_page_config(page_title='c.AI',
    page_icon=':heart:',
    layout="centered")

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.markdown(
        f"""
<style>
    .reportview-container .main .block-container{{
        max-width: 80%;
        padding-top: 5rem;
        padding-right: 5rem;
        padding-left: 5rem;
        padding-bottom: 5rem;
    }}
    img{{
    	max-width:40%;
    	margin-bottom:40px;
    }}
</style>
""",
        unsafe_allow_html=True,
    )
#######################################

# container -> horizontal sections
# columns -> vertical sections (can be created inside containers or directly in the app)
# sidebar -> a vertical bar on the side of app

title = st.container()
explanation = st.container()
test = st.container()
inputs = st.container()
risk = st.container()
text = st.container()
graph = st.container()
ref = st.container()
#######################################

#CONTAINER PURELY FOR TITLE AND LOGO

with title:
        col1, col2, col3 = st.columns(3)

        with col1:
            st.write(' ')

        with col2:
            st.image('logo.png')

        with col3:
            st.write(' ')
            
        st.markdown("<h1 style='text-align: center; color: black;'>Lp(a) Risk and Benefit Algorithm using Causal AI<h1>", unsafe_allow_html=True)

#CONTAINER FOR TEXT EXPLANATION

with explanation:
        
        st.subheader("Estimating risk of Heart Attack & Stroke caused by Lp(a)")
        #st.write("Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?")
        st.write("Lp(a) is a cholesterol-carrying molecule that circulates in the blood and can damage your arteries, causing a heart attack or stroke. You can measure how much your blood level of Lp(a) increases your risk of having a heart attack or stroke using this app.") 
        st.write("Enter your health information in the boxes below. The graph will show you your risk of having a heart attack, stroke, or undergoing a procedure to clear a blocked artery at any age up to age 80.")
        st.write("You can then enter your Lp(a) level using the slider bar below the graph to see how much your level of Lp(a) increases your risk of having a heart attack or stroke.")
        st.write("The only way to know how much your Lp(a) level increases your risk of having a heart attack or stroke is to measure it. Persons with high Lp(a) levels may be at increased risk and not even know it.")
        
        
# CONTAINER PURELY FOR TESTING. WILL BE COMMENTED OUT

##with st.sidebar:
##    add_radio = st.radio(
##        "Choose a shipping method",
##        ("Standard (5-15 days)", "Express (2-5 days)")
##    )
##    slide1 = st.slider('Input your value', 0, 100, 50)
##    slide2 = st.slider('Input your value', 0, 20, 10)


# CONTAINER FOR INPUTS

with inputs:
    st.subheader('**Enter your health information below**')

    with st.form('Inputs'):

        col1, col2 = st.columns(2)

        
            
        with col1:
            sex = st.selectbox("Sex", ('-', 'Male', 'Female'))
            if sex != '-':
                sex = int(sex == 'Male')

            age = st.number_input('Age (years) (ages 45-70)', step = 1)
            st.write('Cholesterol')
            TC = st.number_input('Total Cholesterol (mmol/L) (range 2.6-10.3)', step = 0.1)
            LDL = st.number_input('LDL Cholesterol (mmol/L) (range 2.6-3.4)', step = 0.1)
            HDL = st.number_input('HDL Cholesterol (mmol/L) (range 0.5-3.1)', step = 0.1)
            if TC != 0.0 and HDL != 0.0:
                nHDL = TC - HDL
            #st.write(' ')
            #    st.write('Non-HDL Cholesterol: ', round(nHDL, 2))
            #else:
            #    st.write('Non-HDL Cholesterol:')
            apoB = st.number_input('apoB (mg/dL)', step = 0.1)
            SBP = st.number_input('Systolic Blood Pressure (mmHg) (range 90-200)', step = 0.1)
            trtbp = st.selectbox("Are you taking a medicine to lower blood pressure?", ('-', 'No', 'Yes'))

        with col2:
            #st.write('BMI (kg/m²)')
            height = st.number_input('Height (cm)', step = 0.1)
            weight = st.number_input('Weight (kg)', step = 0.1)
            if height != 0.0 and weight != 0.0:
                BMI = round(weight/((height/100)**2))
            #st.write(' ')
            #    st.write('BMI: ', BMI)
            #else:
            #    st.write('BMI:')
            st.write('Height and Weight used to calculate BMI (kg/m²)')
            wcirc = st.number_input('Waist Circumference (cm) - if known', step = 0.1)
            hba1c = st.number_input('HbA1c (mmol/mol) - if known', step = 0.1)
            diab = st.selectbox("Do you have diabetes?", ('-', 'No', 'Yes'))
            if diab != '-':
                diab = int(diab == 'Yes')

            smoke = st.selectbox("Do you currently smoke?", ('-', 'No', 'Yes'))
            if smoke != '-':
                smoke = int(smoke == 'Yes')

            fmr_tob = st.selectbox("Have you ever smoked?", ('-', 'No', 'Yes'))
            if fmr_tob != '-':
                fmr_tob = int(fmr_tob == 'Yes')

            famhx = st.selectbox("Has anyone in your family had a heart attack or stroke?", ('-', 'No', 'Yes'))
            if famhx != '-':
                famhx = int(famhx == 'Yes')
        print(sex, age, TC, LDL, HDL, apoB, SBP, height, weight, wcirc, hba1c, diab, smoke, fmr_tob, famhx)
                
        btn = st.form_submit_button('Calculate Risk')
    if btn:
        print('pressed')

        #st.write(sex, age, TC, LDL, HDL, apoB, SBP, height, weight, wcirc, hba1c, diab, smoke, fmr_tob, famhx)
        #print(sex, age, TC, LDL, HDL, apoB, SBP, height, weight, wcirc, hba1c, diab, smoke, fmr_tob, famhx)
        #if sex != '-' and age != 0.0 and TC != 0.0 and LDL != 0.0 and HDL != 0.0 and SBP != 0.0 and trtbp != '-' and height != 0.0 and weight != 0.0 and diab != '-' and smoke != '-' and fmr_tob != '-' and famhx != '-':

        ldl_treatment = 0
        ldl_dec = 0

        age_from_ldl = 45
        age_to_ldl = 80

        sbp_treatment = 0
        sbp_dec = 0

        age_from_sbp = 45
        age_to_sbp = 80

        riskList = calculate(age, sex, LDL, ldl_treatment, ldl_dec,
                             age_from_ldl, age_to_ldl, HDL, SBP, sbp_treatment, sbp_dec,
                             age_from_sbp, age_to_sbp, smoke, fmr_tob, diab, BMI, famhx)


        e_age = riskList[1]
        riskList = riskList[0]
        values = [num * 100 for num in riskList]

        chart_data = pd.DataFrame({
            'age':[a for a in range(45, 81)],
            'risk':values
            })

        st.line_chart(chart_data, x = 'age', y = 'risk')


with risk:
        st.write(' ')
        st.write(' ')
        st.write('** Your risk of having a heart attack, stroke or coronary revascularization procedure:')
        st.image('graphEG.png')
        st.write('Enter your Lp(a) level to see how much your Lp(a) level increases your risk of heart attack and stroke.')
        slide = st.slider('', 0, 130, 25)

with text:
        st.write(' ')
        st.subheader('What to do if your Lp(a) level increases your risk of having a heart attack or stroke')
        #st.write('At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat facere possimus, omnis voluptas assumenda est, omnis dolor repellendus. Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae sint et molestiae non recusandae. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat.')
        st.write('First, it is important to be aware that the level of Lp(a) in your blood is mostly inherited. If you have high blood levels of Lp(a), then other members of your family may also be at increased risk of heart attack or stroke because of high Lp(a) levels. Indeed, high Lp(a) levels may be the most commonly inherited cause of heart attacks and strokes. So, if your Lp(a) level is elevated, or if your risk of heart attack and stroke is increased by your Lp(a) levels, other members of your family may benefit from measuring their Lp(a) levels to determine if they are at increased risk.')
        st.write('Unfortunately, Lp(a) levels in the blood cannot be lowered by diet or exercise. In addition, there are no approved medicines that specifically lower Lp(a) levels. However, new very powerful Lp(a) lowering therapies are currently in development.')
        st.write('Although diet and exercise does not reduce Lp(a) levels, and there are no approved therapies to lower Lp(a), you can still reduce your risk of having a heart attack or stroke despite having high Lp(a) levels.')  
        st.write('If your risk of heart attack and stroke is increased by your Lp(a) level, then current clinical practise guidelines recommend that you should more intensely lower other causes of heart attack and stroke, such as your LDL or blood pressure level. Although lowering LDL and blood pressure will not lower your Lp(a) level, it will reduce your overall risk of having a heart attack and stroke.')              
        #st.write('Using the slider bars below, you can estimate how much you need to lower your LDL or blood pressure to reduce your risk of heart attack and stroke by the same amount as the increased risk caused by your Lp(a) levels.') 
        st.write('Using the slider bars below, you can estimate how much you would have to lower your LDL or blood pressure to reduce your risk of heart attack and stroke by the same amount as the increased risk caused by your Lp(a) level. This information can help guide you about how much more intensely you need to lower your LDL and blood pressure level to improve your cardiovascular health despite having high Lp(a) levels.')
with graph:
        st.write(' ')
        st.write('** How much more intensely should I lower my LDL or blood pressure if I have an increased risk of heart attack and stroke caused by high Lp(a)?')
        st.image('graphEG.png')
        
        col1, col2 = st.columns(2)

        with col1:
                st.write('How much should I lower my LDL?')
                slider = st.slider('', 0, 60, 60)

        with col2:
                st.write('How much should I lower my blood pressure?')
                slider1 = st.slider('', 0, 30, 10)

# TESTING 2 SLIDERS IN THE SAME LINE

# END OF TEST
with ref:
        st.write(' ')
        st.subheader('Further information')
        st.write('References')
