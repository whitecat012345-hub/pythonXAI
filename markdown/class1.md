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
