import pandas
import streamlit as st

st.set_page_config(layout="wide")

col1, col2, col3 = st.columns(3)

container1 = st.container()


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

with container1:
    content = """
    feel free to contact me, if you are needed
    """

    st.write(content)

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
