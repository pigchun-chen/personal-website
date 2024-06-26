import streamlit as st

st.header("Contact US")

with st.form(key="email_forms"):
    user_email = st.text_input("Your email address")

    message = st.text_area("Your message here")

    button = st.form_submit_button()

    if button:
        print("I was pressed!")
