import streamlit as st
with st.expander("class1 課堂筆記"):
    st.write(
        '''
        # 🐍 Python + Streamlit 入門筆記

## 一、今天學的是什麼？

今天我們用 **Python** 搭配 **Streamlit** 來製作簡單的網頁。

可以把它想成：

- 🐍 **Python**：告訴電腦要做什麼
- 🖥️ **Streamlit**：幫我們把 Python 的內容變成網頁
- ✏️ 我們可以在網頁上放「標題、文字、粗體、斜體、清單、程式碼」等等。

---

# 二、第一步：載入 Streamlit

```python
import streamlit as st
```

這一行非常重要！

它的意思是：

> 「我要使用 Streamlit，而且以後我把它簡稱叫做 `st`。」

所以後面看到：

```python
st.title()
st.write()
st.text()
st.markdown()
```

前面的 `st` 都是在叫 Streamlit 幫我們工作。

💡 可以想像成：

```text
Streamlit → 小名叫 st
```

---

# 三、`st.title()`：顯示大標題

```python
st.title("這是標題")
```

網頁上就會出現一個很大的標題：

# 這是標題

### 記憶方法

`title` 的英文就是「標題」。

所以：

```python
st.title("我的第一個網頁")
```

就是告訴 Streamlit：

> 幫我在網頁上放一個大標題「我的第一個網頁」。

---

# 四、`st.write()`：顯示內容

```python
st.write("大家好！")
```

網頁上就會出現：

大家好！

`st.write()` 是非常常用的指令，因為它可以顯示很多不同的東西。

例如：

### 顯示文字

```python
st.write("我是小明")
```

### 顯示數字

```python
st.write(100)
```

### 顯示計算結果

```python
st.write(10 + 20)
```

結果：

```text
30
```

所以可以把 `st.write()` 想成：

> 📢 「把這個東西顯示在網頁上！」

---

# 五、`st.text()`：顯示純文字

```python
st.text("這是一段文字")
```

`st.text()` 也可以顯示文字，但是它比較簡單，只負責顯示「純文字」。

例如：

```python
st.text("Hello World!")
```

網頁會顯示：

```text
Hello World!
```

### `write` 和 `text` 有什麼不同？

可以這樣記：

| 指令         | 功能         | 能力       |
| ------------ | ------------ | ---------- |
| `st.write()` | 顯示各種內容 | ⭐⭐⭐⭐⭐ |
| `st.text()`  | 顯示純文字   | ⭐⭐       |

所以大部分時候，`st.write()` 會比較方便。

---

# 六、`st.markdown()`：讓文字變漂亮

這是今天很重要的一個指令：

```python
st.markdown()
```

Markdown 是一種「幫文字排版」的方法。

可以做：

- 大標題
- 小標題
- **粗體**
- _斜體_
- 清單
- 分隔線
- 連結
- 程式碼

例如：

```python
st.markdown(
"""
# 我的網頁

大家好！

- 蘋果
- 香蕉
- 西瓜
"""
)
```

這樣 Streamlit 就會幫我們排版成漂亮的網頁。

---

# 七、為什麼有三個引號 `"""`？

你今天的程式裡面有：

```python
st.markdown(
"""
大家好
我是小明
我喜歡 Python
"""
)
```

`"""` 可以用來放「很多行文字」。

如果只有一句話，可以寫：

```python
st.write("大家好")
```

如果有很多行，就可以使用：

```python
"""
第一行
第二行
第三行
第四行
"""
```

💡 記憶方式：

> `" "` → 一般短文字
> `""" """` → 很多行文字

---

# 八、Markdown 的標題

Markdown 可以使用 `#` 製作標題。

## 最大標題

```markdown
# 這是最大標題
```

## 第二大標題

```markdown
## 這是第二大標題
```

## 第三大標題

```markdown
### 這是第三大標題
```

一直到：

```markdown
###### 這是第六大標題
```

### 規則

`#` 越少 → 標題越大
`#` 越多 → 標題越小

| 寫法          | 大小    |
| ------------- | ------- |
| `# 標題`      | 🐘 最大 |
| `## 標題`     | 很大    |
| `### 標題`    | 中等    |
| `#### 標題`   | 小      |
| `##### 標題`  | 更小    |
| `###### 標題` | 🐜 最小 |

---

# 九、Markdown 清單 `-`

如果想製作清單，可以在前面加上 `-`。

例如：

```markdown
- 蘋果
- 香蕉
- 西瓜
```

顯示結果：

- 蘋果
- 香蕉
- 西瓜

所以看到：

```python
st.markdown(
"""
- 這是第一個項目
- 這是第二個項目
- 這是第三個項目
"""
)
```

就是要在網頁上製作一個清單。

---

# 十、Markdown 粗體 `**`

如果想讓文字變成**粗體**：

```markdown
**我是粗體**
```

記住：

> 前面兩顆星星 `**`
> 後面也兩顆星星 `**`

例如：

```python
st.markdown("今天要學 **Python**")
```

顯示：

今天要學 **Python**

---

# 十一、Markdown 斜體 `*`

如果想讓文字變成*斜體*，只要使用一顆星星：

```markdown
_我是斜體_
```

例如：

```python
st.markdown("我喜歡 *Python*")
```

顯示：

我喜歡 _Python_

### 粗體與斜體不要搞混

```text
*文字*     → 斜體
**文字**   → 粗體
```

---

# 十二、Markdown 超連結

今天還學到了：

```markdown
[連結](https://www.example.com)
```

它的結構是：

```text
[想顯示的文字](網址)
```

例如：

```markdown
[Google](https://www.google.com)
```

網頁就會出現一個可以點的「Google」。

---

# 十三、Markdown 分隔線 `---`

如果寫：

```markdown
---
```

就會出現一條水平線。

它可以幫我們把不同的內容分開。

例如：

```markdown
# 第一課

今天學 Python。

---

# 第二課

今天學 Streamlit。
```

看起來就會比較整齊。

---

# 十四、顯示 Python 程式碼

Markdown 還可以把程式碼漂亮地顯示出來。

寫法：

````text
```python
print("Hello World!")
```
````

網頁上會顯示成：

```python
print("Hello World!")
```

其中：

```text
python
```

是在告訴電腦：

> 「這一段是 Python 程式碼。」

這樣 Streamlit 就可以把程式碼顯示得更清楚。

---

# 十五、今天所有重要指令整理 ⭐

| 指令                     | 功能             | 記憶方法               |
| ------------------------ | ---------------- | ---------------------- |
| `import streamlit as st` | 載入 Streamlit   | 我要開始使用 Streamlit |
| `st.title()`             | 顯示大標題       | title = 標題           |
| `st.write()`             | 顯示各種內容     | write = 寫出來         |
| `st.text()`              | 顯示純文字       | text = 文字            |
| `st.markdown()`          | 顯示有排版的文字 | 讓文字變漂亮           |

### Markdown 語法

| 語法           | 功能               |
| -------------- | ------------------ |
| `# 標題`       | 最大標題           |
| `## 標題`      | 第二大標題         |
| `### 標題`     | 第三大標題         |
| `###### 標題`  | 第六大標題         |
| `- 項目`       | 清單               |
| `**文字**`     | **粗體**           |
| `*文字*`       | _斜體_             |
| `[名稱](網址)` | 超連結             |
| `---`          | 分隔線             |
| ` ```python `  | 顯示 Python 程式碼 |

---

# 🧠 十六、最簡單的記憶方式

今天最重要的是記住這 4 個：

```python
st.title("標題")
```

👉 放「大標題」

```python
st.write("內容")
```

👉 放「一般內容」

```python
st.text("文字")
```

👉 放「純文字」

```python
st.markdown("Markdown")
```

👉 放「可以排版的漂亮文字」

---

# 🎮 十七、小練習：做一個「我的自我介紹」網頁

試著自己完成：

````python
import streamlit as st

st.title("我的自我介紹")

st.write("大家好！我是小明。")

st.markdown(
"""
## 我的興趣

- 打籃球
- 玩 Minecraft
- 寫 Python

## 我最喜歡的程式

我最喜歡 **Python**！

---

### 我的第一個 Python 程式

```python
print("Hello World!")
````

"""
)

```

如果這個程式可以成功執行，就代表今天學到的主要內容你已經會用了！🎉

---

# ⭐ 今天的重點一句話

> **Python 負責寫程式，Streamlit 幫我們把程式變成網頁，而 Markdown 可以幫我們把網頁上的文字排得更漂亮。**
```

        '''
    )

with st.expander('class2 notes'):
    st.write(
   '''
# 🐍 Python 小學生入門筆記

## 今天學習：比較、邏輯判斷、if、Streamlit、for 迴圈

---

# 一、比較運算子：比一比誰大、誰小

比較運算子就像數學課的「比較大小」。

比較完之後，Python 會告訴我們答案是：

* `True` 👉 對的、成立
* `False` 👉 錯的、不成立

---

## 1. `==` 等於

注意！

Python 的「等於」要寫：

```python
==
```

不是只有一個 `=`。

```python
print(1 == 1)
```

結果：

```python
True
```

因為 1 的確等於 1。

```python
print(1 == 2)
```

結果：

```python
False
```

因為 1 不等於 2。

---

## 2. `!=` 不等於

`!=` 的意思是：

👉「左右兩邊不一樣嗎？」

```python
print(1 != 1)
```

結果：

```python
False
```

因為 1 和 1 是一樣的。

```python
print(1 != 2)
```

結果：

```python
True
```

因為 1 和 2 不一樣。

---

## 3. `>` 大於

```python
print(1 > 2)
```

結果：

```python
False
```

因為 1 沒有比 2 大。

---

## 4. `<` 小於

```python
print(1 < 2)
```

結果：

```python
True
```

因為 1 比 2 小。

---

## 5. `>=` 大於或等於

```python
print(1 >= 2)
```

結果：

```python
False
```

因為 1 不大於 2，也不等於 2。

---

## 6. `<=` 小於或等於

例如：

```python
print(2 <= 2)
```

結果：

```python
True
```

因為 2 等於 2，所以符合「小於或等於」。

---

## ⭐ 比較運算子整理

| 寫法   | 意思    |
| ---- | ----- |
| `==` | 等於    |
| `!=` | 不等於   |
| `>`  | 大於    |
| `<`  | 小於    |
| `>=` | 大於或等於 |
| `<=` | 小於或等於 |

### 💡 小提醒

`=` 和 `==` 完全不一樣！

```python
a = 10
```

意思是：

👉 把 10 放進 `a` 裡面。

但是：

```python
a == 10
```

意思是：

👉 問 Python：「a 是不是等於 10？」

---

# 二、邏輯運算子

有時候我們不只想檢查一件事情，而是想一次檢查好幾個條件。

這時候就可以使用：

```python
and
or
not
```

---

# 1. `and`：而且

`and` 的意思很像：

👉「這個條件要成立，**而且**另一個條件也要成立。」

只有兩邊全部都是 `True`，答案才會是 `True`。

```python
print(True and True)
```

結果：

```python
True
```

但是：

```python
print(True and False)
```

結果：

```python
False
```

```python
print(False and False)
```

結果：

```python
False
```

### 🧠 記憶方法

`and` 很嚴格：

> 全部都要對！

例如：

「有寫完功課 **而且** 有整理書包，才可以玩。」

只完成其中一件都不行。

---

# 2. `or`：或者

`or` 的意思是：

👉「只要其中一個條件成立就可以。」

```python
print(True or True)
```

結果：

```python
True
```

```python
print(True or False)
```

結果：

```python
True
```

```python
print(False or False)
```

結果：

```python
False
```

### 🧠 記憶方法

`or` 比較寬鬆：

> 只要有一個對就可以！

例如：

「星期六 **或** 星期日可以出去玩。」

只要其中一天符合就可以。

---

# 3. `not`：相反

`not` 會把答案反過來。

```python
print(not True)
```

結果：

```python
False
```

```python
print(not False)
```

結果：

```python
True
```

就像：

```text
True → False
False → True
```

### 🧠 記憶方法

`not` 就像「反轉按鈕」。

---

# 三、if：如果……就……

`if` 是 Python 非常重要的功能。

它可以讓電腦根據不同情況，做不同事情。

生活中的例子：

> 如果下雨，就帶雨傘。

Python 可以寫成：

```python
if 下雨:
    帶雨傘
```

---

# 四、密碼檢查

例如我們想做一個密碼門：

```python
password = input("請輸入密碼:")

if password == "123456":
    print("歡迎 Sophia")
elif password == "12356":
    print("Hello, Sam")
elif password == "12345":
    print("Hello, Apple")
else:
    print("密碼錯誤")
```

程式會先問：

```text
請輸入密碼:
```

使用者輸入的內容會被放進：

```python
password
```

---

## `if`

第一個條件：

```python
if password == "123456":
```

意思是：

👉 如果密碼等於 `"123456"`

就顯示：

```python
print("歡迎 Sophia")
```

---

## `elif`

`elif` 的意思可以想成：

👉「如果前面的不符合，那再看看這個。」

例如：

```python
elif password == "12356":
```

---

## `else`

`else` 的意思是：

👉「前面的條件全部都不符合，就做這件事。」

```python
else:
    print("密碼錯誤")
```

---

# 五、多個 `if` 和 `if / elif / else` 有什麼不同？

這個非常重要！

---

## 方法一：很多個 `if`

```python
if 條件1:
    做事情1

if 條件2:
    做事情2

if 條件3:
    做事情3
```

Python 會：

👉 每一個 `if` 都檢查一次。

也就是說，它們是「各自獨立」的。

---

## 方法二：`if / elif / else`

```python
if 條件1:
    做事情1
elif 條件2:
    做事情2
elif 條件3:
    做事情3
else:
    做其他事情
```

只要找到一個符合的條件，就不會繼續往下檢查。

### ⭐ 所以可以記成：

* 多個 `if` 👉 每一題都要檢查
* `if / elif / else` 👉 找到答案就停止

---

# 六、BMI 計算程式

BMI 可以用身高和體重算出來。

公式是：

```text
BMI = 體重 ÷ 身高²
```

Python：

```python
h = float(input("請輸入身高（公尺）："))
w = int(input("請輸入體重（公斤）："))

bmi = w / h**2
```

---

## `float()`

```python
float()
```

可以把輸入的資料變成「有小數點的數字」。

例如：

```text
1.55
```

---

## `int()`

```python
int()
```

可以把資料變成整數。

例如：

```text
40
```

---

## `**` 次方

```python
h**2
```

意思是：

```text
h × h
```

例如：

```python
2**2
```

就是：

```text
2 × 2 = 4
```

---

# BMI 判斷

可以寫成：

```python
if bmi < 18.5:
    print("體重過輕")
elif bmi < 24:
    print("體重正常")
else:
    print("體重過重")
```

為什麼第二個不用再寫：

```python
bmi >= 18.5
```

呢？

因為如果程式能跑到 `elif`，就代表：

```python
bmi < 18.5
```

已經是 `False` 了。

所以 Python 已經知道 BMI 至少是 18.5。

這就是 `elif` 很方便的地方！

---

# 七、認識 Streamlit

Streamlit 可以幫我們把 Python 程式變成簡單的網頁。

首先要寫：

```python
import streamlit as st
```

意思是：

👉 把 `streamlit` 工具拿進來使用。

而：

```python
as st
```

就是幫它取一個比較短的名字：

```text
streamlit → st
```

以後就不用一直寫：

```python
streamlit.number_input()
```

可以直接寫：

```python
st.number_input()
```

方便很多！

---

# 八、`st.number_input()` 輸入數字

```python
number = st.number_input(
    "請輸入一個數字",
    step=1,
    min_value=0,
    max_value=100
)
```

網頁上會出現一個可以輸入數字的地方。

---

## `min_value`

```python
min_value=0
```

意思是：

👉 最小只能輸入 0。

---

## `max_value`

```python
max_value=100
```

意思是：

👉 最大只能輸入 100。

---

## `step`

```python
step=1
```

代表每次增加或減少：

```text
1
```

例如：

```text
1 → 2 → 3 → 4
```

而不是：

```text
1 → 1.1 → 1.2
```

---

# 九、`st.markdown()`

```python
st.markdown()
```

可以在網頁上顯示文字，而且可以使用 Markdown 語法。

例如：

```python
st.markdown("### 我的成績")
```

會顯示成一個標題。

---

## f-string

例如：

```python
number = 50

st.markdown(f"Your number is: {number}")
```

畫面會顯示：

```text
Your number is: 50
```

這個：

```python
f"...{變數}..."
```

叫做：

👉 **f-string**

它可以把變數放進文字裡。

---

# 十、成績判斷程式

```python
a = st.number_input(
    "請輸入你的分數",
    min_value=0,
    max_value=100,
    step=1
)

if a >= 90:
    st.write("You are A")
elif a >= 80:
    st.write("You are B")
elif a >= 70:
    st.write("You are C")
elif a >= 60:
    st.write("You are D")
else:
    st.write("Keep trying!")
```

如果輸入：

```text
95
```

因為：

```python
95 >= 90
```

所以顯示：

```text
You are A
```

---

如果輸入：

```text
85
```

第一個條件：

```python
85 >= 90
```

不成立。

接著檢查：

```python
85 >= 80
```

成立！

所以顯示：

```text
You are B
```

而且後面的條件就不用再檢查了。

---

# 十一、`st.write()`

```python
st.write()
```

可以把文字或數字顯示在 Streamlit 網頁上。

例如：

```python
st.write("Hello!")
```

網頁顯示：

```text
Hello!
```

---

# 十二、分隔線

```python
st.markdown("---")
```

會在網頁上畫出一條橫線。

可以幫我們把不同內容分開。

---

# 十三、`st.button()` 按鈕

```python
st.button("Click me")
```

可以在網頁上做一顆按鈕。

使用者可以用滑鼠點它。

---

## 按下按鈕會發生什麼？

`st.button()` 會回傳：

```python
True
```

或：

```python
False
```

如果使用者剛剛按下按鈕：

```text
True
```

沒有按：

```text
False
```

所以可以搭配 `if`：

```python
if st.button("Click me"):
    st.write("你按到我了！")
```

---

# 十四、`key` 是什麼？

如果網頁上有很多按鈕，Streamlit 要知道：

👉 哪一顆是哪一顆。

所以可以幫每一顆按鈕取一個獨一無二的名字：

```python
key="button1"
```

例如：

```python
st.button("Click me", key="button1")
```

---

# 十五、氣球效果 `st.balloons()`

```python
if st.button("Click me", key="balloons"):
    st.balloons()
```

按下按鈕後：

🎈🎈🎈

畫面會出現氣球動畫。

---

# 十六、下雪效果 `st.snow()`

```python
if st.button("Click me", key="snow"):
    st.snow()
```

按下按鈕後：

❄️❄️❄️

網頁會出現下雪動畫。

---

# 十七、for 迴圈

如果我們想讓電腦重複做同一件事情很多次，就可以使用：

```python
for
```

例如：

```python
for i in range(5):
    print(i)
```

結果：

```text
0
1
2
3
4
```

---

# 十八、`range(5)`

```python
range(5)
```

會產生：

```text
0, 1, 2, 3, 4
```

### ⚠️ 非常重要

不會包含 5！

所以可以記成：

> `range()` 的結束數字不算！

---

# 十九、for 裡面的 `i`

```python
for i in range(5):
```

這裡的：

```python
i
```

是一個變數。

每一回合，它會拿到不同的數字。

第一回合：

```python
i = 0
```

第二回合：

```python
i = 1
```

第三回合：

```python
i = 2
```

一直到：

```python
i = 4
```

---

## `i` 一定要叫 i 嗎？

不用！

你也可以寫：

```python
for number in range(5):
    print(number)
```

結果一模一樣。

只是程式設計的人很常使用：

```python
i
```

當作迴圈裡面的變數名稱。

---

# 二十、`range(開始, 結束)`

```python
for i in range(1, 5):
    print(i)
```

結果：

```text
1
2
3
4
```

因為：

```python
range(1, 5)
```

意思是：

```text
從 1 開始
到 5 前面停止
```

所以沒有 5。

---

# 二十一、`range(開始, 結束, 間隔)`

```python
for i in range(1, 10, 2):
    print(i)
```

結果：

```text
1
3
5
7
9
```

因為：

```python
range(1, 10, 2)
```

代表：

* 從 `1` 開始
* 到 `10` 前停止
* 每次增加 `2`

所以：

```text
1 → 3 → 5 → 7 → 9
```

---

# 二十二、for 迴圈裡也可以做計算

```python
for i in range(5):
    a = i * 2
    print(a)
```

每一回合：

### 第 1 回合

```python
i = 0
a = 0 * 2
```

所以：

```text
0
```

### 第 2 回合

```python
i = 1
a = 1 * 2
```

所以：

```text
2
```

### 第 3 回合

```python
i = 2
a = 2 * 2
```

所以：

```text
4
```

最後結果：

```text
0
2
4
6
8
```

---

# 🎯 今天最重要的觀念整理

## 1️⃣ 比較

```python
==   等於
!=   不等於
>    大於
<    小於
>=   大於或等於
<=   小於或等於
```

---

## 2️⃣ 邏輯判斷

```python
and
```

👉 全部都要是 `True`

```python
or
```

👉 至少一個是 `True`

```python
not
```

👉 把 `True` 和 `False` 反過來

---

## 3️⃣ 條件判斷

```python
if
elif
else
```

可以想成：

```text
如果……
不然如果……
都不是的話……
```

---

## 4️⃣ Streamlit

今天學到：

```python
import streamlit as st
```

把 Streamlit 載入。

```python
st.number_input()
```

讓使用者輸入數字。

```python
st.markdown()
```

顯示 Markdown 文字。

```python
st.write()
```

在網頁上顯示內容。

```python
st.button()
```

做按鈕。

```python
st.balloons()
```

顯示氣球動畫。

```python
st.snow()
```

顯示下雪動畫。

---

## 5️⃣ for 迴圈

```python
for i in range(5):
    print(i)
```

可以讓程式重複做事情。

### range 最重要規則：

```python
range(5)
```

👉 `0, 1, 2, 3, 4`

```python
range(1, 5)
```

👉 `1, 2, 3, 4`

```python
range(1, 10, 2)
```

👉 `1, 3, 5, 7, 9`

⭐ **結束的數字不包含在裡面！**

---

# 🧠 超簡單口訣

### 比較

> `==` 問一不一樣，`!=` 問是不是不一樣。

### and

> **全部都要對。**

### or

> **一個對就可以。**

### not

> **答案顛倒過來。**

### if

> **如果這樣，就做這件事。**

### elif

> **前面不對，再試這個。**

### else

> **前面都不對，就做這個。**

### for

> **同一件事情重複做好幾次。**

### range

> **從哪裡開始、到哪裡以前停止、每次走幾步。**

'''    )