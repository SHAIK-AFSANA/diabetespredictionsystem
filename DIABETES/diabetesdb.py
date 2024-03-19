import mysql.connector

# Establish connection to MySQL database
db_connection = mysql.connector.connect(
    host="sql6.freesqldatabase.com",
    user="sql6692414",
    password="CEGc955PeB",
    database="sql6692414"
)

# Create cursor
cursor = db_connection.cursor()

# Execute SQL command to create patienttable
cursor.execute("""
CREATE TABLE patienttable (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
)
""")

# Execute SQL command to create patientsdata with foreign key constraint
cursor.execute("""
CREATE TABLE patientsdata (
    id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT,
    age INT NOT NULL,
    gender ENUM('Male', 'Female') NOT NULL,
    Polyuria ENUM('Yes', 'No') NOT NULL,
    Polydipsia ENUM('Yes', 'No') NOT NULL,
    Sudden_Weight_Loss ENUM('Yes', 'No') NOT NULL,
    Weakness ENUM('Yes', 'No') NOT NULL,
    Polyphagia ENUM('Yes', 'No') NOT NULL,
    Genital_Thrush ENUM('Yes', 'No') NOT NULL,
    Visual_Blurring ENUM('Yes', 'No') NOT NULL,
    Itching ENUM('Yes', 'No') NOT NULL,
    Irritability ENUM('Yes', 'No') NOT NULL,
    Delayed_Healing ENUM('Yes', 'No') NOT NULL,
    Partial_Paresis ENUM('Yes', 'No') NOT NULL,
    Muscle_Stiffness ENUM('Yes', 'No') NOT NULL,
    Alopecia ENUM('Yes', 'No') NOT NULL,
    Obesity ENUM('Yes', 'No') NOT NULL,
    Prediction VARCHAR(8),
    FOREIGN KEY (patient_id) REFERENCES patienttable(id)          
)
""")

# Commit changes and close cursor
db_connection.commit()
cursor.close()

# Close database connection
db_connection.close()
