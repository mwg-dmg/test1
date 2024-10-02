import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import streamlit as st

st.title("Analyze Interactive Data")

if "page" not in st.session_state:
    st.session_state.page = 0

def nextpage(): st.session_state.page += 1
def restart(): st.session_state.page = 0

placeholder = st.empty()
st.button("Next",on_click=nextpage,disabled=(st.session_state.page > 3))

if st.session_state.page == 0:
    # Replace the placeholder with some text:
    placeholder.text(f"Hello, this is page {st.session_state.page}")

elif st.session_state.page == 1:
    # Replace the text with a chart:
     placeholder.text(f"Hello, this is page {st.session_state.page}")

elif st.session_state.page == 2:
# Replace the chart with several elements:
    with placeholder.container():
        st.write("This is one element")
        st.write("This is another")
        st.metric("Page:", value=st.session_state.page)
        
elif st.session_state.page == 3:
    placeholder.text(f"Hello, this is page {st.session_state.page}")
   
   


else:
    with placeholder:
        st.write("This is the end")
        st.button("Restart",on_click=restart)




