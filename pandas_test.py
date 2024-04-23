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




