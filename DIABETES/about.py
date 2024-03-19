import streamlit as st
import mysql.connector

# Function to establish connection with MySQL database
def connect_to_database():
    try:
        conn = mysql.connector.connect(
            host="sql6.freesqldatabase.com",
            user="sql6692414",
            password="CEGc955PeB",
            database="sql6692414"
        )
        return conn
    except mysql.connector.Error as e:
        st.error(f"Error connecting to MySQL database: {e}")
        return None

# Function to fetch number of registered users
def get_registered_users(cursor):
    try:
        cursor.execute("SELECT COUNT(*) FROM patienttable")
        num_users = cursor.fetchone()[0]
        return num_users
    except mysql.connector.Error as e:
        st.error(f"Error fetching number of registered users: {e}")
        return None

# Function to fetch number of reports generated
def get_reports_generated(cursor):
    try:
        cursor.execute("SELECT COUNT(*) FROM patientsdata")
        num_reports = cursor.fetchone()[0]
        return num_reports
    except mysql.connector.Error as e:
        st.error(f"Error fetching number of reports generated: {e}")
        return None

# Main function to display about page
def app():
    # Connect to the database
    conn = connect_to_database()
    if conn:
        cursor = conn.cursor()

        
        num_users = get_registered_users(cursor)
        num_reports = get_reports_generated(cursor)
        
        # Display statistics in two columns
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("OUR USERS")
            if num_users is not None:
                st.markdown(f"<h2 style='color: #FF5733;'>{num_users}</h2>", unsafe_allow_html=True)
            else:
                st.write("Data unavailable")

        with col2:
            st.subheader("RESULTS PREDICTED")
            if num_reports is not None:
                st.markdown(f"<h2 style='color: #33FF77;'>{num_reports}</h2>", unsafe_allow_html=True)
            else:
                st.write("Data unavailable")
        
        # Close cursor and connection
        cursor.close()
        conn.close()
    html_temp = """
        <div style="background-color:#0276ae;padding:5px">
        <h4 style="color:white;text-align:center;">TEAM MEMEBRS</h2>
        </div>
        <br>
        """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    st.write(" SHAIK AFSANA  20731A3102")
    st.write(" A PAVANI  20731A3105")
    st.write(" E NANI  20731A3115")
    st.write(" U UDAY  20731A3152")
    


