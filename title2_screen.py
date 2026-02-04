import streamlit as st
col1, col2= st.columns([2, 2])

with col1:
    st.button("플레이")

with col2:
    st.button("리더보드")