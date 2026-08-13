import streamlit as st

# 1. 初始化購物籃清單 (如果還不存在，就建立一個空的 List)
if "cart" not in st.session_state:
    st.session_state.cart = []

# 2. 最上面的重新整理鍵
if st.button("重新整理"):
    st.rerun()

# 3. 標題：點餐機
st.title("點餐機")

# 4. 輸入餐點與加入按鈕
# 使用 st.columns 將輸入框與按鈕放在同一行
col1, col2 = st.columns([3, 1])

with col1:
    item_input = st.text_input("請輸入餐點", key="food_input", label_visibility="visible")

with col2:
    # 增加一點上方邊距讓按鈕與輸入框對齊
    st.write("") 
    st.write("")
    if st.button("加入"):
        if item_input.strip():  # 確保輸入不是空白
            # 使用學到的 append 將餐點加入 List 最後面
            st.session_state.cart.append(item_input)
            st.rerun()  # 重新整理頁面以更新列表

# 5. 購物籃列表區塊
st.subheader("購物籃")  # 購物籃列表的小標題


    # 使用學到的 range 與 len() 走訪 List 中的每一個元素與 index
for i in range(len(st.session_state.cart)):
        c1, c2 = st.columns([4, 1])
        
        with c1:
            # 讀取 List 中的餐點名稱
            st.write(f" {st.session_state.cart[i]}")
            
        with c2:
            # 為每個項目建立一個刪除按鈕 (按鈕 key 必須唯一)
            if st.button("刪除", key=f"del_{i}"):
                # 使用學到的 pop(index) 移除指定位置的元素
                st.session_state.cart.pop(i)
                st.rerun()