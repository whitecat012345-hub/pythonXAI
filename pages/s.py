import random
import streamlit as st

# 頁面基本設定
st.set_page_config(page_title="Streamlit 2048 遊戲", page_icon="🎮", layout="centered")

# 自訂 CSS 樣式
st.markdown(
    """
    <style>
    .stApp {
        background-color: #faf8ef;
    }
    .main-title {
        text-align: center;
        color: #776e65;
        font-family: 'Helvetica Neue', Arial, sans-serif;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .score-board {
        background-color: #bbada0;
        color: white;
        padding: 10px 20px;
        border-radius: 6px;
        text-align: center;
        font-weight: bold;
        font-size: 20px;
    }
    .grid-container {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        grid-gap: 12px;
        background-color: #bbada0;
        padding: 12px;
        border-radius: 8px;
        margin-top: 15px;
    }
    .tile {
        height: 80px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 28px;
        font-weight: bold;
        border-radius: 5px;
        color: #776e65;
    }
    /* 不同數字的顏色設定 */
    .tile-0 { background-color: #ccc0b4; color: transparent; }
    .tile-2 { background-color: #eee4da; }
    .tile-4 { background-color: #ede0c8; }
    .tile-8 { background-color: #f2b179; color: #f9f6f2; }
    .tile-16 { background-color: #f59563; color: #f9f6f2; }
    .tile-32 { background-color: #f67c5f; color: #f9f6f2; }
    .tile-64 { background-color: #f65e3b; color: #f9f6f2; }
    .tile-128 { background-color: #edcf72; color: #f9f6f2; font-size: 24px; }
    .tile-256 { background-color: #edcc61; color: #f9f6f2; font-size: 24px; }
    .tile-512 { background-color: #edc850; color: #f9f6f2; font-size: 24px; }
    .tile-1024 { background-color: #edc53f; color: #f9f6f2; font-size: 20px; }
    .tile-2048 { background-color: #edc22e; color: #f9f6f2; font-size: 20px; }
    </style>
    """,
    unsafe_allow_html=True,
)


# --- 遊戲邏輯函數 ---
def init_board():
    """初始化 4x4 棋盤並隨機產生兩個數字"""
    board = [[0] * 4 for _ in range(4)]
    add_random_tile(board)
    add_random_tile(board)
    return board


def add_random_tile(board):
    """在空白格子隨機生成 2 (90%機率) 或 4 (10%機率)"""
    empty_tiles = [
        (r, c) for r in range(4) for c in range(4) if board[r][c] == 0
    ]
    if empty_tiles:
        r, c = random.choice(empty_tiles)
        board[r][c] = 2 if random.random() < 0.9 else 4


def compress(row):
    """將非零數字往左靠攏"""
    new_row = [num for num in row if num != 0]
    return new_row + [0] * (4 - len(new_row))


def merge(row):
    """相鄰相同的數字合併，並計算得分"""
    score = 0
    for i in range(3):
        if row[i] != 0 and row[i] == row[i + 1]:
            row[i] *= 2
            row[i + 1] = 0
            score += row[i]
    return row, score


def move_left(board):
    """向左移動並合併"""
    new_board = []
    total_score = 0
    for row in board:
        compressed = compress(row)
        merged, score = merge(compressed)
        final_row = compress(merged)
        new_board.append(final_row)
        total_score += score
    return new_board, total_score


def rotate(board):
    """順時針旋轉矩陣（透過旋轉將上下右方向的移動轉化為向左移動）"""
    return [list(r) for r in zip(*board[::-1])]


def make_move(direction):
    """根據方向執行移動操作"""
    board = st.session_state.board
    rotations = {"Left": 0, "Up": 3, "Right": 2, "Down": 1}[direction]

    # 轉到左邊視角
    for _ in range(rotations):
        board = rotate(board)

    new_board, score_gained = move_left(board)

    # 轉回原始方向
    for _ in range((4 - rotations) % 4):
        new_board = rotate(new_board)

    # 若盤面有變化，更新狀態並新增隨機塊
    if new_board != st.session_state.board:
        st.session_state.board = new_board
        st.session_state.score += score_gained
        add_random_tile(st.session_state.board)


# --- State 初始化 ---
if "board" not in st.session_state:
    st.session_state.board = init_board()
if "score" not in st.session_state:
    st.session_state.score = 0

# --- UI 渲染 ---
st.markdown("<h1 class='main-title'>🎮 Streamlit 2048</h1>", unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])
with col1:
    st.write("使用下方的按鈕控制滑動，將相同的數字合併，湊出 **2048**！")
with col2:
    st.markdown(
        f"<div class='score-board'>得分<br>{st.session_state.score}</div>",
        unsafe_allow_html=True,
    )

# 繪製 4x4 遊戲棋盤
grid_html = "<div class='grid-container'>"
for r in range(4):
    for c in range(4):
        val = st.session_state.board[r][c]
        val_class = f"tile-{val}" if val <= 2048 else "tile-2048"
        display_text = str(val) if val != 0 else ""
        grid_html += (
            f"<div class='tile {val_class}'>{display_text}</div>"
        )
grid_html += "</div>"

st.markdown(grid_html, unsafe_allow_html=True)

st.write("")

# 控制按鈕介面
btn_col1, btn_col2, btn_col3 = st.columns([1, 1, 1])

with btn_col2:
    if st.button("⬆️ 向上", use_container_width=True):
        make_move("Up")
        st.rerun()

btn_left, btn_restart, btn_right = st.columns([1, 1, 1])

with btn_left:
    if st.button("⬅️ 向左", use_container_width=True):
        make_move("Left")
        st.rerun()

with btn_restart:
    if st.button("🔄 重新開始", use_container_width=True):
        st.session_state.board = init_board()
        st.session_state.score = 0
        st.rerun()

with btn_right:
    if st.button("➡️ 向右", use_container_width=True):
        make_move("Right")
        st.rerun()

btn_down_col1, btn_down_col2, btn_down_col3 = st.columns([1, 1, 1])
with btn_down_col2:
    if st.button("⬇️ 向下", use_container_width=True):
        make_move("Down")
        st.rerun()