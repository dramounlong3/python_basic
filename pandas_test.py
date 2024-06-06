import pandas as pd
# import sys
# sys.stdout.reconfigure(encoding='utf-8')
s = pd.Series([1,3,5,7,9])
print(s)

print()
data = {
    'apples': [3,2,0,1],
    'oranges': [0,3,7,2]
}
df = pd.DataFrame(data)
print(df)

print()
# 由字典列表建立
data2 = [
    {'姓名': '小明', '年紀': 24, '工作': '工程師'},
    {'姓名': '小華', '年紀': 30, '工作': '設計師'},
    {'姓名': '小天', '年紀': 28, '工作': '老師'}
]
df2 = pd.DataFrame(data2)
print(df2)

print()
# 由列的字典建立
data3 = {
    '姓名':['小明','小華','小天'],
    '年紀':[24,30,28],
    '工作':['工程師','設計師','老師']
}
df3 = pd.DataFrame(data3)
print(df3) #與df2結果相同

print()
# 由行的字典建立
rows = [
    ['小明',24,'工程師'],
    ['小華',30,'設計師'],
    ['小天',28,'老師']
]

col_names = ['姓名','年紀','工作']
df4 = pd.DataFrame(rows,columns=col_names)
print(df4) #與df2, df3結果相同

print()
# 從Series建立
s1 = pd.Series(['小明','小華','小天'])
s2 = pd.Series([24,30,28])
s3 = pd.Series(['工程師','設計師','老師'])
df5 = pd.DataFrame({'姓名':s1, '年紀':s2, '工作': s3})
print(df5) #與df2, df3, df4結果相同

print()
#查看df型態
print(df4.dtypes)
print(df5.dtypes)

print()
# DataFrame常見屬性
data6 = {
    'Integers': [1,2,3],
    'Floats': [0.1,0.2,0.3],
    'Strings': ['apple','banana', 'cherry']
}
df6= pd.DataFrame(data6)
print("Data types:\n", df6.dtypes)
print("Shape:", df6.shape) #行數、列數 (3,3)
print("Index:", df6.index)
print("Columns:", df6.columns) #column name
print("Info:", df6.info()) #顯示每個column不是空值數量...等
print("Describe:\n", df6.describe()) #顯示統計資訊 count, mean...等
print("Head:", df6.head())
print("Size:", df6.size) #總數量 rows * columns
print("Is empty:", df6.empty)

print()
# 取得指令column內的資料
column_data = df5['工作']
print(column_data)
print(df5.工作) #只要欄位名稱是有效的變數名則可透過.來取得column數值
#透過row & col index取得資料  ===> iloc
#單一元素
element = df5.iloc[1,2] #row index 1, col index 2
print("Single element:", element)
#單一row
row = df5.iloc[2] # row index 2
print("Row index 2:\n{0}".format(row))
#數個row
multiRow = df5.iloc[0:2] # 0 ~ 2 (不包含2)
print("multiRow:\n{0}".format(multiRow))
#數個col
multiCol = df5.iloc[:, 1:3] #col index 1 ~ 3 (不包含3)
print("multiCol:\n{0}".format(multiCol))
#數個row + col (取子集合)
multiRowCol = df5.iloc[1:3, 0:2]
print("multiRowCol:\n{0}".format(multiRowCol))

print()
#透過row, col name取得資料 ===> loc
#單一元素
ele = df5.loc[0, '姓名'] # 0不是 row index, 而是row的name (預設為數字)
print("ele:", ele)
#取得指定row
rowLoc = df5.loc[1]
print("rowLoc:\n{0}".format(rowLoc))
#取得數個row
multiRowLoc = df5.loc[0:1] #跟iloc的差異在於, loc會包含1
print("multiRowLoc:\n{0}".format(multiRowLoc))
#取得數個col
multiColLoc = df5.loc[:,'年紀':'工作'] #會包含工作的col
print("multiColLoc:\n{0}".format(multiColLoc))
#取得特定row & col (取交集)
multiRowColLoc = df5.loc[1:2, '姓名':'工作'] #會包含2 和 工作
print("multiRowColLoc:\n{0}".format(multiRowColLoc))
"""
切片差異：iloc 在進行切片時不包含結束位置，而 loc 包含結束位置。
非數字索引：當使用非數字索引時（例如字符串標籤），loc 特別有用。
條件選擇：loc 可以與布林條件配合使用，選擇符合特定條件的行列。
效率：在訪問單個值或者小區域時，直接使用 iloc 或 loc 通常更高效。但對於較大的區域或者整個行列的操作，使用條件選擇或直接列名可能更好。
"""

data7 = {'apples': [3, 2], 'oranges': [4, 6]}
df7 = pd.DataFrame(data7)
print("data7:\n{0}".format(df7))
#增加col
df7['bananas'] = [5, 3]
print("data7:\n{0}".format(df7))
#增加row
new_row = {'apples': 7, 'oranges': 8, 'bananas': 2}
df7 = df7.append(new_row, ignore_index=True)
print("data7:\n{0}".format(df7))

#去除重複數據
data8 = {'apples': [3, 2, 3, 8], 'oranges': [4, 6, 4, 6]}
df8 = pd.DataFrame(data8)
print(df8)
df8 = df8.drop_duplicates() #row 2被刪掉
print(df8)

print()
import numpy as np
#刪除有缺失值的row
data9 = {'apples': [3, np.nan, 3, 8], 'oranges': [4, 6, 4, 6], 'bananas':[1, 7, np.nan, 5]}
df9 = pd.DataFrame(data9)
print(df9)
df9 = df9.dropna()
print(df9)

print()
#刪除有缺失值的col
data10 = {'apples': [3, np.nan, 3, 8], 'oranges': [4, 6, 4, 6], 'bananas':[1, 7, np.nan, 5]}
df10 = pd.DataFrame(data10)
print(df10)
df10 = df10.dropna(axis='columns')
print(df10)

print()
#刪除全部都是nan的row
data11 = {'apples': [3, 1, np.nan, 8], 'oranges': [4, 6, np.nan, 6], 'bananas':[1, 7, np.nan, 5]}
df11 = pd.DataFrame(data11)
print(df11)
df11 = df11.dropna(how='all') #any表示有nan就刪
print(df11)

print()
#刪除有值的數量少於2的row
data12 = {'apples': [3, 1, 9, 8], 'oranges': [4, 6, np.nan, np.nan], 'bananas':[1, 7, np.nan, 5]}
df12 = pd.DataFrame(data12)
print(df12)
df12 = df12.dropna(thresh=2)
print(df12)

print()
#將nan以指定值補上
df13 = pd.DataFrame({
    'A': [1, np.nan, 3],
    'B': [4, 5, np.nan],
    'C': [np.nan, np.nan, np.nan]
})
print(df13)
#使用固定值補齊
df_filled = df13.fillna(0)
print(df_filled)
#使用各col的平均值補齊
df_filled = df13.fillna(df13.mean())
print(df_filled)
#使用nan的下一個值往上補齊
df_filled = df13.fillna(method='ffill')
print(df_filled)

print()
#計算出col的平均值
df14 = pd.DataFrame({'apples': [3, 1, 9, 8], 'oranges': [4, 6, 9, 10]})
print(df14.mean())

print()
# 轉換型別
df15 = pd.DataFrame({
    'A':['1','2','3'],
    'B':['1.1','2.2','3.3'],
    'C':['2021-01-01','2021-01-02','2021-01-03'],
    'D': ['apple', 'banana', 'cherry']
})
print(df15.dtypes)
df15['A'] = df15['A'].astype(int)
df15['B'] = df15['B'].astype(float)
df15['C'] = pd.to_datetime(df15['C'])
df15['D'] = df15['D'].astype('category')
print(df15.dtypes)

print()
# 修正數據
df16 = pd.DataFrame({
    'Age': [29,-1,0,25,120],
    'Salary': ['10000$', '9000$', '8000$', '7000$', '6000$'],
    'Name': ['Alice', 'Bob','', 'Charlie', 'David']
})

#修正年齡
df16.loc[df16['Age'] < 0, 'Age'] = df16['Age'].median()
df16.loc[df16['Age'] > 100, 'Age'] = df16['Age'].median()
#修正薪水
df16['Salary'] = df16['Salary'].str.replace('$', '', regex=False).astype(int)
#修正空名字
df16['Name'] = df16['Name'].replace('', 'Unknow')
print(df16)

print()
#資料合併
df17 = pd.DataFrame(
    {
        'A': ['A0', 'A1', 'A2'],
        'B': ['B0', 'B1', 'B2']
    },
    index = ['K0', 'K1', 'K2']
)
df18 = pd.DataFrame(
    {
        'C': ['C0', 'C2', 'C3'],
        'D': ['D0', 'D2', 'D3']
    },
    index = ['K0', 'K2', 'K3']
)
#concat, 基於row的索引合併, K0 接 K0, 以新增col的方式合併, 若其中一邊沒有則以NaN補齊
result1 = pd.concat([df17, df18], axis=1)
#merge, 類似inner join, 兩個df都有的index才會以新增col的方式合併
result2 = pd.merge(df17, df18, left_index=True, right_index=True, how='inner') #若改為how='outer', 則兩邊都會保留, 空值以NaN補齊, 變成與result1的結果相同
#join, 類似left join, 若想要以df18為主, 則以df18.join起頭, 右半部沒有的值則以NaN補齊
result3 = df17.join(df18)
print("result1:")
print(result1)
print("result2:")
print(result2)
print("result3:")
print(result3)

print()
#檔案處理
#讀取csv
df19 = pd.read_csv("class_info.csv", sep=',', encoding='big5')
print("csv:")
print(df19)
#讀取xlsx
df20 = pd.read_excel('class_info.xlsx', sheet_name=0)
print("excel")
print(df20)

print()
#group by
col20 = ['class', 'name', 'hbd']
data20 = [
    ['class0', 'user0', '1993-10-01'],
    ['class0', 'user1', '1992-10-02'],
    ['class1', 'user2', '1990-10-01'],
    ['class2', 'user3', '1983-10-03'],
    ['class1', 'user4', '1991-10-02'],
    ['class0', 'user5', '2001-10-03']
]
df20 = pd.DataFrame(data20, columns=col20)
print("original data20")
print(df20)
df20_groupByClass = df20.groupby('class')
print("df20 after group by class")
print(df20_groupByClass.groups)
print("df20 get group class1")
print(df20_groupByClass.get_group('class1'))

print()
#聚合
df21 = pd.DataFrame({
    'Group': ['A', 'B', 'A', 'B', 'A', 'B'],
    'Value': [1, 2, 3, 4, 5, 6],
    'Grade': [99,100,10,20,30,50]
})
grouped = df21.groupby('Group').agg({'Value': lambda x: list(x)})
print(grouped)
grouped = df21.groupby('Group').agg(list)
print(grouped) #與上方結果相同, 都是以Group為分組將Value以list的形式放在一起
sumGroup = df21.groupby('Group').agg({'Value': [lambda x: list(x), 'sum']})
print(sumGroup)
sumGroupByAnotherWay = df21.groupby('Group')['Grade'].agg([list,sum]) #groupby後, 可以再用['col name']選擇欄位拿來做aggregate運算
print(sumGroupByAnotherWay) #與上方結果相同, 都可以將分組後的list計算衝加總數字

print()
#any()
my_string = "coding**is**so**cool**123"
are_there_digits = [x.isdigit() for x in my_string] #迭代所有字串內的字元, 並且判斷是否為數字
print("原始測試完的結果")
print(are_there_digits)
print("使用any判斷是否list內有任何一個true")
print(any(are_there_digits))

print()
#all()
my_alphabet = "this is my first time to check"
are_there_alphabet = [y.isalpha() for y in my_alphabet] #判斷是否為字母
print(all(are_there_alphabet))
my_new_alphabet = my_alphabet.replace(" ","")
print("new: ", my_new_alphabet)
are_there_new_alphabet = [y.isalpha() for y in my_new_alphabet] #判斷是否為字母
print("將空白取代為空字串後")
print(all(are_there_new_alphabet))

print()
# 將資料by UserAccount groupby後, 將其他欄位整合成list格式, 並且將結果做迭代, 然後找出ReportOwner有含v的UserAccount
data22 = {
    'UserAccount': ['user1', 'user2', 'user3', 'user1'],
    'ReportRLS': ['RLS1', 'RLS2', 'RLS3', 'RLS4'],
    'ReportOwner': ['', 'owner2', 'v', 'dejief']
}
df22 = pd.DataFrame(data22)
grouped = df22.groupby('UserAccount').agg({'ReportRLS': list, 'ReportOwner': list}).reset_index()
print(grouped)
print()
last_element = None
for index, element in grouped.iterrows():
    if 'v' in element['ReportOwner']:
        print("UserAccount:", element['UserAccount'])
    else:
        print("v not found")

print()
#連接db
import pymssql
sql_query = "select top 10 * from common.PBI_UserPermission with(nolock)"
try:
    #使用windows認證登入
    with pymssql.connect(host = 'TWTPESQLDV2', database = 'BI_ETL') as conn:
    #使用帳密登入
    # with pymssql.connect(server = 'TWTPESQLDV2', database = 'BI_ETL', user = 'xxx', password = 'xxxxxx') as conn:
        with conn.cursor() as cursor:
            cursor.execute(sql_query)
            # conn.commit() #使用insert才需要commit

            #迭代撈取到的資料
            rows = cursor.fetchall()
            for row in rows:
                pass #print(row)

            print(cursor.description)
            print()
            columns_ori = [column[0] for column in cursor.description] #取得欄位名稱
            types = [column[1] for column in cursor.description]   #取得資料型態, 但目前看是數字 (可能1對應到NVARCHAR, 4對應到DATETIME)
            print(columns_ori)
            print(types)

            #將取得的資料放到DF中
            print()
            df23 = pd.DataFrame(rows)  #如果沒加上columns的設定, 則col_name 預設是以數字編排
            print(df23)
            df24 = pd.DataFrame(rows, columns=columns_ori)
            print()
            print(df24)

    print("Select successful")
except Exception as e:
    print(f"Error selecting data: {str(e)}")
    
    
    

# explode
# 可將名聲有多筆的人展開成多列
# 1.df_explode['名聲'].str.split(',') ==> 將名聲的這個column的內容以逗號做切割, 轉換為 list
# 2.df_explode.assign(名聲 = ...)     ==> 將名聲(若名稱不存在就會新增column), 的內容重新指定為步驟1 list的結果
# 3.dataFrame.explode('名聲')         ==> 將dataFrame以名聲欄位為主, 將list中的多個元素展開來為不同列, 其他欄位的值就與原本那一列的內容相同
import sys
sys.stdout.reconfigure(encoding='utf-8')

df_explode = pd.read_excel("class_info.xlsx")
print("原始:df_explode\n", df_explode)
df_assign = df_explode.assign(名聲 = df_explode['名聲'].str.split(','))
print("assign\n", df_assign)
df_explode = df_explode.assign(名聲 = df_explode['名聲'].str.split(',')).explode('名聲')
print("展開後: df_explode\n", df_explode)


import json

all_sheet = pd.read_excel("class_info.xlsx", sheet_name=['class1','class2'])
print("\nall_sheet\n", all_sheet)

#將各自的sheet補上sheet_name欄位, 並且給予原本的sheet name名稱
for name, sheet in all_sheet.items():
    sheet['sheet_name'] = name

sheet1 = all_sheet['class1']
sheet2 = all_sheet['class2']

print("\nsheet1\n", sheet1)
print("\nsheet2\n", sheet2)

merged_class = pd.concat([sheet1, sheet2], ignore_index=True)
print("\nmerged_class\n", merged_class)
list_str_calss = [merged_class.to_json()]
print("\nlist_str_calss\n", list_str_calss)

df_from_json = pd.read_json(list_str_calss[0])
print("\ndf_from_json\n", df_from_json)
df_class2 = df_from_json[df_from_json['sheet_name'] == 'class2'].reset_index(drop=True)
print("\ndf_class2\n", df_class2)
print("\ntype(df_class2)\n", type(df_class2))
df_class1 = df_from_json[df_from_json['sheet_name'] == 'class1'].reset_index(drop=True)
print("\ndf_class1\n", df_class1)
print("\ntype(df_class1)\n", type(df_class1))



# pd.read_json, pd.DataFrame, json_loads, json_dumps, json_load, json_dump, pd.json_normalize
# pd.read_json          將 json 字串 讀取後轉為 dataFrame
# json_loads            將 json 字串 讀取後轉為 python dict/list
# pd.DataFrame          將 python dict/list 或 json格式的檔案 讀取後轉為 dataFrame

# json_dumps            將 python dict/list 讀取後轉為 json 字串
# json_dump             將 python dict/list 讀取後轉為 json 字串檔案
# json_load             將 json 字串檔案     讀取後轉為 python dict/list
# pd.json_normalize     將 python dict/list 讀取後轉為 dataFrame (但內容表達的方式 與 pd.DataFrame轉過來的方式不太一樣)
# https://www.geeksforgeeks.org/how-to-read-json-files-with-pandas/ 參考內容



data = pd.read_csv("https://raw.githubusercontent.com/turingplanet/pandas-intro/main/public-datasets/country.csv")
print(data)