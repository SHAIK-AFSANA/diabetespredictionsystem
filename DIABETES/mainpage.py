import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import home, account, contact, about
st.set_page_config(
        page_title="Diabetes Awareness",
        page_icon=":hospital:",
          # Adjust layout to make the page wider
    )
st.markdown("<style> ul {display: none;} </style>", unsafe_allow_html=True)
class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        
        html_temp = """
        <div style="background-color:#0278ae;padding:10px">
        <h1 style="color:white;text-align:center;">DIABETES PREDICTOR</h2>
        </div>
        <br>
        """
        st.markdown(html_temp, unsafe_allow_html=True)

        with st.sidebar:
            image = Image.open("Images/world-diabetes-day-elements-png.webp")
            new_image = image.resize((600, 400))
            st.image(new_image)
        with st.sidebar:      
            app = option_menu(
    menu_title='PREDIAB ',
    options=['Main','Account','Contact','About'],
    icons=['house-fill','person-circle','chat-fill','info-circle-fill'],
    menu_icon='chat-text-fill',
    default_index=0,
    styles={
        "container": {"padding": "5px", "background-color": "black"},
        "icon": {"color": "white", "font-size": "23px"},
        "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px", "--hover-color": "blue"},
        "nav-link-selected": {"background-color": "#02ab21"},
        "menu-title": {"color": "white", "font-size": "20px", "font-weight": "bold", "text-align": "center"}
    }
)
    

        
        if app == "Main":
            home.app()
        if app == "Account":
            account.app()            
        if app == 'Contact':
            contact.app()
        if app == 'About':
            about.app()    
             
          
             
    run()            
         