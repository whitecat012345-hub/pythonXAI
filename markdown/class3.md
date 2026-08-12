# 🐍 Python + Streamlit 課堂筆記

## 數字金字塔、List 清單、複製資料、排序、Columns 欄位與文字輸入

今天學到的內容很多，可以分成 **6 個大主題**：

1. 🔺 用 `for` 迴圈做金字塔
2. 📦 List 清單的基本用法
3. 🔍 List 的 Index 與切片
4. 🛠️ List 新增、刪除、排序
5. 🔗 `a = b` 和 `.copy()` 的差別
6. 🖥️ Streamlit 的 `columns` 與 `text_input`

---

# 1️⃣ 數字金字塔 🔺

我們可以使用：

- `st.number_input()` 讓使用者輸入數字
- `for` 迴圈重複執行
- `str()` 把數字變成文字
- `*` 讓文字重複

### 程式：

```python
import streamlit as st

st.title("數字金字塔")

n = st.number_input(
    "請輸入一個整數（1到9）",
    min_value=1,
    max_value=9,
    step=1
)

st.write("數字金字塔：")

for i in range(1, n + 1):
    st.write(str(i) * i)
```

假如輸入：

```text
5
```

會顯示：

```text
1
22
333
4444
55555
```

---

## 🧠 為什麼是 `str(i) * i`？

例如：

```python
i = 3
```

先做：

```python
str(i)
```

就會把：

```python
3
```

變成文字：

```python
"3"
```

接著：

```python
"3" * 3
```

就是：

```text
333
```

所以：

```python
str(i) * i
```

可以記成：

> 「把數字變文字，再重複 i 次。」

---

# 2️⃣ `range(1, n + 1)` 為什麼要 `+1`？

例如：

```python
range(1, 5)
```

實際上只有：

```text
1
2
3
4
```

因為 Python 的 `range()`：

> **最後面的數字不會被算進去。**

所以如果希望跑到 `5`：

```python
range(1, 6)
```

也就是：

```python
range(1, n + 1)
```

### 🧠 口訣

> `range()`：**顧頭不顧尾！**

---

# 3️⃣ 箭頭金字塔 ➡️

我們也可以利用：

```python
" " * 數量
```

產生空格，以及：

```python
"*" * 數量
```

產生星星。

---

### 程式：

```python
st.markdown("---")
st.title("箭頭金字塔")

n = st.number_input(
    "請輸入箭頭的層數",
    min_value=1,
    step=1
)

a = ""

for i in range(1, n + 1):
    a = a + (" " * (n - i) + "*" * (i * 2 - 1) + "\n")

for i in range(n):
    a = a + (" " * (n - 1) + "*" + "\n")

st.code(a)
```

例如：

```text
n = 4
```

會變成：

```text
   *
  ***
 *****
*******
   *
   *
   *
   *
```

---

# 4️⃣ `a = ""` 是什麼？

```python
a = ""
```

代表先準備一個**空字串**。

可以把它想像成：

> 📝 拿一張空白紙，等等慢慢把星星寫上去。

例如：

```python
a = ""
a = a + "*"
a = a + "**"
```

最後：

```python
a
```

就是：

```text
***
```

---

# 5️⃣ `\n` 是什麼？

```python
"\n"
```

代表：

> ↩️ 換行

例如：

```python
a = "Apple\nBanana"
```

顯示：

```text
Apple
Banana
```

---

# 6️⃣ List 是什麼？ 📦

`List` 中文通常叫做：

> **串列 / 清單**

它可以一次裝很多資料。

可以把 List 想像成：

> 🚂 一列火車，每個車廂都可以放一個東西。

---

## 空的 List

```python
print([])
```

代表：

```text
[]
```

裡面什麼東西都沒有。

---

## 放數字

```python
print([1, 2, 3])
```

有三個元素：

```text
1
2
3
```

---

## List 可以放不同種類的資料

```python
print([1, True, "a", 1.23])
```

裡面有：

- 整數 `1`
- 布林值 `True`
- 字串 `"a"`
- 小數 `1.23`

---

## List 裡面還可以再放 List 😲

```python
print([1, 2, 3, ["a", "b", "c"]])
```

可以想像成：

```text
大箱子
├── 1
├── 2
├── 3
└── 小箱子
    ├── a
    ├── b
    └── c
```

這種情況叫做：

> **Nested List（巢狀 List）**

也就是：

> List 裡面還有 List。

---

# 7️⃣ List 的 Index 編號 🔢

假設：

```python
L = [1, 2, 3, "a", "b", "c"]
```

Python 會幫每個東西編號。

| Index | 資料  |
| ----: | ----- |
|     0 | `1`   |
|     1 | `2`   |
|     2 | `3`   |
|     3 | `"a"` |
|     4 | `"b"` |
|     5 | `"c"` |

⚠️ Python 的 Index：

> **不是從 1 開始，而是從 0 開始！**

---

例如：

```python
print(L[0])
```

得到：

```text
1
```

```python
print(L[3])
```

得到：

```text
a
```

---

# 8️⃣ List 切片 Slice ✂️

List 可以一次拿出很多資料。

格式：

```python
L[開始:結束:間隔]
```

和：

```python
range(開始, 結束, 間隔)
```

的想法很像。

---

## 例子 ①

```python
L = [1, 2, 3, "a", "b", "c"]

print(L[1:4])
```

代表：

```text
從 index 1
拿到 index 4 前面
```

所以得到：

```python
[2, 3, "a"]
```

⚠️ Index `4` 不包含！

---

## 例子 ②

```python
print(L[::2])
```

代表：

```text
從頭開始
到最後
每次跳 2 格
```

所以取：

```text
index 0 → 1
index 2 → 3
index 4 → b
```

結果：

```python
[1, 3, "b"]
```

---

## 例子 ③

```python
print(L[1:4:2])
```

代表：

```text
從 index 1 開始
到 index 4 前面
每次跳 2 格
```

所以：

```text
index 1 → 2
index 3 → a
```

結果：

```python
[2, "a"]
```

---

## 🧠 Slice 口訣

```python
L[開始:結束:間隔]
```

記成：

> 🚩 **哪裡開始 → 哪裡停止 → 每次跳幾格**

---

# 9️⃣ `len()`：List 有幾個東西？ 📏

```python
L = [1, 2, 3, "a", "b", "c"]

print(len(L))
```

結果：

```text
6
```

因為裡面有：

```text
1
2
3
a
b
c
```

總共六個元素。

---

⚠️ 注意：

```python
len(L)
```

問的是：

> 有幾個元素？

不是：

> 最大 Index 是多少？

這個例子：

```text
元素數量 = 6
最大 Index = 5
```

---

# 🔟 使用 `for` 走訪 List 🚶

「走訪 List」的意思就是：

> 把 List 裡面的東西一個一個拿出來。

---

## 方法一：使用 Index

```python
L = [1, 2, 3, "a", "b", "c"]

for i in range(0, len(L), 2):
    print(L[i])
```

這裡：

```python
range(0, len(L), 2)
```

會得到：

```text
0
2
4
```

所以：

```python
L[0]
L[2]
L[4]
```

結果：

```text
1
3
b
```

---

## 方法二：直接拿 List 裡的資料

```python
for i in L:
    print(i)
```

結果：

```text
1
2
3
a
b
c
```

---

## ⭐ 兩種方法差在哪裡？

### 方法一

```python
for i in range(len(L)):
    print(L[i])
```

適合：

> 我需要知道 **Index 編號**。

---

### 方法二

```python
for i in L:
    print(i)
```

適合：

> 我只想知道 **裡面的資料**。

---

# 1️⃣1️⃣ 數字的複製

課堂上可以先把這個概念理解成 **Call by Value 的感覺**。

```python
a = 1
b = a

b = 2

print(a, b)
```

結果：

```text
1 2
```

為什麼？

一開始：

```text
a → 1
b → 1
```

接著：

```python
b = 2
```

變成：

```text
a → 1
b → 2
```

所以改 `b`：

> 不會把 `a` 也一起改掉。

---

# 1️⃣2️⃣ List 的 `a = b` 有什麼不同？ 🔗

這個非常重要！

```python
a = [1, 2, 3]
b = a
```

這時不是產生第二個獨立 List。

比較像：

```text
        ┌───────────┐
a ────→ │ [1, 2, 3] │
        └───────────┘
             ↑
b ───────────┘
```

`a` 和 `b` 都指向**同一個 List**。

---

所以：

```python
b[0] = 2
```

原本：

```python
[1, 2, 3]
```

會變成：

```python
[2, 2, 3]
```

所以：

```python
print(a)
print(b)
```

兩個都是：

```text
[2, 2, 3]
```

---

# 1️⃣3️⃣ `.copy()`：真的複製一份 📄

如果希望：

> a 有自己的 List
> b 也有自己的 List

可以使用：

```python
.copy()
```

例如：

```python
a = [1, 2, 3]

b = a.copy()

b[0] = 2

print(a)
print(b)
```

結果：

```text
[1, 2, 3]
[2, 2, 3]
```

因為現在變成：

```text
a → [1, 2, 3]

b → [2, 2, 3]
```

兩個是不同的 List。

---

## 🧠 超重要比較

| 寫法           | 意思                    |
| -------------- | ----------------------- |
| `b = a`        | 兩個名字指向同一個 List |
| `b = a.copy()` | 另外複製一個 List       |

### 記憶法：

> `=` → 一起用同一個箱子 📦
> `.copy()` → 再影印一個箱子 📦📦

---

# 1️⃣4️⃣ `append()`：加入新元素 ➕

假設：

```python
L = [1, 2, 3]
```

如果使用：

```python
L.append(4)
```

會變成：

```python
[1, 2, 3, 4]
```

所以：

```python
append()
```

的工作就是：

> 把新東西加到 List **最後面**。

---

例如：

```python
fruit = ["apple", "banana"]

fruit.append("orange")

print(fruit)
```

得到：

```python
["apple", "banana", "orange"]
```

---

# 1️⃣5️⃣ `remove()`：按照「東西」刪除 ❌

例如：

```python
L = [1, 2, 3, "a", "b", "c"]

L.remove("a")

print(L)
```

得到：

```python
[1, 2, 3, "b", "c"]
```

---

`remove()` 是：

> 「我要刪掉這個東西。」

例如：

```python
L.remove("a")
```

就是：

> 幫我找到 `"a"`，然後刪掉它。

---

## 如果有很多個 `"a"` 呢？

```python
L = ["a", "b", "a", "c"]
L.remove("a")
```

只會刪掉**第一個找到的 `"a"`**。

結果：

```python
["b", "a", "c"]
```

---

⚠️ 如果想刪除全部 `"a"`，不建議一邊：

```python
for i in L:
```

一邊：

```python
L.remove(i)
```

因為 List 在走訪的時候同時變短，有可能漏掉資料。

初學可以使用：

```python
while "a" in L:
    L.remove("a")
```

例如：

```python
L = ["a", "a", "b", "a"]

while "a" in L:
    L.remove("a")

print(L)
```

結果：

```text
['b']
```

---

# 1️⃣6️⃣ `pop()`：按照 Index 刪除 🗑️

`remove()` 是：

> 按照「內容」刪。

`pop()` 是：

> 按照「位置」刪。

---

例如：

```python
L = [1, 2, 3, "a", "b", "c"]

L.pop(0)
```

Index `0` 是：

```text
1
```

所以變成：

```python
[2, 3, "a", "b", "c"]
```

---

如果沒有寫 Index：

```python
L.pop()
```

會刪掉：

> **最後一個元素**

---

## ⭐ `remove()` vs `pop()`

| 指令          | 你告訴 Python 什麼？ |
| ------------- | -------------------- |
| `remove("a")` | 我要刪掉 `"a"`       |
| `pop(0)`      | 我要刪掉 Index `0`   |
| `pop()`       | 我要刪掉最後一個     |

### 🧠 記憶方式

```python
remove("蘋果")
```

👉 找「東西」

```python
pop(2)
```

👉 找「位置」

---

# 1️⃣7️⃣ `sort()`：把資料排序 📊

假設：

```python
L = [1, 3, 2, 4, 5]
```

使用：

```python
L.sort()
```

變成：

```python
[1, 2, 3, 4, 5]
```

也就是：

> 預設從小排到大。

---

完整程式：

```python
L = [1, 3, 2, 4, 5]

L.sort()

print(L)
```

輸出：

```text
[1, 2, 3, 4, 5]
```

---

⚠️ `sort()` 會直接改掉原本的 List。

例如：

```python
L = [3, 1, 2]

L.sort()

print(L)
```

原本：

```text
[3, 1, 2]
```

已經變成：

```text
[1, 2, 3]
```

---

# 1️⃣8️⃣ Streamlit 的 `st.columns()` 🖥️

以前我們寫：

```python
st.button("按鈕1")
st.button("按鈕2")
```

通常會上下排列：

```text
[按鈕1]

[按鈕2]
```

但如果想要：

```text
[按鈕1]    [按鈕2]
```

就可以使用：

```python
st.columns()
```

---

# 1️⃣9️⃣ 建立兩個 Columns

```python
col1, col2 = st.columns(2)
```

意思是：

> 把畫面分成兩欄。

就像：

```text
┌──────────┬──────────┐
│   col1   │   col2   │
│          │          │
└──────────┴──────────┘
```

---

然後：

```python
col1.button("按鈕1", key="btn1")
col2.button("按鈕2", key="btn2")
```

會變成：

```text
┌──────────┬──────────┐
│ [按鈕1] │ [按鈕2] │
└──────────┴──────────┘
```

---

# 2️⃣0️⃣ Columns 還可以設定寬度比例

```python
col1, col2 = st.columns([1, 2])
```

代表：

```text
col1 : col2
  1  :  2
```

所以第二欄大約是第一欄的兩倍寬。

可以想像：

```text
┌───────┬──────────────┐
│ col1  │     col2     │
└───────┴──────────────┘
```

---

三欄：

```python
col1, col2, col3 = st.columns([1, 2, 3])
```

代表：

```text
col1 : col2 : col3
  1  :  2   :  3
```

第三欄最寬。

---

# 2️⃣1️⃣ 使用 List 管理很多 Columns

```python
cols = st.columns(4)
```

其實 `cols` 很像一個 List：

```text
cols[0]
cols[1]
cols[2]
cols[3]
```

也就是四個欄位。

---

所以可以使用：

```python
for i in range(len(cols)):
    with cols[i]:
        st.button(
            f"按鈕{i + 1}",
            key=f"btn{i + 10}"
        )
```

這樣就不用一個一個寫：

```python
col1
col2
col3
col4
```

---

### 🧠 這就是程式設計很重要的想法：

> 如果事情一直重複，就想想看能不能用 `for` 迴圈完成！

---

# 2️⃣2️⃣ `with col1:` 是什麼？

以前可以寫：

```python
col1.button("按鈕1")
```

但如果想在 `col1` 裡面放很多東西，就可以寫：

```python
with col1:
    st.button("按鈕1")
    st.write("Hello")
    st.balloons()
```

意思就是：

> 「接下來這些東西全部放進 col1 裡面。」

---

例如：

```python
col1, col2 = st.columns([1, 2])

with col1:
    if st.button("按鈕1", key="btn8"):
        st.balloons()

    st.write("這是 col1")

with col2:
    st.button("按鈕2", key="btn9")
    st.write("這是 col2")
```

可以想像成：

```text
┌──────────┬──────────────────┐
│ 按鈕1   │ 按鈕2            │
│ 文字    │ 文字              │
│ 🎈      │                   │
└──────────┴──────────────────┘
```

---

# 2️⃣3️⃣ 為什麼 Button 要有 `key`？ 🔑

例如：

```python
st.button("按鈕1", key="btn1")
```

`key` 可以想像成：

> 每個 Streamlit 元件的「身分證號碼」。

例如：

```python
key="btn1"
key="btn2"
key="btn3"
```

這樣 Streamlit 才知道：

> 「喔！這是三個不同的按鈕。」

---

如果有很多一樣名字的 Button，使用：

```python
key=
```

尤其重要。

---

# 2️⃣4️⃣ `f"..."`：把變數放進文字裡

例如：

```python
i = 3

st.button(f"按鈕{i}")
```

會變成：

```text
按鈕3
```

---

所以：

```python
for i in range(3):
    st.button(f"按鈕{i + 1}")
```

會產生：

```text
按鈕1
按鈕2
按鈕3
```

這種寫法叫：

> **f-string**

---

## 🧠 記憶方式

先寫：

```python
f""
```

再把變數放進：

```python
{}
```

例如：

```python
name = "Jack"

print(f"Hello {name}")
```

結果：

```text
Hello Jack
```

---

# 2️⃣5️⃣ 為什麼 Columns 放在 `for` 裡結果不同？

這一段：

```python
col1, col2 = st.columns(2)

with col1:
    st.button("按鈕1")
    st.button("按鈕2")
    st.button("按鈕3")

with col2:
    st.write("這是col2")
    st.write("這是col2")
    st.write("這是col2")
```

是：

> 先建立 **一組兩欄**，再一直往欄位下面放東西。

---

看起來像：

```text
┌───────────┬───────────┐
│ 按鈕1    │ 文字       │
│ 按鈕2    │ 文字       │
│ 按鈕3    │ 文字       │
└───────────┴───────────┘
```

---

但是：

```python
for i in range(3):
    col1, col2 = st.columns(2)

    with col1:
        st.button(f"按鈕{i + 1}", key=f"{i + 4}")

    with col2:
        st.write(f"這是col2_{i + 4}")
```

代表：

> 每跑一次迴圈，就重新建立一組 Columns。

比較像：

```text
┌──────────┬───────────┐
│ 按鈕1   │ 文字1      │
└──────────┴───────────┘

┌──────────┬───────────┐
│ 按鈕2   │ 文字2      │
└──────────┴───────────┘

┌──────────┬───────────┐
│ 按鈕3   │ 文字3      │
└──────────┴───────────┘
```

這個差別很重要。

---

# 2️⃣6️⃣ `st.text_input()`：讓使用者輸入文字 ⌨️

如果要讓使用者輸入文字，可以使用：

```python
st.text_input()
```

例如：

```python
text = st.text_input(
    "請輸入文字",
    value="這是預設文字"
)
```

畫面會出現：

```text
請輸入文字

[ 這是預設文字                  ]
```

---

## `value=` 是什麼？

```python
value="這是預設文字"
```

代表：

> 使用者還沒有輸入以前，輸入框先放這段文字。

---

# 2️⃣7️⃣ 把使用者輸入的文字存起來

```python
text = st.text_input("請輸入文字")
```

假設使用者輸入：

```text
Hello
```

那麼：

```python
text
```

就會變成：

```python
"Hello"
```

所以：

```python
st.write(f"你輸入的文字是：{text}")
```

會顯示：

```text
你輸入的文字是：Hello
```

---

# 📚 今天最重要的 List 指令整理

| 指令          | 功能            | 範例            |
| ------------- | --------------- | --------------- |
| `L[0]`        | 取得一個元素    | `L[0]`          |
| `L[1:4]`      | 切片            | Index 1～3      |
| `len(L)`      | 計算元素數量    | `len(L)`        |
| `L.append(x)` | 加到最後面      | `L.append(4)`   |
| `L.remove(x)` | 按照內容刪除    | `L.remove("a")` |
| `L.pop(i)`    | 按照 Index 刪除 | `L.pop(0)`      |
| `L.pop()`     | 刪除最後一個    | `L.pop()`       |
| `L.sort()`    | 排序            | 小 → 大         |
| `L.copy()`    | 複製 List       | `b = a.copy()`  |

---

# 🖥️ 今天最重要的 Streamlit 指令

| 指令                | 功能               |
| ------------------- | ------------------ |
| `st.title()`        | 顯示標題           |
| `st.write()`        | 顯示資料           |
| `st.markdown()`     | 顯示 Markdown      |
| `st.code()`         | 顯示程式碼樣式文字 |
| `st.number_input()` | 輸入數字           |
| `st.text_input()`   | 輸入文字           |
| `st.button()`       | 建立按鈕           |
| `st.columns()`      | 將畫面分成很多欄   |
| `st.balloons()`     | 顯示氣球動畫 🎈    |

---

# ⭐ 今天最容易考的 8 個重點

### ① List 的 Index 從多少開始？

```text
0
```

---

### ② `len(L)` 是什麼？

> List 裡總共有幾個元素。

---

### ③ `append()` 放在哪裡？

> List 的最後面。

---

### ④ `remove()` 和 `pop()` 差在哪裡？

```text
remove → 看內容
pop    → 看 Index
```

---

### ⑤ `b = a` 和 `b = a.copy()` 差在哪？

```text
b = a
→ 共用同一個 List

b = a.copy()
→ 各自有自己的 List
```

---

### ⑥ `sort()` 做什麼？

> 將 List 排序，預設小到大。

---

### ⑦ `st.columns([1, 2])` 是什麼？

> 建立兩欄，而且第二欄是第一欄的約 2 倍寬。

---

### ⑧ `st.text_input()` 是什麼？

> 建立可以讓使用者輸入文字的輸入框。

---

# 🧩 小測驗

### 第 1 題

```python
L = [10, 20, 30, 40]

print(L[2])
```

答案：

```text
30
```

因為：

```text
10 → index 0
20 → index 1
30 → index 2
40 → index 3
```

---

### 第 2 題

```python
L = [1, 2, 3]
L.append(4)

print(L)
```

答案：

```python
[1, 2, 3, 4]
```

---

### 第 3 題

```python
L = ["a", "b", "c"]

L.pop(1)

print(L)
```

答案：

```python
["a", "c"]
```

因為 Index `1` 是 `"b"`。

---

### 第 4 題

```python
a = [1, 2, 3]
b = a

b[0] = 100

print(a)
```

答案：

```python
[100, 2, 3]
```

因為 `a` 和 `b` 指向同一個 List。

---

### 第 5 題

```python
a = [1, 2, 3]
b = a.copy()

b[0] = 100

print(a)
```

答案：

```python
[1, 2, 3]
```

因為 `.copy()` 已經另外複製一份。

---

# 🎯 今天一句話總結

> **今天學會了用 `for` 做圖形、用 List 管理很多資料，再用 `append / remove / pop / sort / copy` 修改 List，最後利用 Streamlit 的 `columns` 和 `text_input` 做出更漂亮、更像真正 App 的網頁介面。** 🐍💻
