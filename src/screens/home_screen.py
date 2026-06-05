import streamlit as st  
from src.components.header_home import header_home
from src.ui.base_layout import style_base_layout, style_background_home, style_background_dashbord

def home_screen():
    # st.header("Home screen")
    
    header_home()       # setting header
    
    style_background_home()     # overriding the basic layout of the streamlit
    style_base_layout()
    
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            "<h2 style='color:#1A1A1A;'>I'm Student</h2>",
            unsafe_allow_html=True
        )
        st.image("https://i.ibb.co/844D9Lrt/mascot-student.png", width=120)
        if st.button('Student Portal', type='primary'):
            st.session_state['login_type'] = 'student'
            st.rerun()

    with col2:
        st.markdown(
            "<h2 style='color:#1A1A1A;'>I'm Teacher</h2>",
            unsafe_allow_html=True
        )
        st.image("https://i.ibb.co/CsmQQV6X/mascot-prof.png", width=145)
        if st.button('Teacher Portal', type='primary'):
            st.session_state['login_type'] = 'teacher_login'
            st.rerun()