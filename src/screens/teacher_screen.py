import streamlit as st  

def teacher_screen():
    st.header("Teacher screen")

    butt = st.button("Back")
    if butt:
        st.session_state['login_type'] = None
        st.rerun