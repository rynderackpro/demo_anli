import streamlit as st

st.title("极简计算器")
num = st.number_input("输入数字", value=0)
if st.button("平方结果"):
    st.success(f"{num}² = {num**2}")