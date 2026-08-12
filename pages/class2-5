print([])#這是一個空的list
print([1,2.3])#這是一個有三個元素的list
print([1,2,3,'a','b','c'])#這是一個有六個元素的list
print([1,2,3,['a','b','c']])#這是一個有四個元素的list
print([1,True,'a',1.23])#這是一個有四個元素的list

#list 讀取元素，元素的index從0開始
L=[1,2,3,'a','b','c']
print(L[0]) #1
print(L[1]) #2
print(L[2]) #3
print(L[3]) #'a'

L=[1,2,3,'a','b','c']
#取index 0 到最後，每次取兩個元素，所以是[1,3,'b']
print(L[::2])
#取index 1到3的元素，不包含index 4 ，所以是[2,3,'a']
print(L[1:4])
#取index 1~3 的元素不包含index 4 ，並每次取兩個元素，所以是[2,'a']
print(L[1:4:2])
#跟range一樣的用法，只是符號不同

#list取長度，也就是list中有幾個元素，不是index的最大值
L=[1,2,3,'a','b','c']
print(len(L))

# nest走訪元素
#可以透過取得index的方式來找到list中的資料
#也可以直接把list當做一個範圍來取得資料
#這兩種方式都可以，但是看使用者的情境是否會需要index來決定要用哪一種方式
L=[1,2,3,'a','b','c']
for i in range(0,len(L),2):
    print(L[i])
for i in L:
    print(i)

# call by value
a = 1
b = a  # 複製a的值給b
b = 2
print(a, b)

# call by reference
a = [1, 2, 3]
b = a  # 把a跟b指向同一個記憶體位置，所以改變b的值，a也會跟著改變
b[0] = 2
print(a, b)

a = [1, 2, 3]
b = a.copy()  # 複製a的值給b，但是b跟a指向不同的記憶體位置
b[0] = 2
print(a, b)

# list的append
L=[1,2,3]
L.append(4)#把字加到L的最後面
print(L)

# list的移除元素方式有兩種
#1.如果想一使用remove，可以移除指定的元素
L=[1,2,3,'a','b','c']
L.remove('a')#移除第一個a
#代表remove會從頭開始找，找到第一個符合的元素就會移除
#如果想要移除所有的符合元素可以使用回圈
for i in L :
    if i == 'a':
        L.remove(i)

#2.使用pop，可以移除指定的index的元素
L=[1,2,3,'a','b','c']
L.pop(0)#移除index 0的元素
#代表pop會移除指定的index的元素
#如果不指定index，則會移除最後一個元素
L.pop()#移除最後一個元素
print(L)

# sort：將 List 中的元素進行排序，預設是由小到大（升序排列）
# 注意：這個方法會直接修改原本的 List，不會產生新的 List
L = [1, 3, 2, 4, 5]
L.sort()
print(L)