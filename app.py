import streamlit as st
import os
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import joblib
import base64  



# st.set_option('deprecation.showPyplotGlobalUse', False)

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)
set_background('bg.jpg')


model = joblib.load('./senti_model_rf.h5')
v = joblib.load('./v.h5')

def pred(sentence):
    input = v.transform([sentence])
    y_pred = model.predict(input)
    return y_pred

bill = [980,728, 991, 999, 768]


def fake_analysis():
    st.header("Fake Review monitoring system") 
    user = (st.text_input("Enter Name: ", value=" ")).lower()
    prod = (st.text_input("Enter Product Name: ", value=" ")).lower()  

    review = st.text_area("Enter Review: ")
    n = st.number_input("Enter Bill ID no.: ", value=0, step = 1)
    rv = pred(review)

    if st.button("Check"):
        if user and prod and review and n:
            found = False
            with open("Fake-Review-Monitoring-System/customer_data.txt", "r") as file:
                for line in file:
                    
                    if (f"Name: {user.lower()}" in line and 
                        f"Product: {prod.lower()}" in line and 
                        f"Bill ID: {n}" in line):
                        found = True
                        break

            if found:
                # st.success("The review details match a record.")
                if rv[0] == 'Positive':
                    result = 'Genuine user and review'
                    st.success(result)
                else:
                    st.error(f"Genuine User but Review is {rv[0]}")
            else:
                st.error("Fake User")
        else:
            st.error("Please fill in all fields.")

def home():
    # Using Markdown to style sections within the dark theme
    st.markdown("""
        <div style="background-color: #333333; color: #FFFFFF; padding: 20px; border-radius: 8px;">
            <h1>Fake Review Analysis</h1>
            <h2>Introduction</h2>
            <p>Tasks of this project are performed in the following steps:</p>
            <ul>
                <li><strong>Email Verification</strong>: Users will be required to log in using their email for better verification purposes, ensuring the authenticity of the reviewer.</li>
                <li><strong>Feature Mining</strong>: Product features that have been commented on by customers will be extracted and analyzed to focus on key aspects that matter to users.</li>
                <li><strong>Opinion Analysis</strong>: Each review will be broken down into sentences, and the sentiment of each sentence will be analyzed to determine whether the comment is positive, negative, or neutral.</li>
                <li><strong>Fake Review Detection</strong>: If a review or comment is determined to be fake based on specific criteria, it will be flagged and removed to maintain the integrity of the review section.</li>
                <li><strong>Final Output</strong>: The result will be a refined review section with a minimum number of fake reviews, ensuring that customers get reliable and genuine feedback on products.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

def register():
    name = st.text_input("Enter Name: ")
    product = st.text_input("Enter Product Name: ")
    bill = st.number_input("Enter your Bill ID no.:", step=1)

    if st.button("Submit"):
        if not name or not product or not bill:
            st.error("Please fill in all fields.")
        else:
            with open("./customer_data.txt", "a") as file:
                file.write(f"Name: {name.lower()}, Product: {product.lower()}, Bill ID: {bill}\n")
            
            st.success("Information submitted successfully!")


    


if "radio_choice" not in st.session_state:
    st.session_state.radio_choice = "HOME"
choice = st.sidebar.radio(
    "Select an option:",
    ("HOME", "Register", "Review"),
    index=["HOME", "Register", "Review"].index(st.session_state.radio_choice)
)
st.session_state.radio_choice = choice

if choice == 'Register':
    register()
elif choice == 'HOME':
    home()
elif choice == 'Review':
    fake_analysis()
