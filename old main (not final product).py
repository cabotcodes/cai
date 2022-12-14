import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import matplotlib
import math
import copy
############################## Data ##############################
men_mean_LDL = [3.3174731188868307, 3.334143838077217, 3.350898329725846, 3.3677370147998453, 3.3846603163817544, 3.4016686596801553, 3.4187624720403567, 3.435942182955132, 3.45320822407551, 3.4705610292216185, 3.4880010343935868, 3.4955003878975948, 3.54100077579519, 3.555500387897595, 3.611998965606413, 3.655001292991983, 3.6629997414016033, 3.6299999999999994, 3.6829997414016034, 3.6814998707008013, 3.695500387897595, 3.68899922420481, 3.700499094905611, 3.724998707008017, 3.7459994828032066, 3.7070002585983968, 3.7089992242048098, 3.714000517196793, 3.721499870700802, 3.714000517196793, 3.718500129299198, 3.69899922420481, 3.6940005171967933, 3.6870002585983968, 3.6940005171967933, 3.6570002585983965, 3.6470002585983967, 3.6449987070080163, 3.631998965606413, 3.613838970778381, 3.595769775924489, 3.5777909270448665, 3.559901972409642, 3.542102462547594, 3.524391950234856, 3.506769990483682, 3.4892361405312635, 3.471789959828607, 3.454431010029464, 3.437158854979317, 3.41997306070442]
women_mean_LDL = [2.861743860038676, 2.8833691285024443, 2.905157812093143, 2.9271111456857857, 2.949230373486938, 2.971516749105227, 2.9939715356223946, 3.016596005664881, 3.03939144147595, 3.062359134988363, 3.085500387897595, 3.0970002585983964, 3.12, 3.162999741401603, 3.1659994828032065, 3.2199999999999998, 3.2514998707008016, 3.3110007757951894, 3.351998965606413, 3.43, 3.497000258598397, 3.5314998707008014, 3.601998965606413, 3.654000517196793, 3.7199999999999998, 3.7695009050943886, 3.7919989656064126, 3.821998965606413, 3.8435014222911814, 3.83899922420481, 3.9010007757951897, 3.9270002585983965, 3.934998707008017, 3.9259994828032063, 3.9440005171967933, 3.9495009050943883, 3.9449987070080166, 3.9380010343935865, 3.9570002585983968, 3.9329997414016034, 3.9529997414016034, 3.9332347426945957, 3.9135685689811224, 3.8940007261362166, 3.8745307225055354, 3.8551580688930076, 3.8358822785485422, 3.8167028671558, 3.797619352820021, 3.7786312560559208, 3.759738099775641]

men_mean_SBP = [127.09770000000009, 127.64270000000009, 128.1877000000001, 128.73270000000008, 129.27770000000007, 129.82270000000005, 130.36770000000004, 130.91270000000003, 131.45770000000002, 132.0027, 132.5477, 132.5595, 133.0417, 133.9244, 133.8602, 134.1759, 134.8107, 135.0133, 136.0058, 136.2948, 136.8521, 137.2601, 137.7067, 138.7961, 139.1646, 139.5142, 140.0917, 140.7533, 141.3936, 142.006, 142.6065, 143.1211, 143.6272, 144.0828, 145.4364, 145.5392, 146.494, 146.6693, 146.9347, 147.3451, 147.8901, 148.43509999999998, 148.98009999999996, 149.52509999999995, 150.07009999999994, 150.61509999999993, 151.16009999999991, 151.7050999999999, 152.2500999999999, 152.79509999999988, 153.34009999999986]
women_mean_SBP = [111.82199999999999, 112.72099999999999, 113.61999999999999, 114.51899999999999, 115.41799999999999, 116.317, 117.216, 118.115, 119.014, 119.913, 120.812, 121.5938, 122.2175, 122.8461, 123.4768, 124.808, 125.45, 126.2387, 127.1368, 128.1205, 129.2104, 130.3305, 131.2608, 132.1755, 132.5652, 133.3094, 134.2712, 135.0678, 136.1804, 137.2556, 137.6882, 139.0932, 140.3054, 141.3204, 142.0509, 142.8775, 144.2726, 145.0231, 145.8587, 146.5092, 145.9757, 146.8747, 147.7737, 148.6727, 149.5717, 150.4707, 151.3697, 152.2687, 153.1677, 154.0667, 154.9657]

men_Ha = [0.9999, 0.9999, 0.9998, 0.9999, 0.9998, 0.9997, 0.9997, 0.9997, 0.9995, 0.9994, 0.999, 0.9993, 0.9989, 0.9991, 0.9989, 0.9983, 0.9985, 0.9984, 0.998, 0.9975, 0.997, 0.9974, 0.9966, 0.9966, 0.996, 0.9953, 0.9953, 0.9951, 0.9944, 0.9945, 0.9934, 0.9936, 0.9929, 0.9931, 0.9923, 0.9925, 0.9922, 0.9913, 0.9915, 0.9911, 0.9909, 0.99, 0.9899, 0.9898, 0.9891, 0.9881, 0.9879, 0.9873, 0.9858, 0.987, 0.9855]
men_Hb = [1, 1, 0.9999, 1, 0.9999, 1, 0.9999, 1, 0.9999, 0.9998, 0.9997, 0.9999, 0.9997, 0.9998, 0.9997, 0.9995, 0.9996, 0.9995, 0.9994, 0.9994, 0.9991, 0.9993, 0.9989, 0.9988, 0.9987, 0.9986, 0.9984, 0.9982, 0.9979, 0.9977, 0.9971, 0.9972, 0.9965, 0.9962, 0.9953, 0.9948, 0.9944, 0.9929, 0.9924, 0.991, 0.9901, 0.9885, 0.986, 0.9848, 0.9835, 0.9817, 0.9798, 0.9763, 0.9748, 0.9717, 0.9662]

women_Ha = [1, 1, 1, 1, 1, 1, 1, 0.9999, 0.9999, 0.9999, 0.9998, 0.9999, 0.9998, 0.9998, 0.9998, 0.9997, 0.9997, 0.9996, 0.9996, 0.9994, 0.9993, 0.9994, 0.9992, 0.9992, 0.9991, 0.9989, 0.9989, 0.9989, 0.9986, 0.9984, 0.9981, 0.9981, 0.9982, 0.9979, 0.998, 0.9975, 0.997, 0.9969, 0.9968, 0.9964, 0.9961, 0.9956, 0.9955, 0.9951, 0.9944, 0.9939, 0.9934, 0.993, 0.99304, 0.9913, 0.9921]
women_Hb = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.9999, 0.9999, 0.9999, 0.9999, 0.9999, 0.9998, 0.9998, 0.9997, 0.9997, 0.9996, 0.9995, 0.9995, 0.9994, 0.9992, 0.9992, 0.9991, 0.9989, 0.9988, 0.9986, 0.9985, 0.9982, 0.9978, 0.9976, 0.9971, 0.9967, 0.9963, 0.9957, 0.995, 0.9941, 0.993, 0.992, 0.9911, 0.9902, 0.9885, 0.9874, 0.985, 0.9832, 0.9821, 0.9797]

Ha_list = [women_Ha, men_Ha]
Hb_list = [women_Hb, men_Hb]

mean_LDL_list = [women_mean_LDL, men_mean_LDL]
mean_SBP_list = [women_mean_SBP, men_mean_SBP]

Ha_list = [women_Ha, men_Ha]
Hb_list = [women_Hb, men_Hb]

mean_LDL_list = [women_mean_LDL, men_mean_LDL]
mean_SBP_list = [women_mean_SBP, men_mean_SBP]

avg_bmi = [26.98912, 27.85051]
avg_hdl = [1.598386, 1.283341]
############################## Data ##############################

########################### Algorithm ###########################
@st.cache(hash_funcs = {matplotlib.figure.Figure: lambda _: None})
def calculate(age, sex, ldl, ldl_rx, ldl_dec, age_start_rx_ldl, age_stop_rx_ldl, hdl, sbp, sbp_rx, sbp_dec, age_start_rx_sbp, age_stop_rx_sbp, smoke, fmr_tob, prevalent_diabetes_35, bmi, fam_hx_chd, Lp_a = None):
    if Lp_a == None:
        Lp_a = [20.66, 16.6][sex]
    past_a_sums = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    dm = int(prevalent_diabetes_35)

    lnRR_a_list = []
    lnRR_b_list = []

    lnRR_a = [0 for _ in range(81-30)]
    lnRR_b = [0 for _ in range(81-30)]
    a_t = [0 for _ in range(81-30)]
    b_t = [0 for _ in range(81-30)]
    c_t = [0 for _ in range(81-30)]
    d_t = [0 for _ in range(81-30)]
    e_t = [0 for _ in range(81-30)]
    f_t = [0 for _ in range(81-30)]
    m_t = [0 for _ in range(81-30)]

    LDL_ES_mmol = [0.610294236200972/45, 0.696666480552631/40]
    SBP_ES_mmol = [0.596822386208318/450, 0.562215263512178/400]

    del_LDL = ldl - mean_LDL_list[sex][age-30]
    del_SBP = sbp - mean_SBP_list[sex][age-30]
    
    a_beta = [
        [1, 1,
        [0.983679437374588, 0.768813402297644],
        [0.467034851783647, 0.417294201034895],
        0.800648203696211, 0.502003018790893,
        0.00895775920895248, -0.632265086010107,
        0],

        [1, 1,
        [0.641703348526382, 0.4042777367951],
        [0.396454635449883, 0.351011034242294],
        0.690752315157672, 0.555861893739954,
        0.0109834603573848, -0.612663093385597,
        0]
    ]

    b_beta = [
        [0.00432149552442511, 0.0000196190161699591,
        [1.11270781170849, 1.23876285117286],
        [0.336045717103265, 0.462419315914295],
        0.515257189855812, 0.0179926569543217,
        0.0140518092696023, -0.201163272313767,
        0],

        [0.00866812947141468, 0.000260041603209642,
        [1.29162125334208, 0.857058215628963],
        [0.453034845319801, 0.382734719097288],
        0.592360632788394, 0.0374768858776153,
        0.0148344238334535, 0.00425393915728762,
        0]
    ]

    for i_a in range(30, 81):

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
                (bmi - avg_bmi[sex]) * a_beta[sex][6],
                (hdl - avg_hdl[sex]) * a_beta[sex][7],

                (Lp_a - [20.66, 16.6][sex]) * a_beta[sex][8]

            ]
        #print(f"a_sums: {a_sums}")
        past_a_sums.append(a_sums)

        b_sums = [

                del_LDL * b_beta[sex][0],
                del_SBP * b_beta[sex][1],

                smoke * b_beta[sex][2][dm],
                fmr_tob * b_beta[sex][3][dm],
                prevalent_diabetes_35 * b_beta[sex][4],
                fam_hx_chd * b_beta[sex][5],
                (bmi - avg_bmi[sex]) * b_beta[sex][6],
                (hdl - avg_hdl[sex]) * b_beta[sex][7]

            ]
        #print(f"b_sums: {b_sums}")

        lnRR_a_list.append(sum(a_sums[8:]))
        lnRR_b_list.append(sum(b_sums))
        #print()
    for i in range(81 - 30):
        lnRR_a[i] = lnRR_a_list[i]
        lnRR_b[i] = lnRR_b_list[i]

        
        #if i < age - 30:
        #    a_t[i] = 0
        #    b_t[i] = 0
        #    c_t[i] = 0
        #    d_t[i] = 0
        #    e_t[i] = 0
        #    f_t[i] = 0
        #    m_t[i] = 0

        if i == 0: #age - 30:
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
        #print(f"{i}, age: {age}, Ha: {Ha_list[sex][i]}, Hb: {Hb_list[sex][i]}, lnRR_a: {round(lnRR_a[i], 6)}, lnRR_b: {round(lnRR_b[i], 6)}, a_t: {round(a_t[i], 6)}, b_t: {round(b_t[i], 6)}, c_t: {round(c_t[i], 6)}, d_t: {round(d_t[i], 6)}, e_t: {round(e_t[i], 6)}, f_t: {round(f_t[i], 6)}, m_t: {round(m_t[i], 6)}")

    f_t.insert(0, 0)
    return [f_t, 30 + sum(e_t)]

def calc_BMI(height, weight, units_height, units_weight):
    if units_height == "in":
        h = height * 2.54
    else:
        h = height
        
    if units_weight == "lbs":
        w = weight / 2.2
    else:
        w = weight


    BMI = round(w/((h/100)**2))

    return BMI
########################### Algorithm ###########################

st.set_page_config(page_title='LPAclinicalguidance',
    page_icon='::',
    layout="centered")

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {
	
                visibility: hidden;
	
            }
            footer:after {
                content:'Copyright ?? TBFerence & CKFerence 2022'; 
                visibility: visible;
                display: block;
                position: relative;
                padding: 5px;
                top: 2px;
            }
            
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

hide_img_fs = '''
<style>
button[title="View fullscreen"]{
    visibility: hidden;}
</style>
'''

st.markdown(hide_img_fs, unsafe_allow_html=True)

def hide_anchor_link():
    st.markdown("""
        <style>
        .css-15zrgzn {display: none}
        .css-eczf16 {display: none}
        .css-jn99sy {display: none}
        </style>
        """, unsafe_allow_html=True)



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
##with title:
##        st.image('Transparent.png', use_column_width=auto)
with title:
        col1, col2, col3, col4, col5 = st.columns(5)        
        with col1:
            st.write(' ')

        with col2:
            st.write(' ')

        with col3:
            st.image('Logo2.png')

        with col4:
            st.write(' ')

        with col5:
            st.write(' ')
  
        st.markdown("<h1 style='text-align: center; color: black;'>Lp(a) Clinical Guidance<h1>", unsafe_allow_html=True)
        #st.markdown("<h6 style='text-align: center; color: grey;'>This website will help you estimate how much your Lp(a) level increases your risk of having a heart attack or stroke, and provide you with specific guidance about what you can do to lower your risk if your Lp(a) level is elevated.<h6>", unsafe_allow_html=True)
        st.write('This website will determine how much your Lp(a) level increases your risk of having a heart attack or stroke, and provide you with specific guidance about what you can do to lower your risk if your Lp(a) level is elevated.')
#Risk and Benefit Algorithm using Causal AI
#CONTAINER FOR TEXT EXPLANATION

with explanation:
        
        st.subheader("Estimating the risk of Heart Attack & Stroke caused by Lp(a)")
        #st.write("Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?")
        st.write("Lp(a) is a cholesterol-carrying molecule that circulates in the blood and can damage your arteries, causing a heart attack or stroke. You can measure how much your blood level of Lp(a) increases your risk of having a heart attack or stroke using this app.") 
        st.write("Enter your health information in the boxes below. The graph will show you your risk of having a heart attack, stroke, or undergoing a procedure to clear a blocked artery at any age up to age 80. The only way to know how much your Lp(a) level increases your risk of having a heart attack or stroke is to measure it. Persons with high Lp(a) levels may be at increased risk and not even know it.")
        st.write("You can then enter your Lp(a) level using the slider bar below the graph to see how much your level of Lp(a) increases your risk of having a heart attack or stroke.")
        
        
        
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
    unit_col1, unit_col2, unit_col3 = st.columns([2, 1, 1])
    with unit_col1:
        units_LDL = st.radio("Cholesterol units:", ["mmol/L", "mg/dL"], horizontal = True)
    with unit_col2:
        units_height = st.radio("Height units:", ["cm", "in"], horizontal = True)
    with unit_col3:
        units_weight = st.radio("Weight units:", ["kg", "lbs"], horizontal = True)
        
    with st.form('Inputs'):
        col1, col2 = st.columns(2)

        
            
        with col1:
            sex = st.selectbox("Sex", ('-', 'Male', 'Female'))
            if sex != '-':
                sex = int(sex == 'Male')

            age = st.number_input('Age (years) (ages 30-80)', min_value = 30, max_value = 80, step = 1, key = 'age')

            st.write('Cholesterol')
            if units_LDL == "mmol/L":            
                TC = st.number_input('Total Cholesterol (mmol/L) (range 3.5 - 8.0)', value = 5.8, step = 0.1)
                LDL = st.number_input('LDL Cholesterol (mmol/L) (range 2.0 - 5.0)', value = men_mean_LDL[st.session_state.age-30], step = 0.1)
                HDL = st.number_input('HDL Cholesterol (mmol/L) (range 0.6 - 2.8)', value = avg_hdl[1], step = 0.1)
            else:
                TC = st.number_input('Total Cholesterol (mg/dL) (range 135 - 300)', step = 1)
                LDL = st.number_input('LDL Cholesterol (mg/dL) (range 80 - 200)', step = 1)
                HDL = st.number_input('HDL Cholesterol (mg/dL) (range 25 - 100)', value = avg_hdl[1] * 38.67, step = 1)

            if TC != 0.0 and HDL != 0.0:
                nHDL = TC - HDL
            #st.write(' ')
            #    st.write('Non-HDL Cholesterol: ', round(nHDL, 2))
            #else:
            #    st.write('Non-HDL Cholesterol:')
            apoB = st.number_input('apoB (mg/dL)', value = 107.6, step = 0.1)
            SBP = st.number_input('Systolic Blood Pressure (mmHg) (range 90-200)', step = 1)
            trtbp = st.selectbox("Are you taking a medicine to lower blood pressure?", ('-', 'No', 'Yes'))

        with col2:
            #st.write('BMI (kg/m??)')

            if units_height == "cm":
                height = st.number_input('Height (cm)', value = 176.3, step = 0.1)
            else:
                height = st.number_input('Height (in)', value = 176.3/2.54, step = 0.1)
            
            if units_weight == "kg":
                weight = st.number_input('Weight (kg)', value = 86.2, step = 0.1)
            else:
                weight = st.number_input('Weight (lbs)', value = 86.2 * 2.2, step = 0.1)
            
            if height != 0.0 and weight != 0.0:
                BMI = calc_BMI(height, weight, units_height, units_weight)
            #st.write(' ')
            #    st.write('BMI: ', BMI)
            #else:
            #    st.write('BMI:')
            st.write('Height and Weight used to calculate BMI (kg/m??)')
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



    age_from_ldl = 45
    age_to_ldl = 80

    age_from_sbp = 45
    age_to_sbp = 80

    if btn:
        pass

with risk:
        st.write(' ')
        st.write(' ')
        #st.write('** Your risk of having a heart attack, stroke or coronary revascularization procedure:')

        lpa_chart_placeholder = st.empty()
        if SBP > 0.0 and LDL > 0.0:

            if units_LDL == "mmol/L":
                ldl = LDL
                hdl = HDL
            else:
                ldl = LDL / 38.67
                hdl = HDL / 38.67


            riskList = calculate(age, sex, ldl, 0, 0,
                                 age_from_ldl, age_to_ldl, hdl, SBP, 0, 0,
                                 age_from_sbp, age_to_sbp, smoke, fmr_tob, diab, BMI, famhx)


            e_age = riskList[1]
            riskList = riskList[0]
            values = [num * 100 for num in riskList]
            ageList = [a for a in range(45, 81)]


            x_base = ageList
            y_base = values

            lpa_graph = go.Figure(layout = go.Layout(
                title = go.layout.Title(text = "Your risk of having a heart attack, stroke or coronary revascularization procedure:"),
                paper_bgcolor = 'rgba(255, 255, 255,1)',
                plot_bgcolor = 'rgb(255, 255, 255)',
                font_color = 'rgb(18, 49, 135)',

                spikedistance =  -1,

                xaxis = dict(
                    gridcolor = 'rgb(230, 230, 230)',
                    showline = True,
                    linecolor = 'rgb(0, 0, 0)',

                    showspikes = True,
                    spikecolor = 'rgb(150, 150, 150)',
                    spikemode  = 'across+toaxis',
                    spikesnap = 'data',
                    spikedash = 'solid',
                    spikethickness = 1,
                    ),

                yaxis = dict(
                    gridcolor = 'rgb(230, 230, 230)',
                    showline = True,
                    linecolor = 'rgb(0, 0, 0)',
                    ),

                ))

            sbpldl_graph = go.Figure(layout = go.Layout(
                title = go.layout.Title(text = "How much more intensely should I lower my LDL or blood pressure<br>if I have an increased risk of heart attack and stroke caused by high Lp(a)?"),
                paper_bgcolor = 'rgba(255, 255, 255,1)',
                plot_bgcolor = 'rgb(255, 255, 255)',
                font_color = 'rgb(18, 49, 135)',

                spikedistance =  -1,

                xaxis = dict(
                    gridcolor = 'rgb(230, 230, 230)',
                    showline = True,
                    linecolor = 'rgb(0, 0, 0)',

                    showspikes = True,
                    spikecolor = 'rgb(150, 150, 150)',
                    spikemode  = 'across+toaxis',
                    spikesnap = 'data',
                    spikedash = 'solid',
                    spikethickness = 1,
                    ),

                yaxis = dict(
                    gridcolor = 'rgb(230, 230, 230)',
                    showline = True,
                    linecolor = 'rgb(0, 0, 0)',
                    ),

                ))

        ####################################################################################

            units_lpa = st.radio("Lp(a) units:", ["nmol/L", "mg/dL"], horizontal = True)
            if units_lpa == "nmol/L":
                lpa = st.slider('Enter your Lp(a) level to see how much your Lp(a) level increases your risk of heart attack and stroke.', 0.0, 500.0, [20.66, 16.6][sex])
            else:
                LPA = st.slider('Enter your Lp(a) level to see how much your Lp(a) level increases your risk of heart attack and stroke.', 0.0, 1000.0, [20.66*2.15, 16.6*2.15][sex])
                lpa = LPA / 2.15
            
            riskList_lpa = calculate(age, sex, ldl, 0, 0, age_from_ldl, age_to_ldl,
                                     hdl, SBP, 0, 0, age_from_sbp, age_to_sbp,
                                     smoke, fmr_tob, diab, BMI, famhx, lpa)

            riskList_lpa = riskList_lpa[0]
            values_lpa = [num * 100 for num in riskList_lpa]

            x_lpa = ageList
            y_lpa = values_lpa

            all_values = values + values_lpa
            

            lpa_graph.add_trace(go.Scatter(
                x = x_base,
                y = y_base,
                line_color = 'rgb(18, 49, 135)',
                mode='lines',
                name='Risk without Lp(a)',
                hovertemplate="<br>".join(
                    ["Age: %{x}",
                     "Risk: %{y:.1f}%",]
                    )
                ))

            lpa_graph.add_trace(go.Scatter(
                x = x_lpa,
                y = y_lpa,
                line_color = 'rgb(214, 14, 14)',
                mode='lines',
                name='Risk with Lp(a)',
                hovertemplate="<br>".join(
                    ["Age: %{x}",
                     "Risk: %{y:.1f}%",]
                    )
                ))
            st.cache()

            lpa_graph.update_layout(
                    hovermode="x",
                    title_x=0.5,
                    hoverlabel=dict(
                     bgcolor="white",
                     font_size=15
                     ),
                    font = dict(size = 12),
                    xaxis_title="Age (years)",
                    yaxis_title="Risk (%)",
                    yaxis_range=[0, round(max(all_values)) + 0.5],
                    legend = dict(
                     x=0,
                     y=1,
                     traceorder ='reversed',
                     bgcolor='rgba(255, 255, 255, 0.75)',
                     font_color = 'rgb(18, 49, 135)',
                     )
                    )

            lpa_chart_placeholder.plotly_chart(lpa_graph)

            if units_lpa == "nmol/L":
                st.write(f"risk with Lp(a) value of {round(lpa, 2)} is {round(values_lpa[-1], 1)}%")
            else:
                st.write(f"risk with Lp(a) value of {round(LPA, 2)} is {round(values_lpa[-1], 1)}%")
        else:
            st.write("You must enter at least your age, sex, LDL and SBP levels to estimate your risk.")


            #st.write('Enter your Lp(a) level to see how much your Lp(a) level increases your risk of heart attack and stroke.')
            #slide = st.slider('', 0, 130, 25)
        #else:
            #st.write("You must enter your age, sex, LDL and SBP levels to estimate your risk.")
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
        #st.write('** How much more intensely should I lower my LDL or blood pressure if I have an increased risk of heart attack and stroke caused by high Lp(a)?')

    ####################################################################################

        sbpldl_chart_placeholder = st.empty()
        if SBP > 0.0 and LDL > 0.0:

            col1, col2 = st.columns(2)
            with col1:
                if units_LDL == "mmol/L":
                    ldl_dec = st.slider('How much should I lower my LDL?', 0.0, ldl, 0.0, step = 0.5)
                else:
                    LDL_DEC = st.slider('How much should I lower my LDL?', 0, LDL, 0, step = 1)
                    ldl_dec = LDL_DEC / 38.67

            with col2:
                #st.write('How much should I lower my blood pressure?')
                sbp_dec = st.slider('How much should I lower my blood pressure?', 0, 30, 0, step = 1)

            ldl_treatment = 1 if ldl_dec != 0 else 0
            sbp_treatment = 1 if sbp_dec != 0 else 0
            
            riskList_Rx = calculate(age, sex, ldl, ldl_treatment, ldl_dec * -1, age_from_ldl, age_to_ldl,
                                    hdl, SBP, sbp_treatment, sbp_dec * -1, age_from_sbp, age_to_sbp,
                                    smoke, fmr_tob, diab, BMI, famhx, None)


            print(age, sex, ldl, ldl_treatment, ldl_dec * -1, age_from_ldl, age_to_ldl,
                                    hdl, SBP, sbp_treatment, sbp_dec * -1, age_from_sbp, age_to_sbp,
                                    smoke, fmr_tob, diab, BMI, famhx, None)

            riskList_Rx = riskList_Rx[0]
            values_Rx = [num * 100 for num in riskList_Rx]

            x_Rx = ageList
            y_Rx = values_Rx

            all_values = values + values_lpa + values_Rx
            


            sbpldl_graph.add_trace(go.Scatter(
                x = x_Rx,
                y = y_Rx,
                line_color = 'rgb(14, 214, 14)',
                mode='lines',
                name='Risk after lowering LDL or blood pressure',
                hovertemplate="<br>".join(
                    ["Age: %{x}",
                     "Risk: %{y:.1f}%",]
                    )
                ))
            
            sbpldl_graph.add_trace(go.Scatter(
                x = x_base,
                y = y_base,
                line_color = 'rgb(18, 49, 135)',
                mode='lines',
                name='Risk without Lp(a)',
                hovertemplate="<br>".join(
                    ["Age: %{x}",
                     "Risk: %{y:.1f}%",]
                    )
                ))

            sbpldl_graph.add_trace(go.Scatter(
                x = x_lpa,
                y = y_lpa,
                line_color = 'rgb(214, 14, 14)',
                mode='lines',
                name='Risk with Lp(a)',
                hovertemplate="<br>".join(
                    ["Age: %{x}",
                     "Risk: %{y:.1f}%",]
                    )
                ))


            st.cache()

            sbpldl_graph.update_layout(hovermode="x",
                    title_x=0.5,
                    hoverlabel=dict(
                     bgcolor="white",
                     font_size=15
                     ),
                    font = dict(size = 12),
                    xaxis_title="Age (years)",
                    yaxis_title="Risk (%)",
                    yaxis_range=[0, round(max(all_values)) + 0.5],
                    legend = dict(
                     x=0,
                     y=1,
                     traceorder ='reversed',
                     bgcolor='rgba(255, 255, 255, 0.75)',
                     font_color = 'rgb(18, 49, 135)',
                     )
                    )

            sbpldl_chart_placeholder.plotly_chart(sbpldl_graph)

            if units_LDL == "mmol/L":
                if ldl_dec != 0:
                    st.write(f"risk lowering LDL by {ldl_dec} is {round(values_Rx[-1], 1)}%")
                if sbp_dec != 0:
                    st.write(f"risk lowering SBP by {sbp_dec} is {round(values_Rx[-1], 1)}%")
                if sbp_dec != 0 and ldl_dec != 0:
                    st.write(f"risk lowering SBP by {sbp_dec} and LDL by {ldl_dec} is {round(values_Rx[-1], 1)}%")
            else:
                if ldl_dec != 0:
                    st.write(f"risk lowering LDL by {LDL_DEC} is {round(values_Rx[-1], 1)}%")
                if sbp_dec != 0:
                    st.write(f"risk lowering SBP by {sbp_dec} is {round(values_Rx[-1], 1)}%")
                if sbp_dec != 0 and ldl_dec != 0:
                    st.write(f"risk lowering SBP by {sbp_dec} and LDL by {LDL_DEC} is {round(values_Rx[-1], 1)}%")

           
# TESTING 2 SLIDERS IN THE SAME LINE

# END OF TEST
with ref:
        st.write(' ')
        st.subheader('Further information')
        st.write('References')
