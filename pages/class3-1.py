import streamlit as st

st.title('欄位元件')
col1,col2=st.columns(2) #2 columns 
col1.button('按鈕1',key='btn1')#在c o l one中建立一個按鈕類似st.button b t n one
col2.button('按鈕2',key='btn2')#在c o l two中建立一個按鈕類似st.button b t n two

# two columns,可以用比例來設定每個column的寬度，將比例放到list中
col1,col2=st.columns([1,2])
col1.button('按鈕1',key='btn3')#在c o l one中建立一個按鈕類似st.button b t n one
col2.button('按鈕2',key='btn4')#在c o l two中建立一個按鈕類似st.button b t n two

# three columns
col1,col2,col3=st.columns([1,2,3])
col1.button('按鈕1',key='btn5')#在c o l two中建立一個按鈕類似st.button b t n two
col2.button('按鈕2',key='btn7')#在c o l two中建立一個按鈕類似st.button b t n two
col3.button('按鈕3',key='btn6')#在c o l three中建立一個按鈕類似st.button b t n three

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

st.write('---')
st.title(' columns排列元件效果比較')
#2columns
col1,col2=st.columns(2)
with col1:
    st.button('按鈕1',key='1')
    st.button('按鈕2',key='2')
    st.button('按鈕3',key='3')
with col2:
    st.write('這是col2')
    st.write('這是col2')
    st.write('這是col2')


st.write('---')

for i in range(3):
    col1,col2=st.columns(2)
    with col1:
        st. button(f'按鈕{i+1}',key=f'{i+4}')
    with col2:
        st. write(f'這是col2_{i+4}')

st.write('---')
st.title('文字輸入元件')
#st.text_input指定格式 st.text_input(之前輸入欄位的標題, value='預設顯示文字')
text=st.text_input('請輸入文字',value='這是預設文字')
st.write(f'你輸入的文字是：{text}')

    



