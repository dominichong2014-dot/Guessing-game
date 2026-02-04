import streamlit as st
from PIL import Image
st.write("20초")
st.write("뭔지 마춰보세요")
image = Image.open("")
st.image(image, caption="마춰보세요")
st.button("다음")
