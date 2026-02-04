import streamlit as st
first_page=st.Page("name1.py",title="login",default=True,icon=":app/first")
second_page=st.Page("title2_screen.py",title="title screen",icon=":app/second")
third_page=st.Page("difficulty3.py",title="difficulty chose",icon=":app/third")
fourth_page=st.Page("game4.py",title="game",icon=":app/fourth")
fifth_page=st.Page("points5.py",title="final score",icon=":app/fifth")
pg = st.navigation([first_page,second_page,third_page,fourth_page,fifth_page])
pg.run()