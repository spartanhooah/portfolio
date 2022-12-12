import streamlit as st

st.set_page_config(layout="wide")

column1, column2 = st.columns(2)

with column1:
    st.image("images/photo.jpg")

with column2:
    st.title("Ben Frey")
    content = """
    I am a Java developer with experience in Spring Boot APIs and Spock testing.
    I graduated in 2016 with a Master of Science in Computer Science 
    from Michigan State University.
    """
    st.info(content)

st.write("Below you can find some of the apps I have built in Python. Feel free to contact me!")
