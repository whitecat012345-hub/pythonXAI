# 🐍 Python 課堂筆記：AI 聊天機器人＋Streamlit 購物平台

今天的課程很厲害！我們學到怎麼讓 **Python 跟 AI 說話**，還學到怎麼用 **Streamlit 做出聊天網頁和購物平台**。

可以把今天的內容想成三大關卡：

> 🤖 第一關：Python 跟 AI 聊天
> 💬 第二關：做一個 AI 聊天網頁
> 🛒 第三關：做一個會計算庫存的購物平台

---

## 🌟 第一課：匯入需要的工具

```python
import openai
from dotenv import load_dotenv
import os
```

這三個工具就像三個不同的小幫手。

| 指令            | 小學生版解釋              |
| --------------- | ------------------------- |
| `import openai` | 找 OpenAI 小幫手來使用 AI |
| `import os`     | 找電腦系統小幫手          |
| `load_dotenv()` | 打開 `.env` 秘密資料夾    |
| `os.getenv()`   | 從秘密資料夾拿資料        |

例如：

```python
load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
```

意思就是：

> 🔐 「請去 `.env` 裡面找我的 OpenAI API Key。」

---

# 🔑 第二課：什麼是 API Key？

API Key 可以想成是：

> **AI 世界的秘密鑰匙 🔑**

有了這把鑰匙，我們的 Python 程式才可以跟 OpenAI 的 AI 聯絡。

⚠️ API Key 不可以隨便給別人看！

就像：

- 銀行密碼不能給別人
- 遊戲帳號密碼不能給別人
- API Key 也不能放在公開的程式碼裡

所以可以把它放在 `.env` 或 Streamlit 的 `secrets` 裡。

---

# 🤖 第三課：讓 Python 跟 AI 說話

我們可以讓使用者輸入問題：

```python
user_input = input("你:")
```

例如畫面可能變成：

```text
你:今天天氣如何？
```

輸入的文字會被存進：

```python
user_input
```

---

# 🔄 第四課：`while True` 重複聊天

```python
while True:
```

這句的意思是：

> 🔁 「一直做下去！」

所以程式可以一直問：

```text
你:
AI:
你:
AI:
你:
AI:
```

就像真的聊天一樣。

---

# 🚪 第五課：離開聊天程式

如果輸入：

```text
exit
```

或：

```text
quit
```

就可以離開聊天。

正確寫法可以是：

```python
if user_input.lower() in ["exit", "quit"]:
    break
```

### `lower()` 是什麼？

```python
user_input.lower()
```

會把英文全部變成小寫。

例如：

```text
EXIT
```

會變：

```text
exit
```

所以使用者輸入：

```text
EXIT
Exit
exit
```

都可以辨認。

### `break` 是什麼？

```python
break
```

意思就是：

> 🛑 「停止迴圈！」

---

# 🧠 第六課：告訴 AI 要做什麼

OpenAI 的聊天資料通常會像這樣：

```python
messages=[
    {"role": "system", "content": "請用繁體中文進行後續對話"},
    {"role": "user", "content": user_input}
]
```

裡面有兩個非常重要的東西：

```python
role
content
```

---

## 🎭 `role`：誰在講話？

我們可以把 AI 聊天想像成三種角色。

| role        | 是誰？    |
| ----------- | --------- |
| `system`    | 老師 📋   |
| `user`      | 使用者 👦 |
| `assistant` | AI 🤖     |

例如：

```python
{"role": "system", "content": "請用繁體中文回答"}
```

就是：

> 📋 老師告訴 AI：「之後都要講繁體中文。」

---

```python
{"role": "user", "content": "你好"}
```

就是：

> 👦 使用者說：「你好。」

---

```python
{"role": "assistant", "content": "你好！"}
```

就是：

> 🤖 AI 說：「你好！」

---

# 📦 第七課：`content` 是說話的內容

例如：

```python
{
    "role": "user",
    "content": "什麼是 Python？"
}
```

`role` 告訴我們：

> 👦 是使用者講話。

`content` 告訴我們：

> 💬 他說了「什麼是 Python？」

---

# 🤖 第八課：呼叫 AI

我們學到：

```python
response = openai.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages
)
```

可以想像成：

> 📮 把我們的問題寄給 AI。

其中：

```python
model="gpt-4o-mini"
```

是在選擇：

> 「我要找哪一個 AI 來回答？」

---

# 📬 第九課：把 AI 的答案拿出來

AI 回答之後，我們可以使用：

```python
assistant_message = response.choices[0].message.content
```

把 AI 的文字取出來。

然後：

```python
print(f"AI:{assistant_message}")
```

顯示在畫面上。

例如：

```text
你:什麼是蘋果？
AI:蘋果是一種水果。
```

---

# 🧠 第十課：讓 AI 記得以前聊過什麼

一開始先建立一個清單：

```python
messages = [
    {
        "role": "system",
        "content": "請用繁體中文進行後續對話"
    }
]
```

使用者講話後：

```python
messages.append(
    {
        "role": "user",
        "content": user_input
    }
)
```

AI 回答後也要記起來：

```python
messages.append(
    {
        "role": "assistant",
        "content": assistant_message
    }
)
```

這樣 `messages` 就可能變成：

```python
[
    {"role": "system", "content": "請用繁體中文"},
    {"role": "user", "content": "我叫小明"},
    {"role": "assistant", "content": "你好，小明！"},
    {"role": "user", "content": "我叫什麼名字？"}
]
```

AI 就比較能知道：

> 🤖「你剛剛說你叫小明！」

---

# 🧩 第十一課：`append()` 是什麼？

```python
messages.append(...)
```

`append()` 可以想成：

> ➕ 在清單最後面增加一個東西。

例如：

```python
fruits = ["蘋果", "香蕉"]
```

加入橘子：

```python
fruits.append("橘子")
```

就會變成：

```python
["蘋果", "香蕉", "橘子"]
```

所以聊天程式也可以用 `append()` 一直加入新的聊天紀錄。

---

# 💬 第十二課：Streamlit 的聊天泡泡

我們學到：

```python
st.chat_message("user").write("這是使用者的訊息")
```

會顯示：

> 👤 使用者聊天泡泡

而：

```python
st.chat_message("assistant").write("這是AI的訊息")
```

會顯示：

> 🤖 AI 聊天泡泡

---

# 🪄 第十三課：聊天泡泡加圖示

還可以自己設定 avatar：

```python
st.chat_message(
    "user",
    avatar="🪄"
).write("你好")
```

AI：

```python
st.chat_message(
    "assistant",
    avatar="✨"
).write("哈囉！")
```

這樣聊天畫面會更可愛。

---

# 📚 第十四課：使用 `for` 顯示聊天紀錄

假設有：

```python
history = [
    {"role": "user", "content": "你好"},
    {"role": "assistant", "content": "哈囉"}
]
```

可以：

```python
for message in history:
```

意思是：

> 📖 一筆一筆把以前的聊天紀錄拿出來。

再判斷：

```python
if message["role"] == "user":
```

如果是使用者，就畫使用者泡泡。

否則：

```python
else:
```

就畫 AI 泡泡。

---

# 🧳 第十五課：`st.session_state`

這是今天非常重要的一個功能！

```python
st.session_state
```

可以把它想像成：

> 🧳 Streamlit 的「記憶背包」。

因為 Streamlit 網頁常常會重新執行程式，如果沒有這個背包，很多資料就會不見。

---

## 例如：記住聊天紀錄

```python
if "history" not in st.session_state:
    st.session_state.history = []
```

意思是：

> 如果記憶背包裡還沒有 `history`，就建立一個空清單。

---

# 🧠 第十六課：記住系統訊息

```python
if "system_message" not in st.session_state:
    st.session_state.system_message = "請用繁體中文進行後續對話"
```

就是把：

> 「請用繁體中文回答」

存進 Streamlit 的記憶背包。

---

# 🤖 第十七課：記住 AI 模型

```python
if "model" not in st.session_state:
    st.session_state.model = "gpt-4o-mini"
```

就是記住：

> 現在使用哪一個 AI 模型。

---

# 🏠 第十八課：`st.columns()` 分欄

```python
col1, col2, col3 = st.columns([4, 2, 1])
```

可以把網頁切成三間房間：

```text
┌────────────────┬────────┬────┐
│     col1       │ col2   │col3│
│      4         │  2     │ 1  │
└────────────────┴────────┴────┘
```

第一欄最大，第三欄最小。

---

# 📝 第十九課：`st.text_input()`

```python
st.text_input("系統訊息")
```

會做出一個文字輸入框。

可以讓使用者修改：

```text
系統訊息
[請用繁體中文回答          ]
```

---

# 🔽 第二十課：`st.selectbox()`

```python
st.selectbox(
    "AI模型",
    [
        "gpt-4o-mini",
        "gpt-4o"
    ]
)
```

會做出：

> 🔽 下拉選單

讓使用者選擇模型。

---

# 🗑️ 第二十一課：按鈕

```python
if st.button("🗑️"):
```

意思是：

> 如果使用者按下垃圾桶按鈕，就執行下面的程式。

例如清空聊天：

```python
st.session_state.history = []
```

---

# 🔄 第二十二課：`st.rerun()`

```python
st.rerun()
```

可以想成：

> 🔄 「重新整理 Streamlit 程式！」

例如清掉聊天紀錄後：

```python
st.session_state.history = []
st.rerun()
```

畫面就會重新更新。

---

# 💬 第二十三課：`st.chat_input()`

```python
prompt = st.chat_input("請輸入想要對話的訊息")
```

會在網頁下面出現聊天輸入框：

```text
┌─────────────────────────────┐
│ 請輸入想要對話的訊息...      │
└─────────────────────────────┘
```

使用者打的文字就會放進：

```python
prompt
```

---

# 🛒 第二十四課：開始做「購物平台」

我們另外做了一個：

# 🛍️ Python 水果購物平台

裡面有：

- 🍎 蘋果
- 🍌 香蕉
- 🍊 橘子
- 商品圖片
- 商品價格
- 商品庫存
- 購買按鈕
- 補充庫存

---

# 📦 第二十五課：用字典存商品資料

例如：

```python
"apple": {
    "name": "蘋果",
    "price": 10,
    "stock": 10,
    "image": "image/apple.png"
}
```

可以想像成一張商品卡：

```text
🍎 蘋果

名稱：蘋果
價格：10 元
庫存：10 個
圖片：image/apple.png
```

---

# 🗂️ 第二十六課：什麼是 Dictionary 字典？

Python 的：

```python
{}
```

可以拿來建立 **字典 Dictionary**。

例如：

```python
apple = {
    "name": "蘋果",
    "price": 10,
    "stock": 10
}
```

想拿名字：

```python
apple["name"]
```

得到：

```text
蘋果
```

想拿價格：

```python
apple["price"]
```

得到：

```text
10
```

---

# 🔢 第二十七課：讓使用者選擇欄位數

```python
column_num = st.number_input(
    "請輸入欄位數",
    min_value=1,
    max_value=5,
    value=4,
    step=1
)
```

意思是：

> 讓使用者決定一排要放幾個商品。

例如輸入：

```text
2
```

商品可能變成：

```text
🍎 蘋果    🍌 香蕉
🍊 橘子    🍇 其他商品
```

---

# 🔑 第二十八課：`.keys()`

```python
product_keys = list(
    st.session_state.products.keys()
)
```

`.keys()` 就是在拿商品的「代號」。

例如：

```python
{
    "apple": {...},
    "banana": {...},
    "orange": {...}
}
```

`.keys()` 可以拿到：

```python
apple
banana
orange
```

---

# 🔁 第二十九課：`enumerate()`

```python
for i, key in enumerate(product_keys):
```

`enumerate()` 可以同時知道：

> 🔢 現在是第幾個

和

> 🔑 現在是哪個商品

例如：

```text
0 apple
1 banana
2 orange
```

---

# 🖼️ 第三十課：檢查圖片存不存在

```python
if os.path.exists(product["image"]):
```

意思是：

> 🔍 「這張圖片真的存在嗎？」

如果存在：

```python
st.image(product["image"], width=150)
```

就顯示圖片。

如果不存在：

```python
st.write("找不到圖片")
```

---

# 🏷️ 第三十一課：顯示商品名稱

```python
st.subheader(product["name"])
```

會顯示比較大的文字。

例如：

# 🍎 蘋果

---

# 💰 第三十二課：使用 f-string

例如：

```python
st.write(f"價錢：{product['price']}")
```

如果：

```python
product["price"] = 10
```

就會顯示：

```text
價錢：10
```

`f""` 就像是一台：

> 🧩 「把變數塞進文字裡」的機器。

---

# 🛒 第三十三課：購買商品

```python
if st.button(f"購買{product['name']}"):
```

如果使用者按：

```text
購買蘋果
```

就檢查庫存。

---

# 📦 第三十四課：檢查庫存

```python
if product["stock"] > 0:
```

就是：

> 「還有商品嗎？」

如果還有：

```python
st.session_state.products[key]["stock"] -= 1
```

庫存減一。

例如原本：

```text
🍎 10 個
```

買一個後：

```text
🍎 9 個
```

---

# ➖ 第三十五課：`-=`

```python
stock -= 1
```

跟：

```python
stock = stock - 1
```

意思一樣。

例如：

```python
stock = 10
stock -= 1
```

變成：

```python
9
```

---

# ✅ 第三十六課：`st.success()`

買成功時：

```python
st.success("你已購買蘋果 1 個")
```

就會顯示成功訊息。

例如：

> ✅ 你已購買蘋果 1 個

---

# ❌ 第三十七課：`st.error()`

如果庫存變成：

```text
0
```

就顯示：

```python
st.error("蘋果庫存不足")
```

例如：

> ❌ 蘋果庫存不足

---

# ➖ 第三十八課：`st.divider()`

```python
st.divider()
```

會畫一條分隔線：

---

讓網頁不同區域比較容易看懂。

---

# 📦 第三十九課：增加商品庫存

可以先讓使用者選商品：

```python
selected_product = st.selectbox(
    "選擇商品",
    product_keys
)
```

再輸入增加幾個：

```python
add_stock = st.number_input(
    "選擇新增庫存數量"
)
```

最後按：

```text
新增庫存
```

---

# ➕ 第四十課：增加庫存

```python
st.session_state.products[selected_product]["stock"] += add_stock
```

`+=` 就是：

> ➕ 加上去。

例如：

```text
蘋果原本：10 個
增加：5 個
```

變成：

```text
蘋果：15 個
```

---

# 🧮 `+=` 和 `-=` 要記住

| 指令     | 意思 | 例子    |
| -------- | ---- | ------- |
| `x += 1` | 加 1 | 10 → 11 |
| `x -= 1` | 減 1 | 10 → 9  |
| `x += 5` | 加 5 | 10 → 15 |
| `x -= 5` | 減 5 | 10 → 5  |

---

# ⚠️ 今天程式裡有兩個很重要的小錯誤

## ❌ 錯誤 1：判斷 exit

原本：

```python
if user_input.lower() == ["exit","quit"]:
```

這樣是在拿「一個字串」和「一個清單」比較，所以不會成功。

✅ 應該改成：

```python
if user_input.lower() in ["exit", "quit"]:
    break
```

記法：

> `in` = 「有沒有在裡面？」

---

## ❌ 錯誤 2：記錄 AI 回答

原本：

```python
messages.append({
    "role": "assistant",
    "content": "user_unput"
})
```

這樣 AI 的真正答案沒有被存進去。

✅ 應該是：

```python
messages.append({
    "role": "assistant",
    "content": assistant_message
})
```

也就是：

> 🤖 AI 說了什麼，就把 AI 真正說的內容記下來。

---

# 🧠 今天最重要的 Python 指令整理

| 指令                | 小學生記法              |
| ------------------- | ----------------------- |
| `import`            | 找工具來幫忙 🧰         |
| `input()`           | 讓使用者輸入 ⌨️         |
| `while True`        | 一直重複 🔄             |
| `break`             | 停止迴圈 🛑             |
| `if`                | 如果…… 🤔               |
| `else`              | 不然的話……              |
| `for`               | 一個一個做 🔁           |
| `append()`          | 在清單最後加入東西 ➕   |
| `list()`            | 建立清單 📋             |
| `{}`                | 字典 Dictionary 📖      |
| `st.session_state`  | Streamlit 的記憶背包 🧳 |
| `st.chat_message()` | 顯示聊天泡泡 💬         |
| `st.chat_input()`   | 聊天輸入框 ⌨️           |
| `st.columns()`      | 把網頁分欄 🏠           |
| `st.selectbox()`    | 下拉選單 🔽             |
| `st.number_input()` | 數字輸入框 🔢           |
| `st.button()`       | 按鈕 🔘                 |
| `st.image()`        | 顯示圖片 🖼️             |
| `st.success()`      | 成功訊息 ✅             |
| `st.error()`        | 錯誤訊息 ❌             |
| `st.rerun()`        | 重新跑一次程式 🔄       |
| `.keys()`           | 找字典裡所有鑰匙 🔑     |
| `+=`                | 加上去 ➕               |
| `-=`                | 減掉 ➖                 |

---

# 🎯 今天我們真正學會了什麼？

今天不是只學幾個 Python 指令，而是已經開始把很多以前學過的東西組合起來。

我們會：

> 👦 使用者輸入問題
> ↓
> 🐍 Python 接收問題
> ↓
> 📚 把問題放進聊天紀錄
> ↓
> 🤖 把問題送給 AI
> ↓
> 💬 AI 回答
> ↓
> 🧳 把回答存進 `session_state`
> ↓
> 🖥️ Streamlit 把回答顯示成聊天泡泡

而在購物平台裡，我們又學會：

> 🍎 建立商品
> → 🖼️ 顯示圖片
> → 💰 顯示價格
> → 📦 記錄庫存
> → 🛒 按下購買
> → ➖ 庫存減 1
> → ➕ 還可以補充庫存

所以今天已經是在練習一個非常重要的程式設計能力：

## 🌟「把很多小功能組合成一個真正可以使用的程式！」

這就像玩樂高一樣：

以前學的 `if`、`for`、`list`、`dictionary`、`button` 都是一塊一塊的小積木；今天開始把它們組合起來，就變成了 **AI 聊天機器人 🤖** 和 **購物網站 🛒**。
