import streamlit as st
from streamlit_option_menu import option_menu
import pages.patient_reports
st.set_page_config(initial_sidebar_state="collapsed",layout="wide")
st.markdown("<style> ul {display: none;} </style>", unsafe_allow_html=True)
import pages.patient_health
def runpatient():
    app = option_menu('WELCOME',
                            ['MY HEALTH','MY REPORTS'],
                            icons = ['heart','report'],
                            menu_icon="cast",
                            default_index =0,
                            orientation="horizontal",
                            styles={
                            "container":{"padding":"0!important","background-color":"#ffffff80"},
                            "icon":{"color":"black","font-size":"20px"},
                            "nav-link":{"font-size":"15px","text_align":"left",
                                        "margin":"0px","--hover-color":"#eee",
                            },"nav-link-selected":{"background-color":"#50ABE7"},})
    

    if app == "MY HEALTH":
        pages.patient_health.patient_page()         
    if app == 'MY REPORTS':
        pages.patient_reports.app()
    if app == 'MY PROFILE':
        pass
    
runpatient()
