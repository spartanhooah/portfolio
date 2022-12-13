import streamlit as st
import pandas

st.set_page_config(layout="wide")


def create_row(row):
    st.header(row["title"])
    st.write(row["description"])
    st.image(f"images/{row['image']}")
    st.write(f"[Source Code]({row['url']})")


column1, column2 = st.columns(2)

with column1:
    st.image("images/photo.jpg", width=600)

with column2:
    st.title("Ben Frey")
    content = """
    I am a Java developer with experience in Spring Boot APIs and Spock testing.
    I graduated in 2016 with a Master of Science in Computer Science 
    from Michigan State University.
    """
    st.info(content)

st.write("Below you can find some of the apps I have built in Python. Feel free to contact me!")

column3, empty, column4 = st.columns([1.5, 0.5, 1.5])

data = pandas.read_csv("data.csv", sep=";")


for index, row in data.iterrows():
    if index % 2:
        with column3:
            create_row(row)
    else:
        with column4:
            create_row(row)
