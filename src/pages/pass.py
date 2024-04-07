import streamlit as st
from dotenv import load_dotenv
from os import getenv

load_dotenv()
imported_pass = getenv("pass")
st.write(f"La pass es {imported_pass}")