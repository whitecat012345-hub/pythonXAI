#比較運算子，只能同樣類型作比較
print(1 == 1) # True
print(1 == 2) # False
print(1 != 1) # False
print(1 != 2) # True
print(1 > 2) # False
print(1 < 2) # True
print(1 >= 2) # False

#邏輯運算子
#and運算子，只要一個條件為False，就是False
print(True and True) # True
print(True and False) # False
print(False and False) # False

#or運算子，只要一個條件為True，就是True
print(True or True) # True
print(True or False) # True
print(False or False) # False

#not運算子，將布林值反轉
print(not True) # False
print(not False) # True

#密碼門檢查
password = input("請輸入密碼:")
if password == "123456":
    print("歡迎sophia")
if password == "12356":
    print("hello,sam")
if password == "12345":
    print("hello,apple")
else:
    print("密碼錯誤")
#連續使用if跟使用if,elif,else的差別
#elif可以排除前前面有判斷過的條件，所以判斷條件的複雜難度會降低，程式碼也會比較簡潔
#但是如果使用多個if，來做獨立判斷，則每個if都會被執行，所以效率較低

h=float(input('enter your 身高，公尺'))
w=int(input('enter your 體重'))
bmi = w/h**2
if bmi < 18.5:
    print("體重過輕")
elif 18.5< bmi < 24:
    print("體重正常")
else:
    print("體重過重")