import streamlit as st

st.title("欄位元件")
col1, col2 = st.columns(2)
col1.button("按鈕1", key="btn1") # 在col1中建立一個按鈕類似st.button("按鈕1")
col2.button("按鈕2", key="btn2") # 在col2中建立一個按鈕類似st.button("按鈕2")

# 2columns, 可以用比例來設定每個column的寬度，將比例放到list中
col1, col2 = st.columns([1, 2])
col1.button("按鈕1", key="btn3") # 在col1中建立一個按鈕類似st.button("按鈕1")
col2.button("按鈕2", key="btn4") # 在col2中建立一個按鈕類似st.button("按鈕2")

# 3columns
col1, col2 ,col3= st.columns([1, 2, 3])
col1.button("按鈕1", key="btn5") # 在col1中建立一個按鈕類似st.button("按鈕1")
col2.button("按鈕2", key="btn6") # 在col2中建立一個按鈕類似st.button("按鈕2")
col3.button("按鈕3", key="btn7") # 在col3中建立一個按鈕類似st.button("按鈕3")

# 多個columns可以使用for迴圈來建立
cols = st.columns(4)  # 4columns, cols[0]...cols[3]
for i in range(len(cols)):
    with cols[i]:
        st.button(f"按鈕{i+1}", key=f"btn{i+10}")  # 在cols[i]中建立一個按鈕類似
    # st.balloons()  # 在cols[i]中建立一個氣球
col1, col2 = st.columns([1, 2])
with col1:  # 在col1使用 with 語句放更多東西
    if st.button("按鈕1", key="btn8"):  # 在col1中建立一個按鈕
        st.balloons()  # 在col1中建立一個氣球
    st.write("這是col1")  # 在col1中建立一個文字
with col2:  # 在col2使用 with 語句放更多東西
    st.button("按鈕2", key="btn9")  # 在col2中建立一個按鈕
    st.write("這是col2")  # 在col2中建立一個文字
st.write("---")
st.write("coiumns排列元見效果比較")
# 2columns
col1, col2, = st.columns(2)
with col1:
    st.button("按鈕1", key="1")
    st.button("按鈕2", key="2")
    st.button("按鈕3", key="3")
with col2:
    st.write("這是col2")
    st.write("這是col2")
    st.write("這是col2")

st.write("---")

for i in range(3):
    col1, col2 = st.columns(2)
    with col1:
        st.button(f"按鈕{i+1}",key=f"{i+4}")
    with col2:
        st.write(f"這是col2_{i+1}")


st.write("---")
st.title("文字輸入元件")
# st text_input指令格式 st.text_input(輸入欄位的標題，value="預設顯示文字")
text = st.text_input("請輸入文字",value="這是預設文字")
st.write(f"你輸入的文字是:{text}")

# session_state

if "ans1" not in st.session_state: #如果session_state中沒有ans這個變數
    st.session_state.ans1 = 1 # 設定session_state = 1

if st.button("按下去ans+1", key="ans2"): # 如果按下按鈕
        st.session_state.ans1 = st.session_state.ans1+1 # st.session_state.ans+1
st.write(f"ans={st.session_state.ans1}") # 顯示session_state.ans的值


if "apple" not in st.session_state: # 如果session_state中沒有apple這個變數
    st.session_state.apple = 1 # 設定session_state=1
# 有時候按鈕按下，不一定會重新整理整個畫面
# 這時候可以使用st.rerun()強制重新整理畫面
if st.button("重新整理畫面", key = "banana"): # 如果按下按鈕
    # .....
    st.rerun() # 重新執行程式