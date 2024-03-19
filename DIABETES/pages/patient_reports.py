import mysql.connector
import streamlit as st
import pandas as pd
import base64
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
import os
# Establish connection to MySQL database
mydb = mysql.connector.connect(
    host="sql6.freesqldatabase.com",
    user="sql6692414",
    password="CEGc955PeB",
    database="sql6692414"
)
mycursor = mydb.cursor()

# Function to fetch patient data for the logged-in user
def fetch_patient_data(patient_id):
    sql = "SELECT * FROM patientsdata WHERE patient_id = %s"
    val = (patient_id,)
    mycursor.execute(sql, val)
    patient_data = mycursor.fetchall()
    return patient_data

def generate_report_pdf(df):
    # Function to generate PDF report
    filename = "patient_report.pdf"
    # Define columns to include in the report
    columns_to_include = ["Patient_id", "ID", "Age", "Gender", "Symptoms", "prediction"]
    # Select only the columns to include in the report
    truncated_df = df[columns_to_include]
    # Calculate the width of each column based on the number of columns
    col_widths = [100] * len(truncated_df.columns)
    # Create a PDF document
    doc = SimpleDocTemplate(filename, pagesize=letter)
    # Define data for the table
    data = [truncated_df.columns.tolist()] + truncated_df.values.tolist()
    # Create a table with adjusted column widths
    table = Table(data, colWidths=col_widths)
    # Add style to the table
    style = TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # Vertically align the values in the middle of each cell
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('GRID', (0, 0), (-1, -1), 1, colors.black)
])
    table.setStyle(style)
    # Add the table to the PDF document
    doc.build([table])
    return filename
def app():
    no_sidebar_style = """
    <style>
        div[data-testid="stSidebarNav"] {display: none;}
    </style>
    """
    st.markdown(no_sidebar_style, unsafe_allow_html=True)

    # Check if user is logged in
    if "user_logged_in" not in st.session_state or not st.session_state.user_logged_in:
        st.error("You must be logged in to view your patient data.")
        return

    # Fetch patient data for the logged-in user
    patient_id = st.session_state.user_details['id']
    patient_data = fetch_patient_data(patient_id)

    # Display patient data in a table
    st.subheader("Generate Your Reports - Click On Generate")
    if not patient_data:
        st.write("No patient data found.")
    else:
        # Convert patient data to DataFrame
        df = pd.DataFrame(patient_data, columns=["ID", "Patient_id","Age", "Gender", "Polyuria", "Polydipsia", 
                                                 "Sudden_Weight_Loss", "Weakness", "Polyphagia", 
                                                 "Genital_Thrush", "Visual_Blurring", "Itching", 
                                                 "Irritability", "Delayed_Healing", "Partial_Paresis", 
                                                 "Muscle_Stiffness", "Alopecia", "Obesity", "prediction"])

        # Check if 'Symptoms' column is present in DataFrame
        if 'Symptoms' not in df.columns:
            # Filter for columns with 'Yes' values and concatenate them
            symptom_columns = [col for col in df.columns if df[col].eq('Yes').any()]
            df['Symptoms'] = df[symptom_columns].apply(lambda row: '\n '.join(row.index[row == 'Yes']), axis=1)

        # Display the DataFrame
        st.dataframe(df)

        # Add a "Generate Report" column with download buttons
        # Iterate through the DataFrame rows and display buttons for each report
        # Iterate through the DataFrame rows and display buttons for each report
        # Iterate through the DataFrame rows and display buttons for each report
        
        if st.button("GENERATE"):
            filename = generate_report_pdf(df)
            with open(filename, "rb") as f:
                pdf_data = f.read()
                # Encode the file content as base64
            pdf_base64 = base64.b64encode(pdf_data).decode("utf-8")
                # Create a download link
            href = f'<a href="data:application/octet-stream;base64,{pdf_base64}" download="{filename}">Download PDF</a>'
                # Display the download link
            st.markdown(href, unsafe_allow_html=True)
                # Delete the temporary PDF file
            os.remove(filename)
        