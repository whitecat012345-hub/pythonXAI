import random as rm

ans=rm.randint(1,100) #隨機產生1~100的整數
max=100 #設定最大值
min=1 #設定最小值
while True:#無窮回圈
    #可以吧你想要測試的程式碼放在try裡面，如果成是了錯誤，就會執行except裡面的程式碼
    # try跟except是一對的最少要有一個try跟一個except，也可以有多個except
    try:
        num=int(input(f'請輸入{min}~{max}的整數:')) 
    except: #如果輸入的不是數字
        print('請輸入數字')
        continue #跳出本次回圈，繼續下一次回圈

    if num<0 or num>100: #如果輸入的數字不在1~100之間
        print('請輸入1~100的整數')
    elif num>ans: #如果輸入的數字大於答案
        print('太大了')
        if num<max: #如果輸入的數字大於最大值
            max=num #將最大值改為輸入的數字
    elif num<ans: #如果輸入的數字小於答案
        print('太小了')
        if num>min: #如果輸入的數字小於最小值
            min=num #將最小值改為輸入的數字
    else: #如果輸入的數字等於答案
        print('恭喜你答對了')
        break #跳出回圈
