import streamlit as st

def app():
    

    
    st.write("""
    Diabetes is a chronic condition characterized by high blood sugar levels. Most commonly people affected by Type-1 or Type-2 diabetes. It can lead to serious health complications 
    such as heart disease, stroke, kidney failure, and blindness if left untreated. Recognizing the symptoms and 
    understanding the risk factors is crucial for early detection and management of diabetes.
    """)
    
    st.image("Images/Diabetes-type-2.jpg",use_column_width=True)
    # Information about the "3 P's" of diabetes
    
    st.header("Symptoms of Diabetes")
    st.write("""
    There are three main symptoms that are associated with diabetes commonly referred as 3P's. They are, Polyuria, Polydipsia, and Polyphagia. 
    """)
    # Display the information in three columns
    col1, col2, col3 = st.columns(3)

    # Information about Polyuria
    with col1:
        st.subheader("Polyuria")
        st.image("Images/polyuria.jpg", use_column_width=True)
        st.write("""
        Polyuria refers to excessive urination. It is one of the classic symptoms of diabetes and occurs when the kidneys 
        filter too much glucose from the blood, leading to increased urine production. People with diabetes may experience 
        frequent urination, especially during the night (nocturia).
        """)

    # Information about Polydipsia
    with col2:
        st.subheader("Polydipsia")
        st.image("Images/polydipsia.webp", use_column_width=True)
        st.write("""
        Polydipsia is excessive thirst. It is closely related to polyuria because the body tries to compensate for the fluid 
        lost through excessive urination by increasing the sensation of thirst. People with diabetes may have an unquenchable 
        thirst and feel the need to drink fluids frequently.
        """)

    # Information about Polyphagia
    with col3:
        st.subheader("Polyphagia")
        st.image("Images/polyphagia.webp", use_column_width=True)
        st.write("""
        Polyphagia is excessive hunger or increased appetite. Despite eating regularly, people with diabetes may still feel 
        hungry because their cells are unable to absorb glucose properly, leading to a constant feeling of hunger. This can 
        contribute to weight gain and difficulty managing blood sugar levels.
        """)
    st.write("""
        There are many other symptoms that helps us in early diagnosis of diabetes and taking measures to prevent 
             diabetes. Here they are listed below click each to know more.
        """)
    col4, col5, col6=st.columns(3)
    with col4:
        with st.expander("SUDDEN WEIGHT LOSS "):
            st.image("Images/suddenweightloss.webp", use_column_width=True)
            st.write("""
            Losing weight without trying, despite maintaining regular eating habits, often due to the body's inability to properly utilize glucose for energy, resulting in the breakdown of muscle and fat tissues for fuel.
            """)

    # Information about Polydipsia
    with col5:
        with st.expander("WEAKNESS "):
            st.image("Images/weakness.webp", use_column_width=True)
            st.write("""
            Feeling unusually tired or weak, which may be caused by fluctuations in blood sugar levels and the body's inability to effectively transport glucose to cells for energy.
            """)

    # Information about Polyphagia
    with col6:
        with st.expander("GENITAL THRUSH "):
            st.image("Images/genital thrush.webp", use_column_width=True)
            st.write("""
            Developing recurrent yeast infections, particularly in the genital area, due to the excess sugar in the urine providing an ideal environment for yeast to grow.
            """)
    st.markdown("""---""")
    col7, col8, col9=st.columns(3)
    with col7:
        with st.expander("VISUAL BLURRING "):
            st.image("Images/sight.webp", use_column_width=True)
            st.write("""
             Experiencing blurred or distorted vision as high levels of blood glucose can affect the shape and function of the lens in the eye, leading to changes in vision.
            """)

    # Information about Polydipsia
    with col8:
        with st.expander("ITCHING "):
            st.image("Images/itching.webp", use_column_width=True)
            st.write("""
            Experiencing itching or irritation in the genital area, often due to yeast infections caused by the overgrowth of Candida fungus fueled by high blood sugar levels.
            """)

    # Information about Polyphagia
    with col9:
        with st.expander("IRRITABILITY "):
            st.image("Images/irritability.webp", use_column_width=True)
            st.write("""
            Experiencing mood swings, irritability, or difficulty concentrating, which may be attributed to fluctuations in blood sugar levels affecting brain function and mood regulation.
            """)
    st.markdown("""---""")
    col10, col11, col12=st.columns(3)
    with col10:
        with st.expander("DELAYED HEALING "):
            st.image("Images/delayed healing.webp", use_column_width=True)
            st.write("""
             Noticing wounds or sores taking longer to heal than usual, as high blood sugar levels can impair the body's ability to repair damaged tissue and fight infections.
            """)

    # Information about Polydipsia
    with col11:
        with st.expander("PARTIAL PARESIS  "):
            st.image("Images/partialparesis.webp", use_column_width=True)
            st.write("""
             Experiencing numbness, tingling, or pain, particularly in the hands and feet, due to nerve damage (neuropathy) caused by prolonged exposure to high levels of glucose in the bloodstream.
            """)

    # Information about Polyphagia
    with col12:
        with st.expander("MUSCLE STIFFNESS "):
            st.image("Images/musclestiffness.webp", use_column_width=True)
            st.write("""
            Feeling stiffness or cramping in the muscles, which may be caused by dehydration or electrolyte imbalances resulting from frequent urination and loss of fluids.
            """)
    st.markdown("""---""")
    col13, col14=st.columns(2)
    with col13:
        with st.expander("ALOPECIA (HAIR LOSS)  "):
            st.image("Images/hairloss.webp", use_column_width=True)
            st.write("""
              Experiencing hair thinning or loss, particularly on the scalp or other parts of the body, which may be attributed to poor circulation or changes in hormone levels associated with diabetes.
            """)

    # Information about Polydipsia
    with col14:
        with st.expander("OBESITY "):
            st.image("Images/obesity.webp", use_column_width=True)
            st.write("""
             Being overweight or obese, particularly with excess abdominal fat, increases the risk of developing type 2 diabetes by causing insulin resistance and impairing glucose metabolism.
            """)
    st.markdown("""---""")
    st.markdown("""It's important to note that while these symptoms are commonly associated with diabetes, they may also indicate other health conditions. It's essential to consult a healthcare professional for proper diagnosis and treatment.""")
    
    html_temp = """
        <div style="background-color:#0278ae;padding:6px">
        <h4 style="color:white;text-align:center;">CHECK YOUR HEALTH BY CREATING ACCOUNT</h2>
        </div>
        <br>
        """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    