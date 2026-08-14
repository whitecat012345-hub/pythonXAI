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

with st.expander('class三課堂筆記'):
    st.write(
        '''
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

'''
    )

with st.expander('class四課堂筆記'):
    st.write(
        '''
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

* `col1` → 1 份
* `col2` → 2 份
* `col3` → 3 份

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

* `for`
* `range()`
* `len()`
* List
* `st.columns()`

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

| 指令         | 意思        |
| ---------- | --------- |
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

| 指令                 | 功能                  |
| ------------------ | ------------------- |
| `st.columns(2)`    | 📐 把畫面分成 2 欄        |
| `with col1:`       | 📦 把東西放進指定欄位        |
| `st.text_input()`  | ⌨️ 讓使用者輸入文字         |
| `st.session_state` | 🧠 記住 Streamlit 資料  |
| `st.rerun()`       | 🔄 重新執行網頁           |
| `.append()`        | ➕ List 最後加入資料       |
| `.pop()`           | 🗑️ 刪除資料            |
| `+=`               | ➕ 加完存回去             |
| `while`            | 🔁 條件成立就一直重複        |
| `while True`       | ♾️ 無限回圈             |
| `break`            | 🛑 結束整個回圈           |
| `continue`         | ⏭️ 跳過這一次            |
| `try`              | 🧪 試著執行             |
| `except`           | 🚑 發生錯誤時處理          |
| `rm.randrange()`   | 🎲 隨機選數字，不包含結尾      |
| `rm.randint()`     | 🎲 隨機整數，包含頭尾        |
| `dict`             | 📖 用 Key 找 Value    |
| `.keys()`          | 🔑 取得所有 Key         |
| `.values()`        | 📦 取得所有 Value       |
| `.items()`         | 🔑📦 同時取得 Key、Value |
| `sum()`            | ➕ 數字全部加起來           |
| `len()`            | 📏 計算數量             |
| `st.image()`       | 🖼️ 顯示圖片            |

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

'''
    )


with st.expander ('class 5 notes'):
    st.write(
        '''
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

| 指令              | 小學生版解釋             |
| --------------- | ------------------ |
| `import openai` | 找 OpenAI 小幫手來使用 AI |
| `import os`     | 找電腦系統小幫手           |
| `load_dotenv()` | 打開 `.env` 秘密資料夾    |
| `os.getenv()`   | 從秘密資料夾拿資料          |

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

* 銀行密碼不能給別人
* 遊戲帳號密碼不能給別人
* API Key 也不能放在公開的程式碼裡

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
| ----------- | ------ |
| `system`    | 老師 📋  |
| `user`      | 使用者 👦 |
| `assistant` | AI 🤖  |

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

* 🍎 蘋果
* 🍌 香蕉
* 🍊 橘子
* 商品圖片
* 商品價格
* 商品庫存
* 購買按鈕
* 補充庫存

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

| 指令       | 意思  | 例子      |
| -------- | --- | ------- |
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

| 指令                  | 小學生記法              |
| ------------------- | ------------------ |
| `import`            | 找工具來幫忙 🧰          |
| `input()`           | 讓使用者輸入 ⌨️          |
| `while True`        | 一直重複 🔄            |
| `break`             | 停止迴圈 🛑            |
| `if`                | 如果…… 🤔            |
| `else`              | 不然的話……             |
| `for`               | 一個一個做 🔁           |
| `append()`          | 在清單最後加入東西 ➕        |
| `list()`            | 建立清單 📋            |
| `{}`                | 字典 Dictionary 📖   |
| `st.session_state`  | Streamlit 的記憶背包 🧳 |
| `st.chat_message()` | 顯示聊天泡泡 💬          |
| `st.chat_input()`   | 聊天輸入框 ⌨️           |
| `st.columns()`      | 把網頁分欄 🏠           |
| `st.selectbox()`    | 下拉選單 🔽            |
| `st.number_input()` | 數字輸入框 🔢           |
| `st.button()`       | 按鈕 🔘              |
| `st.image()`        | 顯示圖片 🖼️           |
| `st.success()`      | 成功訊息 ✅             |
| `st.error()`        | 錯誤訊息 ❌             |
| `st.rerun()`        | 重新跑一次程式 🔄         |
| `.keys()`           | 找字典裡所有鑰匙 🔑        |
| `+=`                | 加上去 ➕              |
| `-=`                | 減掉 ➖               |

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

'''
    )