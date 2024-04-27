#設定標準輸出為utf-8的格式, 避免中文為亂碼
import sys
sys.stdout.reconfigure(encoding='utf-8')

#print
pet = "kyle's dog"
print(f'variable pet: {pet}')


#list 同一個list可以儲存不同的資料型態
list1 = [1,3,"test",True,False,88.9]
list1.append(0.5)

#tuple 與list非常相似, 差異在於tuple一但被創建後, 無法新增, 修改, 刪除
tuple1 = (1,2,"abc",True)
#tuple1[0] = 8 這段會出錯

#function example1
def add(num1, num2):
    result = num1 + num2
    return result
receive = add(5,8)
print("receive is: " + str(receive)) #str() 將參數轉字串

#function example2
def sum(num1, num2):
    answer = num1 / num2
result = sum(99,1)
print(result) #None ==> 如果函數沒有return, 則系統會預設回傳None

#if else
num1 = 90
if(num1 == 100 and not(50 == 80) or "a" == "b"):
    print("in if")
elif(num1 == 90 and not(50 == 80)):
    print("in elif") #會到這條
else:
    print("in else")

#dictionary 就是java的Map, 以key value的形式儲存資料
dict1 = {"香蕉":"banana", 0:"apple"}
print(dict1[0]) #0是key, 不是index
print(dict1["香蕉"])

#while
i = 1
while(i <= 5):
    print("i = " + str(i))
    i += 1
    
#for
for l in list1:
    print("list1= " + str(l))
# for in range
for x in range(5): # ==> 所以可以用list的length來迭代, 不會超過list的index
    print(x) # 0 ~ 4
    
#for nested
twoDemisonList = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for row in twoDemisonList:
    for col in row:
        print(col) #123456789
        
#for advanced
x = [i**2 for i in range(10)]
print(f'for advanced {x}')

#enumerate
x = ["apple","banana","ceil","demand","factory"]
for ele, idx in enumerate(x):
    print(f'element: {ele}, idx: {idx}')


#open file
#mode="r" 讀取, mode="a" 覆寫, mode="a" 附加
#加上with可以類似像區域函數的概念結束後自動關閉此檔案, 省去file.close()的功夫 
with open("123.txt", mode="a", encoding="utf-8") as file:
    file.write("\n你好啊")
    
#module即為python的檔案, ex: tool.py
import module_tool as tl#無須加上副檔名 ==> 引入同自己寫的tool module, 然後命別名為tl
print(tl.name) #小白
max_number = tl.max_num(99,1038784,-34894)
print("最大的數字為: " + str(max_number))

from module_tool import max_num as compare #從module tool 只引入 function max_num 並別名為compare
result = compare(-9,48,57769)
print("只引入函數來比較大小: " + str(result))


#可以查內建模組的路徑 ==> 結尾是lib的路徑
print(sys.path) 



#類別, 繼承
from class_student import Student
s1 = Student("kyle", 35, "台科大")
s2 = Student("grass", 31, "彰師大")
print("s1 學生: " + s1.print_name() + ",年齡: " + str(s1.print_age()) + ",學校: " + s1.print_school())
print("s2 學生: " + s2.print_name() + ",年齡: " + str(s2.print_age()) + ",學校: " + s2.print_school())



#pandas
import pandas as pd
df1 = pd.DataFrame({
    "id": [0,1,2],
    "student": ["kyle","grass","sandra"],
    "score": [100,99,60]
              })
print(df1.head(2))
