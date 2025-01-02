import streamlit as st
from streamlit_option_menu import option_menu

st.title("My own project")
# st.sidebar.header("My sidebar")
# st.sidebar.text_input("Enter your name: ")
st.header("Abstraction")
st.write("- Para bidgciuxcozh")
st.write("_Para bidgciuxcozh_")
st.code('''
def fun():
    print("Welcome to GFG")   
fun() 
''',language="python")

name = st.text_input("Name")
email = st.text_input("Email")
if st.button("Submit"):
    st.write(name,email)
    st.success("Data inserted successfully")
    st.balloons()

col1,col2=st.columns(2)
with col1:
    st.text_input("Phone number:")
with col2:
    st.text_input("State: ")
st.button("Register")


with st.sidebar:
    selected = option_menu(
        menu_title="Python_Editorial",
        options=["Abstract","Company profile","System analysis","System requirements"],

    )