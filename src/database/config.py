import streamlit as  st
from supabase import create_client, Client

# Created instance of the database to run queries on the database. 
supabase: Client = create_client(
    st.secrets["SUPABASE_URL"],
    st.secrets["SUPABASE_KEY"]
)