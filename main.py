import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("photo.png")

with col2:
    st.title("Chen Xu")
    content = """
    Hello, I'm Chen and currently on the exciting journey of pursuing my undergraduate degree as a software engineer. 
    My passion for the world of technology has led me to explore the captivating realm of game development. 
    In my private life, I've immersed myself in the intricate and thrilling process of creating games using Unity.
    """

    st.info(content)
