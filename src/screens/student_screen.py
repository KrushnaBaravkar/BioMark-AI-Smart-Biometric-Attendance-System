import streamlit as st  

def student_screen():
    st.header("Student screen")

    butt = st.button("Back")
    if butt:
        st.session_state['login_type'] = None
        st.rerun
