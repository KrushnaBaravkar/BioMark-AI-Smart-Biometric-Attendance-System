import streamlit as st

def main():

    st.header("This is my page")
    name = st.text_input("Enter your name : ")

    col1, col2 = st.columns(2)

    with col1:
        if st.button('Hi', type='primary', key='btn1', width='stretch'):
            print('hi', name)

    with col2:
        if st.button('Bye', type='secondary', key='btn2', width='stretch'):
            print('bye', name)

    st.markdown("""
        <style>
                button{
                    background:orange !important;
                }
                <style>
    """, unsafe_allow_html=True)
main()