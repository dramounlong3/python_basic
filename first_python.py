#設定標準輸出為utf-8的格式, 避免中文為亂碼
import json
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


#json轉換
var_test = 88

pytohn_obj = {
    "a": 123,
    "b": 456,
    "c": [1,2,3,4,5],
    "d": False,
    "obj": {
        "x": 1,
        "y": True,
        "jhk": ['aa','bb',33, False],
        25: 99,
        var_test: [9,8, {'66':6}]
    }
}
print(type(pytohn_obj), pytohn_obj)
print("pytohn_obj['c'][2]:", pytohn_obj['c'][2])
print("pytohn_obj['obj']['y']:", pytohn_obj['obj']['y'])
# 由python dict轉json
string_of_json = json.dumps(pytohn_obj)
print(type(string_of_json), string_of_json)
print("string_of_json[4]:", string_of_json[4]) #字串用index指定字元索引
# 由string_of_json轉python_obj
new_python_obj = json.loads(string_of_json)
print("type(new_python_obj):", type(new_python_obj))
print("pytohn_obj['obj']['jhk'][2]:", pytohn_obj['obj']['jhk'][2])
print("pytohn_obj['obj'][25]:", pytohn_obj['obj'][25]) #key值是數字
print("pytohn_obj['obj'][88][2]:", pytohn_obj['obj'][88][2]) #key值是數字變數, 用數字找
print("pytohn_obj['obj'][var_test][2]:", pytohn_obj['obj'][var_test][2]) #key值是數字變數, 用變數找
print("pytohn_obj['obj'][var_test][2]:", pytohn_obj['obj'][var_test][2]['66']) #key值是數字變數, 用變數找


print()
# lambda
def my_func_1(x):
    return x*100
my_func_1_result = my_func_1(77)
print("my_func_1_result", my_func_1_result)
arr = list(range(1, 6)) #不含6
print("arr", arr)
lambda_result = list(map(lambda x: x*100, arr))
print("lambda_result", lambda_result)

#鐵達尼號的範例資料
#計算出每個人是否高於所有人的平均年齡
import seaborn as sns 
data = sns.load_dataset('titanic')
data = data.loc[:, ['who', 'age', 'survived']] #只挑此三種欄位
print("data.head()", data.head())
tmp = data.copy() #複製一份data
print("tmp", tmp)
#原始做法
tmp['avg_age'] = tmp['age'].mean() #新增avg_age欄位, 值為age欄位的平均
tmp['diff_from_avg_age'] = tmp['age'] - tmp['avg_age'] #將每個人的年齡減去平均年齡並存放在新欄位
tmp['if_age_greater_than_avg'] = tmp['diff_from_avg_age'] > 0 #存放每個人的年齡是否大於平均年齡的結果
pd.options.display.max_columns = None
print("tmp\n", tmp)
#應用assign做法
new_data = data.assign( #x就是data
    avg_age = lambda x: x['age'].mean(),
    #以下開始lamda的參數都會有avg_age的欄位
    diff_from_avg_age = lambda x: x['age'] - x['avg_age'],
    if_age_greater_than_avg = lambda x: x['diff_from_avg_age'] > 0
)
print("new_data\n", new_data)

print("who")
group_data = data.groupby('who').apply(lambda x: print(x, "\n"))
gp_data = data.groupby('who') #分組後會得到DataFrameGroupBy的類別
print("gp_data", gp_data)

print()
#藉由man, woman, child分組後, 拿age欄位 做聚合函數計算 => 分別做 最小, 最大....
agg_data = gp_data['age'].agg(['min', 'max', 'mean', 'median'])
print("agg_data", agg_data)

print()
unique_values = data['who'].unique() #類似像把who這個欄位做distinct
print("unique_values", unique_values)

group_survived_man = gp_data.get_group('man') #只能get_group who有的值
print("group_survived_man\n", group_survived_man)

#重新編列row index, 上面會保留原本的row index
group_survived_man_reset_index = gp_data.get_group('man').reset_index()
print("group_survived_man_reset_index\n", group_survived_man_reset_index)

print()
#計算每種類型的人有多少人, child:83人, woman:271人, man:537人
human_count = data.value_counts('who')
print("human_count\n", human_count)
#再將上面的human_count結果拿去相加 => 83+271+537=891
sum_human_count = data.value_counts('who').sum()
print("sum_human_count", sum_human_count)


print()
# apply應用
# 創建DataFrame
data = {'姓名': ['小明', '小華', '小美'],
        '國文成績': [85, 90, 88],
        '數學成績': [92, 88, 95],
        '英文成績': [78, 85, 80]}
df = pd.DataFrame(data)

print(df)

# 定義一個函數，用於計算總成績
def calculate_total(row):
    total_score = row['國文成績'] + row['數學成績'] + row['英文成績']
    return total_score

# 使用apply方法應用自定義函數到每一行，計算每個學生的總成績
df['總成績'] = df.apply(calculate_total, axis=1)

print(df)

print()
def cal_total_by_axis0(col):
    total = col.sum()
    return total
#計算每個人的各科總成績
subject_score = df.apply(cal_total_by_axis0, axis=0) 
print(subject_score)
print(subject_score['總成績'])
#改計算每科的總分數
merge_score = df.apply(cal_total_by_axis0, axis=0).reset_index() #如果沒有reset_index, 原本欄位的名稱會變row的index
print(merge_score)
print(merge_score.iloc[:, 1:2]) #[row_start:row_end, col_start:col_end]



# lstrip rstrip
mystring = '//_//MFG//AB/C/DEFG/TEST///'
# lstrip會將左邊連續的/刪除
reportPath = "/" + mystring.lstrip("/")  #故此段語法結束後 最前面只會有一個/

print(reportPath)

# rstrip會將右邊連續的/刪除
reportPath = reportPath.rstrip("/") + "/" #故此段語法結束後 最後面只會有一個/

print(reportPath)



# os.path.join
import os
path1 = r"D:\abcd\efg" #r會忽略跳脫字元\, 當作字串處理
path2 = r"hijk\lmn"
path3 = r"\vv\bb\n" #最前面為\定會被當作是絕對路徑, 如果要當作子路徑與其他路徑串接須將最前面的\去除
if path3.startswith(os.sep): #os.sep是當下作業系統的分隔符號, windows:\  ;  unix:/
    path3 = path3.lstrip(os.sep)
filename = 'testfile.xlsx'
result_path = os.path.join(path1,path2,path3,filename)
print(result_path)