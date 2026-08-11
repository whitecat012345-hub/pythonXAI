#for迴圈
#for會搭配in使用，in後面接一個有範圍的東西
#range(5)會產生0~4的數字，不包含5
#i是for迴圈的變數，可以自己取名
#迴圈每回合從範圍取出一個資料
for i in range(5):
    print(i) 

#range可以設定初始值與結束值，不包含結束值
#range(1, 5)會產生1~4
for i in range(1, 5):
    print(i)

#range可以設定初始值、結束值與間隔值，不包含結束值
#range(1, 10, 2)會產生1, 3, 5, 7, 9
for i in range(1, 10, 2):
    print(i)

for i in range(5):
    a = i * 2 #將i乘2存a
    print(a) #在終端機顯示a存的值