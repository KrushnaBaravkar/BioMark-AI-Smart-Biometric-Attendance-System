import streamlit as st  
from src.ui.base_layout import style_background_dashbord, style_base_layout
from src.components.header_home import header_dashboard

def teacher_screen():
    # st.header("Teacher screen")

    style_background_dashbord()
    style_base_layout()

    if st.session_state['login_type'] == 'teacher_login':
        teacher_screen_login()
    elif st.session_state['login_type'] == 'teacher_register':
        teacher_screen_register()
    

def teacher_screen_register():
    col1, col2 = st.columns(2, vertical_alignment="center", gap="large")

    with col1:
        header_dashboard()

    with col2:
        if st.button("Go back to Home", type="secondary", key="loginbackbtn", shortcut="control + backspace"):
            st.session_state['login_type'] = None
            st.rerun

    # st.header("Register your teacher profile")
    st.markdown(
        """
        <h2 style='text-align:center; color:#1A1A1A'>
            Register your teacher profile
        </h2>
        """,
        unsafe_allow_html=True
    )

    # adding space between header and the input boxes
    st.space()
    st.space()
    teacher_name = st.text_input("Enter name", placeholder="Gana")
    teacher_username = st.text_input("Enter username", placeholder="Jay_ganesh")
    teacher_pass = st.text_input("Enter passwerd", type="password", placeholder="Enter passward")
    teacher_pass = st.text_input("Conform passwerd", type="password", placeholder="conform passward")

    st.divider() # add horizontal line to seperate things 

    col1, col2 = st.columns(2, vertical_alignment="center", gap="large")
    with col1:
        but1 = st.button("Register", icon=":material/passkey:", shortcut="control+enter", width="stretch")
        # what to check the entered both the passwards are same or not. 
    with col2:
        if st.button("Login Insted", icon=":material/passkey:", type="primary", width="stretch"):
            st.session_state['login_type'] = 'teacher_login'
            st.rerun



def teacher_screen_login():
    col1, col2 = st.columns(2, vertical_alignment="center", gap="large")

    with col1:
        header_dashboard()

    with col2:
        if st.button("Go back to Home", type="secondary", key="loginbackbtn", shortcut="control + backspace"):
            st.session_state['login_type'] = None
            st.rerun
    # st.header("Register your teacher profile")
    st.markdown(
        """
        <h2 style='text-align:center; color:#1A1A1A'>
            Login your profile
        </h2>
        """,
        unsafe_allow_html=True
    )
    
    # adding space between header and the input boxes
    st.space()
    st.space()
    teacher_username = st.text_input("Enter your registered username", placeholder="Jay_ganesh")
    teacher_pass = st.text_input("Enter passwerd", type="password", placeholder="Enter passward")

    st.divider() # add horizontal line to seperate things 

    col1, col2 = st.columns(2, vertical_alignment="center", gap="large")
    with col1:
        but1 = st.button("Login Account", icon=":material/passkey:", shortcut="control+enter", width="stretch")
    with col2:
        if st.button("Register Insted", icon=":material/passkey:", type="primary", width="stretch"):
            st.session_state['login_type'] = 'teacher_register'
            st.rerun
