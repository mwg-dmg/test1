import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import streamlit as st

st.title("Analyze Data")





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
    placeholder.line_chart({"data": [1, 5, 2, 6]})

elif st.session_state.page == 2:
# Replace the chart with several elements:
    with placeholder.container():
        st.write("This is one element")
        st.write("This is another")
        st.metric("Page:", value=st.session_state.page)
        
elif st.session_state.page == 3:
    placeholder.text(f"Hello, this is page {st.session_state.page}")
    url="test_y_x.csv"
    df=pd.read_csv(url)
    #print(df)

    Y=df["y"]
    X=df["x"]

    fig=plt.figure()
    plt.scatter(X,Y)
    plt.title(" X Y Plot")
    plt.xlabel("X")
    plt.ylabel("Y")

    if st.button("Show Data"):
        st.dataframe(df)
    if st.button("Show Scatter Chart"):    
        st.pyplot(fig)


else:
    with placeholder:
        st.write("This is the end")
        st.button("Restart",on_click=restart)

