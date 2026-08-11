import streamlit as st  #遷入streamlit並命名為st

#st.number_input()可以讓使用者輸入數字，設定step=1可以讓使用者只能輸入整數
#min_value=0可以是訂最小值為0，max_value=100可以設定最大值為100
number=st.number_input('請輸入一個數字',step=1,min_value=0,max_value=100)
#st.markdown()可以再網頁使用markdown語法顯示文字
st.markdown(f'your number is:{number}')

st.markdown('練習')
a=st.number_input('請輸入你的分數',min_value=0,max_value=100,step=1)
if a >=90:
    st.write('you are a')
elif a >=80:
    st.write('you are b')
elif a >=70:
    st.write('you are c')
elif a >=60:
    st.write('you are d')
else :
    st.write('you are a failure')

st.markdown('---')
st.markdown('### 練習')
#st.button()可以再網頁上顯示按鈕，使用者可以點及按鈕
#key式按鈕的識別名稱，用來區別按鈕
#如果使用者點及按鈕，st.button()會回傳true<否則false
st.button("click me", key='button1')
if st.button('click me', key='balloons'):
   st.balloons()
if st.button('click me', key='snow'):
   st.snow()
st.markdown('---')