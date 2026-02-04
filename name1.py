import streamlit as st
name = st.text_input("이름을 입력하세요")
st.write(f"입력된 이름: {name}")