import mysql.connector
import streamlit as st

# Establish connection to MySQL database
mydb = mysql.connector.connect(
    host="sql6.freesqldatabase.com",
    user="sql6692414",
    password="CEGc955PeB",
    database="sql6692414"
    
)
mycursor = mydb.cursor()
print("connection established")

# Function to create account for patients
def create_account(name, email, password):
    if not name or not email or not password:
        return "Please enter all fields"
    try:
        sql = "INSERT INTO patienttable (name, email, password) VALUES (%s, %s, %s)"
        val = (name, email, password)
        mycursor.execute(sql, val)
        mydb.commit()
        user_id = mycursor.lastrowid  # Get the ID of the newly inserted row
        return user_id
    except Exception as e:
        print("Error creating account:", e)
        return False

# Function to validate login credentials for patients
def login(email, password):
    if not email or not password:
        return "Please enter all fields"
    sql = "SELECT * FROM patienttable WHERE email = %s AND password = %s"
    val = (email, password)
    mycursor.execute(sql, val)
    result = mycursor.fetchone()
    if result:
        return result  # Return user details if login successful
    else:
        return "Invalid email or password"

def app():
    no_sidebar_style = """
    <style>
        div[data-testid="stSidebarNav"] {display: none;}
    </style>
    """
    st.markdown(no_sidebar_style, unsafe_allow_html=True)

    # Check if user is logged in
    if "user_logged_in" not in st.session_state:
        st.session_state.user_logged_in = False

    # If user is already logged in, display user details and options
    if st.session_state.user_logged_in:
        user_details = st.session_state.user_details
        st.write(f"Welcome, {user_details['name']}")
        st.write(f"Email: {user_details['email']}")
        if st.button("Go to My Account"):
            st.write("Redirecting to patient page...")
            st.switch_page("pages/patient.py")
        if st.button("Logout"):
            st.session_state.user_logged_in = False
            st.write("Logged out successfully")
            st.button("Login Again")  # Button to allow users to log in again

    else:
        # Dropdown menu for selecting Login or Signup
        option = st.selectbox('Select Option', ['Login', 'Sign up'])

        # Login form
        if option == "Login":
            st.subheader("Login")
            login_email = st.text_input("Email")
            login_password = st.text_input("Password", type="password")
            if st.button("Login"):
                result = login(login_email, login_password)
                if isinstance(result, tuple):
                    user_details = {'id': result[0], 'name': result[1], 'email': result[2]}
                    st.session_state.user_logged_in = True
                    st.session_state.user_details = user_details
                    st.success("Login successful")
                    st.switch_page("pages/patient.py")
                else:
                    st.error(result)

        # Signup form
        elif option == "Sign up":
            st.subheader("Signup")
            name = st.text_input("Name")
            email = st.text_input("Email")
            password = st.text_input("Password", type="password")
            if st.button("Register"):
                result = create_account(name, email, password)
                if isinstance(result, int):
                    user_details = {'id': result, 'name': name, 'email': email}
                    st.session_state.user_logged_in = True
                    st.session_state.user_details = user_details
                    st.success("Account created successfully")
                    st.switch_page("pages/patient.py")
                else:
                    st.error(result)
