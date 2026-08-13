#算數指定運算子
a=1
a+=1 #a=a+1
print(a) #2
a-=1 #a=a-1
print(a) #1
a*=2 #a=a*2
print(a) #2
a/=2 #a=a/2
print(a) #1
a//=2 #a=a//2
print(a) #0
a%=2 #a=a%2
print(a) #0
a**=2 #a=a**2
print(a) #0

# 優先順序
# 1. () 括號
# 2. ** 次方
# 3. * / // % 乘 除 取商 取餘數
# 4. + - 加 減
# 5. == != > < >= <= 比較運算子
# 6. not
# 7. and
# 8. or
# 9. = += -= *= /= //= %= **= 算數指定運算子


#while回圈
#while會搭配一個條件是來使用
i=0
while i<5:
    print(i)
    i+=1 #i=i+1

#break可以強制跳出回圈
#先判斷break的條件，若成立就跳出回圈，若不成立就繼續執行回圈
i=0
while i<5:
    print(i)

    for i in range(5):
        print(i)

    if i==3:
        break #強制跳出回圈
    i+= 1 

for i in range(5):
    print(i)
    if i==3:
          break #強制跳出回圈


import random as rm#匯入renren模組

#rm.randrange()設定抽簽范圍的方式線range()一樣
print(rm.randrange(7)) #0~6
print(rm.randrange(1,7)) #1~6
print(rm.randrange(1,6,2)) #1,3,5

#rm.randint()設定抽簽范圍的方式線range()一樣
#且結束的數字會包含在內
print(rm.randint(1,6)) #1~6

answer = rm.randint(1,100) #設定答案為1~6的隨機數字
min = 1 #設定最小值
max = 100 #設定最大值
while True:
    a=int(input(f"請輸入{min}~{max}的數字:")) #輸入數字
    if answer>a: #若答案大於輸入的數字
        print("太小了") #顯示太小了
        min =a
    elif answer<a: #若答案小於輸入的數字
        print("太大了") #顯示太大了
        max =a
    else: #若答案等於輸入的數字
        print("恭喜答對了") #顯示恭喜答對了
        break #跳出回圈