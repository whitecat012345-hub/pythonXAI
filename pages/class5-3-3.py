import streamlit as st
import os

st.title("購物平臺")

# 初始化商品資料
if "products" not in st.session_state:
    st.session_state.products = {
        "apple": {
            "name": "蘋果",
            "price": 10,
            "stock": 10,
            "image": "image/apple.png"
        },
        "banana": {
            "name": "香蕉",
            "price": 10,
            "stock": 10,
            "image": "image/banana.png"
        },
        "bg": {
            "name": "bg",
            "price": 10,
            "stock": 10,
            "image": "image/bg.png"
        },
        "orange": {
            "name": "橘子",
            "price": 10,
            "stock": 10,
            "image": "image/orange.png"
        }
    }

# 欄位數輸入
column_num = st.number_input("請輸入欄位數", min_value=1, max_value=5, value=4, step=1)

# 顯示商品
product_keys = list(st.session_state.products.keys())
cols = st.columns(column_num)

for i, key in enumerate(product_keys):
    product = st.session_state.products[key]
    with cols[i % column_num]:
        if os.path.exists(product["image"]):
            st.image(product["image"], width=150)
        else:
            st.write("找不到圖片")
        
        st.subheader(product["name"])
        st.write(f"價錢：{product['price']}")
        st.write(f"庫存：{product['stock']}")
        
        if st.button(f"購買{product['name']}", key=f"buy_{key}"):
            if product["stock"] > 0:
                st.session_state.products[key]["stock"] -= 1
                st.success(f"你已購買 {product['name']} 1 個")
            else:
                st.error(f"{product['name']} 庫存不足")

st.divider()

# 新增商品庫存區
st.header("新增商品庫存")

col1, col2 = st.columns(2)

with col1:
    selected_product = st.selectbox(
        "選擇商品",
        product_keys,
        format_func=lambda x: st.session_state.products[x]["name"]
    )

with col2:
    add_stock = st.number_input("選擇新增庫存數量", min_value=1, max_value=100, value=1, step=1)

if st.button("新增庫存"):
    st.session_state.products[selected_product]["stock"] += add_stock
    st.success(f"{st.session_state.products[selected_product]['name']} 已新增 {add_stock} 個庫存")

st.subheader("目前商品庫存:")
for key in product_keys:
    product = st.session_state.products[key]
    st.write(f"{product['name']}{product['stock']}")
