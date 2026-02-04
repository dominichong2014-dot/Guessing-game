
import streamlit as st
from streamlit_gsheets import GSheetsConnection
from PIL import Image
import time 
import random

conn = st.connection("gsheets", type=GSheetsConnection)
url = "https://docs.google.com/spreadsheets/d/1BnCc6-q2e3sVtvv4olzPYpn3CZG1tyEBte0Xg9zPwtY/edit"
df=conn.read(spreadsheet=url).values.tolist()

# 1. 세션 상태 초기화
if 'page' not in st.session_state:
    st.session_state.page = 'username'
if 'diff' not in st.session_state:
    st.session_state.diff = '쉬움'
if 'q' not in st.session_state:
    st.session_state.q = {}
if 'l' not in st.session_state:
    st.session_state.l = 0
if 'start' not in st.session_state:
    st.session_state.start = None
if 'i' not in st.session_state:
    st.session_state.i = 0




easy=[{'img':'2.png','answer':'고양이'},
      {'img':'3.png','answer':'알파카'},
      {'img':'20.png','answer':'코뿔소'},
      {'img':'4.png','answer':'수달'},
      {'img':'5.png','answer':'고슴도치'},
      {'img':'6.png','answer':'하이에나'},
      {'img':'22.png','answer':'오리'},
      {'img':'23.png','answer':'사슴'},
      {'img':'24.png','answer':'여우'},
      {'img':'25.png','answer':'판다'},
      {'img':'26.png','answer':'원숭이'},
      {'img':'27.png','answer':'펭귄'},
      {'img':'28.png','answer':'소'},
      {'img':'29.png','answer':'말'},
      {'img':'30.png','answer':'돼지'},
      {'img':'31.png','answer':'닭'},
      {'img':'32.png','answer':'양'},
      {'img':'33.png','answer':'염소'},
      {'img':'34.png','answer':'다람쥐'},
      {'img':'35.png','answer':'햄스터'},
      {'img':'36.png','answer':'금붕어'},
      {'img':'37.png','answer':'거북이'},
      {'img':'38.png','answer':'앵무새'},
      {'img':'39.png','answer':'백조'},
      {'img':'40.png','answer':'기린'},
      {'img':'41.png','answer':'코끼리'},
      {'img':'42.png','answer':'물개'},
      {'img':'43.png','answer':'병아리'},
      {'img':'44.png','answer':'두더지'},
      {'img':'45.png','answer':'청설모'},
      {'img':'46.png','answer':'비둘기'},
      {'img':'47.png','answer':'까치'},
      {'img':'48.png','answer':'고라니'},
      {'img':'49.png','answer':'개구리'},
      {'img':'50.png','answer':'도마뱀'},
      {'img':'51.png','answer':'나비'},
      {'img':'52.png','answer':'메뚜기'},
      ]

normal=[{'img':'7.png','answer':'나무보아'},
        {'img':'21.png','answer':'타조'},
        {'img':'8.png','answer':'개미핥기'},
        {'img':'9.png','answer':'코알라'},
        {'img':'10.png','answer':'아르마딜로'},
        {'img':'11.png','answer':'태양곰'},
        {'img':'12.png','answer':'가오리'}]

 
hard=[{'img':'.png','answer':'물곰'},
      {'img':'.png','answer':'쿼카'},
      {'img':'15.png','answer':'바위너구리'},
      {'img':'16.png','answer':'레드판다'},
      {'img':'17.png','answer':'설표'},
      {'img':'18.png','answer':'사올라'},
      {'img':'19.png','answer':'말레이맥'}]

name={'쉬움':easy,'보통':normal,'어려움':hard}

# 2. 페이지별 화면 구성
if st.session_state.page == 'username':
    name = st.text_input("이름을 입력하세요")
    st.write(f"입력된 이름: {name}")
    if st.button("다음"):
        df.append([name,0])
        q=conn.update(data=df)
        st.session_state.page = '타이털 스크린'
        st.rerun()

elif st.session_state.page == '타이털 스크린':
    col1, col2= st.columns([2, 2])

    with col1:
        if st.button("플레이"):
            st.session_state.page = '난이도'
            st.rerun() 

    with col2:
        if st.button("리더보드"):
            st.session_state.page = ''
            st.rerun() 


elif st.session_state.page == '난이도':
    diff=st.select_slider("난이도 를 선택 하세요", ["쉬움", "보통", "어려움"])
    if st.button("다음"):
        st.session_state.diff = diff
        st.session_state.q=random.choice(name[st.session_state.diff])
        st.session_state.page = '게임'
        st.session_state.start = time.time()
        st.rerun()

elif st.session_state.page == '게임':
    limit_time = 20
    st.write(st.session_state.i)
    elapsed_time = time.time() - st.session_state.start
    remaning_time = int(limit_time - elapsed_time)
    if remaning_time <= 0:
        st.session_state.page = "게임 오버"
        st.rerun()

    # st.title("게임")
    # st.subheader("남은시간={}".format(remaning_time))
    # st.write("뭔지 마춰보세요")
    st.write(remaning_time)
    image = Image.open(st.session_state.q['img'])
    name = st.text_input("이름을 입력하세요")
    st.image(image, caption="마춰보세요")

    if st.button("다음"):
        st.session_state.start = time.time()
        st.session_state.i+=1
        if  name == st.session_state.q['answer']:
            st.session_state.page = '답 스크린'
            st.rerun()
        else:
            st.session_state.page = '게임 오버'
            st.rerun()

    time.sleep(1)
    st.rerun()

    

elif st.session_state.page == '게임 오버':
    st.write(st.session_state.i)
    st.title("게임 오버")
    if st.button("홈화면"):
        st.session_state.page = '타이털 스크린'
        st.rerun()

elif st.session_state.page == '답 스크린':
    st.title(st.session_state.q['answer'])
    if st.button("다음"):
        st.session_state.page = '게임'
        st.session_state.q=random.choice(name[st.session_state.diff])
        st.session_state.start = time.time()
        st.rerun()