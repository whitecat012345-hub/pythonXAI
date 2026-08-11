'''
這是多行註解
'''

#這試單行註解
print("Hello, World!")   #print是在中端機顯示文字的指令
#ctrl+?可以快速註解或取消註解


#基本型態
print(1) #int這是一個變數,-1,0,1,2,3,4,5,6,7,8,9
print(1.5) #float這是一個浮點數
print("Hello") #string這是一個字串
print(True) #bool這是一個布林值，True或False

#變數
a = 10 #新增一個處存空間並取名為a，'a'的功能是將右邊的值10存入邊的a
print(a) #顯示a的值
a = 'apple' #將a的值改為'apple'
print(a) #顯示a的值

#運算子
print(5 + 3) #加法
print(5 - 3) #減法
print(5 * 3) #乘法
print(5 / 3) #除法
print(5 // 3) #整數除法
print(5 % 3) #取餘數
print(5 ** 3) #次方

# 優先順序
# 1. 先算括號內的
# 2. 先算次方
# 3. 先算乘除
# 4. 最後算加減

#字串
print('hello')
print('Hello '+'World') #字串相加
print('Hello '*3) #字串相乘


#字串格式化
name = 'Sophia Lai YouFei'
age = 18
print(f"我的名字是{name}，今年{age}歲") #F-string
#可以將其他變數或其他型態的資料放到f字串裡面的{}，這樣就可以在字串中顯示

print(len('apple')) #len()可以計算字串的長度，'apple'的長度是5
print(len('Hello, World!')) #len()可以計算字串的長度，'Hello, World!'的長度是12
#type()可以查看變數的型態
print(type(1)) #查看1的型態
print(type(1.5)) #查看1.5的型態
print(type('apple')) #查看'apple'的型態
print(type(True)) #查看True的型態

# 型態轉換
print(int(1.0))  # float轉int
print(float(1))  # int轉float
print(str(1))  # int轉str
print(bool(1))  # int轉bool
print(int(1.234))  # float轉int
print(float("1.234"))  # str轉float
print(str(1.234))  # float轉str
print(bool(1.234))  # float轉bool
# print(int("hello"))  # 這行會報錯，因為字串裡面如果有非數字的字元，無法轉換成數字

print('輸入開始')
#imput()可以讓使用者輸入資料，並將輸入的資料存入變數
#()裡面的文字試題是訊息會先顯示在終端機才會等待使用者輸入
a = input('請輸入一些文字:') 
print('輸入結束')
print(int(a) + 10)
print(type(a)) #input()輸入的資料型態都是字串

#3.14*r*r
r = float(input('請輸入半徑: '))
print(3.14 * r * r)