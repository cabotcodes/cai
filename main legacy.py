import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import math
import copy
############################## Data ##############################
men_mean_LDL = [3.538712, 3.539897, 3.597524, 3.61369, 3.651612, 3.689894, 3.701626, 3.686807, 3.721783, 3.7148, 3.727947, 3.718497, 3.747202, 3.779036, 3.787469, 3.786441, 3.766688, 3.774085, 3.7766, 3.764718, 3.784948, 3.767719, 3.765946, 3.759482, 3.76046, 3.738732, 3.728768, 3.724888, 3.711604, 3.688589, 3.664941]
women_mean_LDL = [3.145337, 3.157391, 3.194953, 3.222178, 3.238601, 3.268339, 3.315789, 3.378602, 3.413502, 3.483169, 3.551529, 3.584646, 3.645474, 3.695869, 3.765233, 3.816435, 3.827959, 3.871363, 3.894899, 3.901048, 3.948822, 3.9807, 3.987348, 3.985714, 3.99556, 4.000246, 4.006666, 4.009283, 4.042506, 4.015938, 4.002537]
men_mean_SBP = [132.2889, 132.2815, 132.6796, 133.4982, 133.2009, 133.6636, 134.2012, 134.3514, 135.0412, 135.3859, 136.0278, 136.5888, 136.7181, 137.8215, 138.0063, 138.3607, 139.0388, 139.4854, 140.1192, 140.7073, 141.6148, 141.8493, 142.4003, 142.7055, 144.5164, 144.3501, 145.6001, 145.6852, 145.9222, 146.8331, 145.7794]
women_mean_SBP = [120.4948, 121.2369, 121.7119, 122.2884, 122.8392, 124.1869, 124.7012, 125.4704, 126.3273, 127.2126, 128.2291, 129.2085, 129.8408, 130.7985, 131.2232, 131.9118, 132.4455, 133.4231, 134.2422, 135.5702, 135.8599, 137.0978, 138.5324, 139.2771, 140.0216, 140.8377, 142.0637, 142.4703, 143.666, 144.3988, 144.1031]
men_Ha = [0.9987, 0.9989, 0.9987, 0.9984, 0.9979, 0.9976, 0.9977, 0.9972, 0.9971, 0.9966, 0.996, 0.9959, 0.9956, 0.995, 0.9951, 0.994, 0.9943, 0.9936, 0.9941, 0.9934, 0.9936, 0.9936, 0.9928, 0.9931, 0.9938, 0.9935, 0.9928, 0.9929, 0.993, 0.9933, 0.9935, 0.9944, 0.9963, 0.997, 0.998]
men_Hb = [0.9999, 0.9999, 0.9997, 0.9998, 0.9997, 0.9996, 0.9996, 0.9995, 0.9994, 0.9994, 0.9993, 0.9992, 0.9991, 0.9989, 0.9988, 0.9984, 0.9982, 0.9977, 0.9974, 0.9967, 0.996, 0.9954, 0.9942, 0.9931, 0.9917, 0.991, 0.9894, 0.9866, 0.9848, 0.9834, 0.9821, 0.9807, 0.9795, 0.9785, 0.9812]
women_Ha = [0.9998, 0.9998, 0.9997, 0.9997, 0.9996, 0.9996, 0.9996, 0.9994, 0.9994, 0.9994, 0.9992, 0.9992, 0.9992, 0.999, 0.9988, 0.9985, 0.9987, 0.9987, 0.9984, 0.9985, 0.9983, 0.9978, 0.998, 0.998, 0.998, 0.9978, 0.9977, 0.9976, 0.9972, 0.9971, 0.9973, 0.998, 0.9978, 0.9989, 0.9988]
women_Hb = [1, 0.9999, 0.9999, 0.9999, 0.9998, 0.9998, 0.9997, 0.9996, 0.9997, 0.9996, 0.9995, 0.9995, 0.9994, 0.9991, 0.9992, 0.9991, 0.9989, 0.9986, 0.9983, 0.998, 0.9976, 0.9973, 0.9967, 0.9962, 0.9954, 0.9947, 0.9933, 0.9928, 0.9914, 0.9913, 0.9897, 0.9888, 0.9886, 0.9875, 0.9882]

Ha_list = [women_Ha, men_Ha]
Hb_list = [women_Hb, men_Hb]

mean_LDL_list = [women_mean_LDL, men_mean_LDL]
mean_SBP_list = [women_mean_SBP, men_mean_SBP]

Ha_list = [women_Ha, men_Ha]
Hb_list = [women_Hb, men_Hb]

mean_LDL_list = [women_mean_LDL, men_mean_LDL]
mean_SBP_list = [women_mean_SBP, men_mean_SBP]
############################## Data ##############################

########################### Algorithm ###########################
@st.cache
def calculate(age, sex, ldl, ldl_rx, ldl_dec, age_start_rx_ldl, age_stop_rx_ldl, hdl, sbp, sbp_rx, sbp_dec, age_start_rx_sbp, age_stop_rx_sbp, smoke, fmr_tob, prevalent_diabetes_35, bmi, fam_hx_chd, Lp_a = None):
    if Lp_a == None:
        Lp_a = [20.66, 16.6][sex]
    past_a_sums = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    dm = int(prevalent_diabetes_35)

    lnRR_a_list = []
    lnRR_b_list = []

    lnRR_a = [0 for _ in range(80-45)]
    lnRR_b = [0 for _ in range(80-45)]
    a_t = [0 for _ in range(80-45)]
    b_t = [0 for _ in range(80-45)]
    c_t = [0 for _ in range(80-45)]
    d_t = [0 for _ in range(80-45)]
    e_t = [0 for _ in range(80-45)]
    f_t = [0 for _ in range(80-45)]
    m_t = [0 for _ in range(80-45)]

    LDL_ES_mmol = [0.610294236200972/45, 0.696666480552631/35]
    SBP_ES_mmol = [0.596822386208318/450, 0.562215263512178/350]

    del_LDL = ldl - mean_LDL_list[sex][age-40]
    del_SBP = sbp - mean_SBP_list[sex][age-40]

    a_beta = [
        [0.66*0.85, 0.6*0.5,
        [0.983679437374588, 0.768813402297644],
        [0.467034851783647, 0.417294201034895],
        0.800648203696211, 0.502003018790893,
        0.0239479451504817, -1.03647868828565,
        0.00305563,
        -0.609690396465665],

        [0.66*0.85, 0.6*0.5,
        [0.641703348526382, 0.4042777367951],
        [0.396454635449883, 0.351011034242294],
        0.690752315157672, 0.555861893739954,
        0.0276443494865389, -1.14697073604065,
        0.00326018,
        -0.295523487273258]
    ]

    b_beta = [
        [0.0578159753767444, 0.00765164978969782,
        [1.11270781170849, 1.23876285117286],
        [0.336045717103265, 0.462419315914295],
        0.515257189855812, 0.0179926569543217,
        0.0130494839094301, -0.377629537350312,
        -0.0841012452776191],

        [0.202829001007803, 0.021673425558946,
        [1.29162125334208, 0.857058215628963],
        [0.453034845319801, 0.382734719097288],
        0.592360632788394, 0.0374768858776153,
        0.037343953140421, -0.121996349209252,
        1.15518044231415]
    ]

    for i_a in range(20, 81):

        a_sums = [

                del_LDL*a_beta[sex][0]*(i_a-20),

                -0.12 if (ldl_rx == 1 and ((i_a) >= age_start_rx_ldl))  else 0,

                (((i_a) - age_start_rx_ldl)+1) * ldl_dec if (((i_a) - age_start_rx_ldl >= 0) and age_stop_rx_ldl - (i_a) >= 0 and ldl_rx == 1) else past_a_sums[-1][2],

                sum([del_LDL*a_beta[sex][0]*(i_a-20),
                     ((i_a - age_start_rx_ldl)+1) * ldl_dec if (((i_a) - age_start_rx_ldl >= 0) and age_stop_rx_ldl - (i_a) >= 0 and ldl_rx == 1) else past_a_sums[-1][2],
                    ]),

                del_SBP*a_beta[sex][1]*(i_a-20),

                -0.1 if (sbp_rx == 1 and ((i_a) >= age_start_rx_sbp)) else 0,

                (((i_a) - age_start_rx_sbp)+1) * sbp_dec if (((i_a) - age_start_rx_sbp >= 0) and (age_stop_rx_sbp - (i_a) >= 0) and sbp_rx == 1) else past_a_sums[-1][6],

                sum([del_SBP*a_beta[sex][1]*(i_a-20),
                     (((i_a) - age_start_rx_sbp)+1) * sbp_dec if (((i_a) - age_start_rx_sbp >= 0) and (age_stop_rx_sbp - (i_a) >= 0) and sbp_rx == 1) else past_a_sums[-1][6],
                    ]),


                #del_LDL*a_beta[sex][0]*(i_a-20)*LDL_ES_mmol[sex],
                (LDL_ES_mmol[sex] * sum([del_LDL*a_beta[sex][0]*(i_a-20),
                                         (((i_a) - age_start_rx_ldl)+1) * ldl_dec if (((i_a) - age_start_rx_ldl >= 0) and (age_stop_rx_ldl - (i_a) >= 0) and ldl_rx == 1) else past_a_sums[-1][2]]
                                       )) + (-0.12 if (ldl_rx == 1 and ((i_a) >= age_start_rx_ldl))  else 0),


                #del_SBP*a_beta[sex][1]*(i_a-20)*SBP_ES_mmol[sex],
                (SBP_ES_mmol[sex] * sum([del_SBP*a_beta[sex][1]*(i_a-20),
                                         (((i_a) - age_start_rx_sbp)+1) * sbp_dec if (((i_a) - age_start_rx_sbp >= 0) and (age_stop_rx_sbp - (i_a) >= 0) and sbp_rx == 1) else past_a_sums[-1][6]]
                                       )) + (-0.1 if (sbp_rx == 1 and ((i_a) >= age_start_rx_sbp)) else 0),


                smoke * a_beta[sex][2][dm],
                fmr_tob * a_beta[sex][3][dm],
                prevalent_diabetes_35 * a_beta[sex][4],
                fam_hx_chd * a_beta[sex][5],
                bmi * a_beta[sex][6],
                hdl * a_beta[sex][7],

                (Lp_a - [20.66, 16.6][sex]) * a_beta[sex][8]

            ]

        past_a_sums.append(a_sums)

        b_sums = [

                del_LDL * b_beta[sex][0],
                del_SBP * b_beta[sex][1],

                smoke * b_beta[sex][2][dm],
                fmr_tob * b_beta[sex][3][dm],
                prevalent_diabetes_35 * b_beta[sex][4],
                fam_hx_chd * b_beta[sex][5],
                bmi * b_beta[sex][6],
                hdl * b_beta[sex][7]

            ]

        lnRR_a_list.append(sum(a_sums[8:]) - a_beta[sex][9])
        lnRR_b_list.append(sum(b_sums) - b_beta[sex][8])

    for i in range(80-45):
        lnRR_a[i] = lnRR_a_list[i+26]
        lnRR_b[i] = lnRR_b_list[i+26]

        if i < age - 45:
            a_t[i] = 0
            b_t[i] = 0
            c_t[i] = 0
            d_t[i] = 0
            e_t[i] = 0
            f_t[i] = 0
            m_t[i] = 0

        elif i == age - 45: #0:
            a_t[i] = 1 - (Ha_list[sex][i] ** math.exp(lnRR_a[i]))
            b_t[i] = 1 - (Hb_list[sex][i] ** math.exp(lnRR_b[i]))
            c_t[i] = b_t[i]
            d_t[i] = a_t[i]

            e_t[i] = 1 - c_t[i] - d_t[i]
            f_t[i] = 0 + d_t[i]
            m_t[i] = 0 + c_t[i]

        else:
            a_t[i] = 1 - (Ha_list[sex][i] ** math.exp(lnRR_a[i]))
            b_t[i] = 1 - (Hb_list[sex][i] ** math.exp(lnRR_b[i]))
            c_t[i] = e_t[i-1] * b_t[i]
            d_t[i] = e_t[i-1] * a_t[i]

            e_t[i] = e_t[i-1] - c_t[i] - d_t[i]
            f_t[i] = f_t[i-1] + d_t[i]
            m_t[i] = m_t[i-1] + c_t[i]

    f_t.insert(0, 0)
    return [f_t, 45 + sum(e_t)]
########################### Algorithm ###########################

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
                
        btn = st.form_submit_button('Calculate Risk')


    values = None
    valuesRx = None
    ageList = None


    age_from_ldl = 45
    age_to_ldl = 80

    age_from_sbp = 45
    age_to_sbp = 80

    if btn:
        pass

    if SBP > 0.0 and LDL > 0.0:

        riskList = calculate(age, sex, LDL, 0, 0,
                             age_from_ldl, age_to_ldl, HDL, SBP, 0, 0,
                             age_from_sbp, age_to_sbp, smoke, fmr_tob, diab, BMI, famhx)


        e_age = riskList[1]
        riskList = riskList[0]
        values = [num * 100 for num in riskList]
        ageList = [a for a in range(45, 81)]


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
