# 🐍 Python 學習筆記：Streamlit、迴圈、亂數、字典與圖片

今天學到的內容很多，可以分成 **8 大主題**：

1. 📐 Streamlit 欄位 `st.columns`
2. ⌨️ 文字輸入 `st.text_input`
3. 💾 `st.session_state` 記住資料
4. ➕ 算術指定運算子
5. 🔁 `while`、`break`、`continue`
6. 🎲 `random` 亂數
7. 📖 字典 `dict`
8. 🖼️ Streamlit 顯示圖片

---

# 1️⃣ Streamlit 欄位：`st.columns()`

平常 Streamlit 的東西會從**上往下排列**。

如果想讓東西「左右排在同一排」，就可以使用：

```python
st.columns()
```

## 🌟 兩個一樣寬的欄位

```python
col1, col2 = st.columns(2)

col1.button("按鈕1", key="btn1")
col2.button("按鈕2", key="btn2")
```

畫面大概會像：

```text
按鈕1      按鈕2
```

`st.columns(2)` 的意思就是：

> 把畫面分成 2 欄。

---

# 2️⃣ 可以決定每一欄有多寬

```python
col1, col2 = st.columns([1, 2])
```

代表：

```text
col1    col2
 1       2
```

所以 `col2` 大約會是 `col1` 的 **2 倍寬**。

例如：

```python
col1, col2, col3 = st.columns([1, 2, 3])
```

就是：

- `col1` → 1 份
- `col2` → 2 份
- `col3` → 3 份

---

# 3️⃣ `with`：告訴 Python「東西要放在哪一欄」

如果一個欄位裡想放很多東西，可以使用：

```python
with col1:
```

例如：

```python
col1, col2 = st.columns([1, 2])

with col1:
    st.button("按鈕1")
    st.write("我是左邊")

with col2:
    st.button("按鈕2")
    st.write("我是右邊")
```

可以把 `with col1:` 想像成：

> 📦 接下來縮排裡面的東西，全部放進 col1 這個箱子。

---

# 4️⃣ 按下按鈕後做事情

```python
if st.button("按鈕1"):
    st.balloons()
```

意思是：

> 如果使用者按下「按鈕1」，就放氣球！ 🎈

所以 `st.button()` 不只是顯示按鈕，也可以拿來判斷：

```python
if 按鈕被按下:
    做某件事情
```

---

# 5️⃣ 為什麼按鈕需要 `key`？

例如：

```python
st.button("按鈕", key="btn1")
st.button("按鈕", key="btn2")
```

`key` 就像每個按鈕的「身分證」。

即使兩個按鈕都叫：

```text
按鈕
```

Streamlit 還是知道它們是不同的按鈕。

⚠️ 同一個網頁裡的 `key` 不可以重複。

---

# 6️⃣ 用 `for` 自動建立很多欄位

如果有很多欄位，不需要一個一個寫。

```python
cols = st.columns(4)
```

會建立：

```python
cols[0]
cols[1]
cols[2]
cols[3]
```

接著可以：

```python
for i in range(len(cols)):
    with cols[i]:
        st.button(f"按鈕{i+1}", key=f"btn{i}")
```

這樣 Python 就會自動產生：

```text
按鈕1   按鈕2   按鈕3   按鈕4
```

💡 這就是把之前學過的：

- `for`
- `range()`
- `len()`
- List
- `st.columns()`

全部組合在一起！

---

# 7️⃣ `st.text_input()`：讓使用者輸入文字

基本寫法：

```python
text = st.text_input("請輸入文字")
```

使用者輸入的內容會存進：

```python
text
```

所以可以：

```python
text = st.text_input("請輸入文字")
st.write(f"你輸入的是：{text}")
```

---

## 🌟 設定預設文字

```python
text = st.text_input(
    "請輸入文字",
    value="這是預設文字"
)
```

畫面一開始就會看到：

```text
這是預設文字
```

---

# 8️⃣ `st.session_state`：幫網頁「記住資料」🧠

Streamlit 有一個很重要的特色：

> 每按一次按鈕，程式通常會重新執行。

所以普通變數很容易重新變回原本的值。

例如：

```python
a = 1
```

重新執行之後又變成：

```python
a = 1
```

這時候就需要：

```python
st.session_state
```

它就像 Streamlit 的：

> 🧠 記憶盒子

---

## 🌟 建立一個記憶

```python
if "ans1" not in st.session_state:
    st.session_state.ans1 = 1
```

意思是：

> 如果記憶盒子裡還沒有 `ans1`，就先建立它，並設定成 1。

---

## 🌟 每按一次就 +1

```python
if st.button("ans + 1"):
    st.session_state.ans1 += 1
```

再顯示：

```python
st.write(st.session_state.ans1)
```

假設一直按按鈕：

```text
1
2
3
4
5
...
```

資料不會每次都消失。

---

# 9️⃣ `st.rerun()`：重新執行網頁 🔄

```python
st.rerun()
```

意思就是：

> 「Streamlit，請從頭再執行一次！」

例如：

```python
if st.button("重新整理"):
    st.rerun()
```

---

# 🔟 點餐機：把很多學過的東西組合起來 🍔

這個程式使用：

```text
st.session_state
List
append()
pop()
for
range()
len()
st.columns()
st.text_input()
st.button()
st.rerun()
```

---

## 建立購物籃

```python
if "cart" not in st.session_state:
    st.session_state.cart = []
```

一開始購物籃：

```python
[]
```

是空的。

---

## 加入餐點

```python
st.session_state.cart.append(item_input)
```

`append()` 的意思：

> 把新東西加到 List 最後面。

例如：

```python
cart = ["漢堡"]

cart.append("薯條")
```

變成：

```python
["漢堡", "薯條"]
```

---

## `.strip()`：檢查是不是只有空白

```python
if item_input.strip():
```

假如使用者輸入：

```text
"      "
```

看起來有輸入，但其實全部都是空白。

`.strip()` 會把前後空白去掉。

所以可以避免有人加入一個「空白餐點」。

---

## 刪除餐點：`pop()`

```python
st.session_state.cart.pop(i)
```

例如：

```python
food = ["漢堡", "薯條", "可樂"]
```

執行：

```python
food.pop(1)
```

就會刪掉 index `1`：

```python
["漢堡", "可樂"]
```

記得：

```text
漢堡 → index 0
薯條 → index 1
可樂 → index 2
```

Python 的 index 從 **0 開始**。

---

# 1️⃣1️⃣ 算術指定運算子

這些是程式設計很常看到的「縮寫寫法」。

## `+=`

```python
a += 1
```

等於：

```python
a = a + 1
```

---

## `-=`

```python
a -= 1
```

等於：

```python
a = a - 1
```

---

## `*=`

```python
a *= 2
```

等於：

```python
a = a * 2
```

---

## `/=`

```python
a /= 2
```

等於：

```python
a = a / 2
```

---

## `//=` 整數除法

```python
a //= 2
```

等於：

```python
a = a // 2
```

例如：

```python
7 // 2
```

答案：

```text
3
```

因為只取「商」。

---

## `%=` 取餘數

```python
a %= 2
```

等於：

```python
a = a % 2
```

例如：

```python
7 % 2
```

答案：

```text
1
```

因為：

```text
7 ÷ 2 = 3 ... 1
```

---

## `**=` 次方

```python
a **= 2
```

等於：

```python
a = a ** 2
```

例如：

```python
3 ** 2
```

就是：

```text
3 × 3 = 9
```

---

# 1️⃣2️⃣ 運算子的優先順序

就像數學有「先乘除後加減」，Python 也有順序。

大致上可以記：

```text
1. ()              括號
2. **              次方
3. * / // %         乘、除、整數除法、餘數
4. + -              加、減
5. == != > < >= <=  比較
6. not
7. and
8. or
9. = += -= ...      指定
```

最重要的技巧：

> 🤔 不確定先算誰，就加括號！

例如：

```python
(3 + 2) * 4
```

會比：

```python
3 + 2 * 4
```

更清楚。

---

# 1️⃣3️⃣ `while` 回圈 🔁

以前學過：

```python
for
```

今天又學到：

```python
while
```

`while` 的意思是：

> **只要條件還成立，就一直做。**

例如：

```python
i = 0

while i < 5:
    print(i)
    i += 1
```

結果：

```text
0
1
2
3
4
```

流程就是：

```text
i = 0
↓
i < 5 嗎？
↓ 是
印出 i
↓
i + 1
↓
再檢查
```

---

# 1️⃣4️⃣ `while True`：無限回圈 ♾️

```python
while True:
```

代表：

> 條件永遠是 True，所以會一直重複。

例如：

```python
while True:
    print("Hello")
```

會永遠印：

```text
Hello
Hello
Hello
Hello
...
```

所以通常要搭配：

```python
break
```

才能停下來。

---

# 1️⃣5️⃣ `break`：立刻離開回圈 🛑

例如：

```python
for i in range(5):
    print(i)

    if i == 3:
        break
```

結果：

```text
0
1
2
3
```

本來還有 `4`，但是：

```python
i == 3
```

時遇到：

```python
break
```

所以回圈直接結束。

可以把 `break` 想成：

> 🛑「不要再跑了，我要離開這個回圈！」

---

# 1️⃣6️⃣ `continue`：跳過這一次 ⏭️

例如：

```python
for i in range(5):
    if i == 2:
        continue

    print(i)
```

結果：

```text
0
1
3
4
```

因為 `i == 2` 時：

```python
continue
```

會說：

> 這一次不要繼續了，直接進行下一次回圈。

### ⭐ 很容易搞混

| 指令       | 意思            |
| ---------- | --------------- |
| `break`    | 🛑 整個回圈結束 |
| `continue` | ⏭️ 只跳過這一次 |

---

# 1️⃣7️⃣ `try`、`except`：處理錯誤 🚑

例如：

```python
num = int(input("請輸入數字："))
```

如果使用者輸入：

```text
apple
```

Python 沒辦法把 `apple` 變成整數，就會發生錯誤。

所以可以：

```python
try:
    num = int(input("請輸入數字："))
except:
    print("請輸入數字")
```

可以想成：

```text
try
👉 試著做看看

except
👉 如果出錯，就來這裡處理
```

---

## 搭配 `continue`

```python
try:
    num = int(input("請輸入數字："))
except:
    print("請輸入數字")
    continue
```

如果輸入錯誤：

```text
apple
```

程式不會壞掉，而是顯示：

```text
請輸入數字
```

然後再問一次。

---

# 1️⃣8️⃣ `random`：讓電腦抽籤 🎲

先載入亂數工具：

```python
import random as rm
```

意思就是：

> 把 `random` 工具箱拿進來，並幫它取綽號叫 `rm`。

---

# 1️⃣9️⃣ `rm.randrange()`

它的規則跟 `range()` 很像。

```python
rm.randrange(7)
```

可能得到：

```text
0、1、2、3、4、5、6
```

---

```python
rm.randrange(1, 7)
```

可能得到：

```text
1～6
```

⚠️ 不包含最後的 `7`。

---

```python
rm.randrange(1, 6, 2)
```

可能得到：

```text
1、3、5
```

---

# 2️⃣0️⃣ `rm.randint()`

```python
rm.randint(1, 6)
```

可能得到：

```text
1、2、3、4、5、6
```

⭐ 和 `randrange()` 最大的差別：

```python
rm.randint(1, 6)
```

**會包含 1 和 6。**

非常適合模擬：

🎲 骰子。

---

# 2️⃣1️⃣ 終極密碼遊戲 🎯

先讓電腦偷偷選答案：

```python
ans = rm.randint(1, 100)
```

例如電腦偷偷選：

```text
63
```

玩家不知道。

---

設定範圍：

```python
min_num = 1
max_num = 100
```

玩家猜：

```text
50
```

因為：

```text
50 < 63
```

所以：

```text
太小了
```

範圍就可以縮成：

```text
50～100
```

下一次如果猜：

```text
80
```

因為太大：

```text
50～80
```

最後猜到：

```text
63
```

就：

```python
print("恭喜你答對了")
break
```

🎉 遊戲結束！

💡 寫程式時，比起把變數叫做 `min`、`max`，建議使用：

```python
min_num
max_num
```

這樣比較不會和 Python 本來的 `min()`、`max()` 功能搞混。

---

# 2️⃣2️⃣ 字典 Dictionary：`dict` 📖

List 是：

```python
["蘋果", "香蕉", "西瓜"]
```

我們用 index 找資料：

```python
fruit[0]
```

但字典不一樣。

字典是利用：

```text
key → value
```

來找資料。

就像真正的字典：

```text
蘋果 → apple
香蕉 → banana
```

---

## 建立字典

```python
d = {
    "a": 1,
    "b": 2,
    "c": 3
}
```

其中：

```text
"a" → key
1   → value
```

---

# 2️⃣3️⃣ 字典的 Key 不可以重複

例如：

```python
d = {
    "小明": 90,
    "小美": 100
}
```

我們可以：

```python
print(d["小明"])
```

得到：

```text
90
```

所以：

> List 用 index 找東西。
> Dict 用 key 找東西。

---

# 2️⃣4️⃣ `.keys()`：取得所有 Key 🔑

```python
print(d.keys())
```

也可以：

```python
for key in d.keys():
    print(key)
```

得到：

```text
a
b
c
```

---

# 2️⃣5️⃣ `.values()`：取得所有 Value 📦

```python
for value in d.values():
    print(value)
```

得到：

```text
1
2
3
```

---

# 2️⃣6️⃣ `.items()`：Key 和 Value 一起拿

```python
for key, value in d.items():
    print(key, value)
```

得到：

```text
a 1
b 2
c 3
```

這個非常常用！

可以記：

```text
.keys()   → 🔑 Key
.values() → 📦 Value
.items()  → 🔑 + 📦
```

---

# 2️⃣7️⃣ 新增或修改字典

例如：

```python
d["d"] = 4
```

如果原本沒有 `"d"`：

👉 新增資料。

如果原本已經有 `"d"`：

👉 修改資料。

例如：

```python
grade = {"小明": 90}

grade["小明"] = 100
```

最後：

```python
{"小明": 100}
```

---

# 2️⃣8️⃣ `.pop()`：刪除字典資料

```python
d.pop("a")
```

就是：

> 把 key 是 `"a"` 的資料刪掉。

而且會把刪掉的 value 回傳。

例如：

```python
print(d.pop("a"))
```

可能得到：

```text
1
```

---

如果怕資料不存在，可以：

```python
d.pop("a", "not found")
```

如果找不到：

```text
not found
```

就不會報錯。

---

# 2️⃣9️⃣ `in`：檢查字典裡有沒有 Key

```python
print("b" in d)
```

如果有 `"b"`：

```text
True
```

如果沒有：

```text
False
```

⭐ 對字典使用 `in` 時，主要是在檢查 **Key**。

---

# 3️⃣0️⃣ 字典裡還可以放 List！

```python
d = {
    "a": [1, 2, 3]
}
```

取得整個 List：

```python
d["a"]
```

得到：

```python
[1, 2, 3]
```

取得第一個數字：

```python
d["a"][0]
```

得到：

```text
1
```

---

# 3️⃣1️⃣ 字典裡還可以放字典！

```python
d = {
    "b": {
        "c": 4,
        "d": 5
    }
}
```

取得裡面的 `c`：

```python
d["b"]["c"]
```

得到：

```text
4
```

可以想像成：

```text
先打開 b 這個箱子
      ↓
再找裡面的 c
```

---

# 3️⃣2️⃣ 成績系統 🏫

例如：

```python
grade = {
    "小明": {
        "國文": [90, 80, 70],
        "數學": [85, 75, 65],
        "英文": [95, 85, 75]
    }
}
```

這就像：

```text
小明
 ├─ 國文 → 90、80、70
 ├─ 數學 → 85、75、65
 └─ 英文 → 95、85、75
```

---

## 找小明的數學

```python
grade["小明"]["數學"]
```

得到：

```python
[85, 75, 65]
```

---

## 找第一次數學成績

```python
grade["小明"]["數學"][0]
```

得到：

```text
85
```

---

# 3️⃣3️⃣ `sum()`：把數字加起來

```python
scores = [90, 80, 70]
```

```python
sum(scores)
```

得到：

```text
240
```

---

# 3️⃣4️⃣ 計算平均

公式：

```text
平均 = 總和 ÷ 數量
```

Python：

```python
avg = sum(scores) / len(scores)
```

例如：

```python
scores = [90, 80, 70]

avg = sum(scores) / len(scores)
print(avg)
```

結果：

```text
80
```

---

# 3️⃣5️⃣ `.2f`：小數點後兩位

```python
print(f"{avg:.2f}")
```

假設：

```python
avg = 83.333333
```

會顯示：

```text
83.33
```

所以：

```text
.2f → 小數點後保留 2 位
```

---

# 3️⃣6️⃣ `len()` 也可以算字典長度

```python
avg_grade = {
    "國文": [],
    "數學": [],
    "英文": []
}
```

```python
len(avg_grade)
```

答案：

```text
3
```

因為有 3 個 Key：

```text
國文
數學
英文
```

---

# 3️⃣7️⃣ Streamlit 顯示圖片 🖼️

先：

```python
import streamlit as st
```

如果圖片在：

```text
image/apple.png
```

可以：

```python
st.image("image/apple.png")
```

---

## 設定圖片寬度

```python
st.image("image/apple.png", width=300)
```

代表圖片寬度設定為：

```text
300 pixels
```

---

# 🧠 今天最重要的指令整理

| 指令               | 功能                      |
| ------------------ | ------------------------- |
| `st.columns(2)`    | 📐 把畫面分成 2 欄        |
| `with col1:`       | 📦 把東西放進指定欄位     |
| `st.text_input()`  | ⌨️ 讓使用者輸入文字       |
| `st.session_state` | 🧠 記住 Streamlit 資料    |
| `st.rerun()`       | 🔄 重新執行網頁           |
| `.append()`        | ➕ List 最後加入資料      |
| `.pop()`           | 🗑️ 刪除資料               |
| `+=`               | ➕ 加完存回去             |
| `while`            | 🔁 條件成立就一直重複     |
| `while True`       | ♾️ 無限回圈               |
| `break`            | 🛑 結束整個回圈           |
| `continue`         | ⏭️ 跳過這一次             |
| `try`              | 🧪 試著執行               |
| `except`           | 🚑 發生錯誤時處理         |
| `rm.randrange()`   | 🎲 隨機選數字，不包含結尾 |
| `rm.randint()`     | 🎲 隨機整數，包含頭尾     |
| `dict`             | 📖 用 Key 找 Value        |
| `.keys()`          | 🔑 取得所有 Key           |
| `.values()`        | 📦 取得所有 Value         |
| `.items()`         | 🔑📦 同時取得 Key、Value  |
| `sum()`            | ➕ 數字全部加起來         |
| `len()`            | 📏 計算數量               |
| `st.image()`       | 🖼️ 顯示圖片               |

---

# 🌟 今天其實已經可以做出很厲害的程式了

你現在學到的東西已經可以組合成：

```text
🍔 點餐機
🎯 終極密碼
📊 學生成績系統
🛒 購物車
🖼️ 圖片展示網站
🎲 骰子遊戲
📝 文字輸入程式
```

最重要的不是把每個指令背起來，而是慢慢了解：

> **變數負責記資料 → if 負責做決定 → for / while 負責重複 → List / Dict 負責整理資料 → Streamlit 把程式做成網頁。**

這幾個觀念如果熟悉，以後就可以把它們像 LEGO 一樣，一塊一塊組合成更大的程式。
