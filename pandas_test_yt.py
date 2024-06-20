import pandas as pd
import numpy as np

# 10個 0~24隨機整數的list
random_items = np.random.randint(25, size=(10))
print(random_items)

#建立series from list
series_data = pd.Series(random_items)
print(series_data)

#獲取第一個元素
print(series_data[0])

#自建index
letter_indexes = ['a','b','c','d','e','f','g','h','i','j']
new_series_data = pd.Series(random_items, index=letter_indexes)
print(new_series_data)
print(new_series_data['h'])

data_dict = {
    'a':1,
    'b':2,
    'c':3,
    'd':4,
    'e':5,
}

#建立series from dict
dict_series = pd.Series(data_dict)
print(dict_series)

#將series命名
dict_series = pd.Series(data_dict, name='series_name')
print(dict_series)

#將series更名
dict_series = dict_series.rename('new_name')
print(dict_series)

#使用boolean index取得大於中位數的元素
dict_series_bigger_than_median = dict_series[dict_series > dict_series.median()]
print(dict_series_bigger_than_median)


# 建立dataframe from dict, 每一個column即為一個series
d = {
    'one': [1, 2, 3, 4],
    'two': [4, 3, 2, 1]
}

dict_df = pd.DataFrame(d)
print(dict_df)

print('two:\n',dict_df['two'])

#column印出型態為series
print(type(dict_df['two']))

#印出df為x*x的二維資料 ==> row:4*col:2
print(dict_df.shape)


# 使用series建立df
d_data = {
    'one': pd.Series([1,2,3], name='col_one', index=['a','b','c']),
    'two': pd.Series([1,2,3,4], name='col_two', index=['a','b','c','d'])
}

df = pd.DataFrame(d_data)
print(df)

#重置index, 原本的index會變col
new_df = df.reset_index()
print(new_df)

#重置index, 並刪除原本的index
new_df = df.reset_index(drop=True)
print(new_df)

print(df)
#inplace強制改變原本的df ==> 本來都是回傳一個新的df
df.reset_index(drop= True, inplace=True)
print(df)

#國家資料
csv_data_path = 'https://raw.githubusercontent.com/turingplanet/pandas-intro/main/public-datasets/country_info.csv'
country_info = pd.read_csv(csv_data_path)
print(country_info)
#獲取row col number
print(country_info.shape)
#獲取column name ==> list
print(country_info.columns)
#查看前三行
print(country_info.head(3))
#獲取指定column (單欄)
print(country_info['Region'])
#獲取指定column (多欄) ==> 參數放list
print(country_info[['Country','Region']])
#獲取指定row (單列) ==> 第101列
print(country_info.iloc[100])
#獲取指定row, col (多列 2 and 4, 多欄 1 and 4) 
print(country_info.iloc[[2,4],[0,3]])

#改用country為index
#先將country的字串頭尾去空白
country_info['Country'] = country_info['Country'].str.strip()
new_country_info = country_info.set_index(['Country'], drop=True)
print(new_country_info.head())
#因為index變字串, 需以loc指定 ==> iloc以整數取得row, col ==> loc以標籤名稱取得row, col
print(new_country_info.loc['China']) 
print(new_country_info.loc[['China', 'Japan']])
#列標籤為China, Japan; 欄標籤為Region, Population
print(new_country_info.loc[['China', 'Japan'], ['Region','Population']]) #使用inner list

#範圍查詢, China ~ Japan中間的所有row 和 Region~Deathrate中間的所有col
print(new_country_info.loc['China':'Japan', 'Region':'Deathrate']) #無需使用inner list

#hk
hk_country_info = country_info[['Country', 'Birthrate', 'Service']].head(10)
print(hk_country_info)
hk_country_info.to_csv('country.csv', index=False)


# filtering
# row index name = 1~4 (不包含5)
print(country_info[1:5])

# row integer location = 1~4 (不包含5), 結果與上面相同 (經測試, 無論使用不連續index, 中文index, 結果都與上面相同)
print(country_info.iloc[1:5])


#4.數據排序與更新
csv_data_path = 'https://raw.githubusercontent.com/turingplanet/pandas-intro/main/public-datasets/small_survey_results.csv'
survey_df = pd.read_csv(csv_data_path)
print(survey_df)

#將Respondent設為index
rsp_df = survey_df.set_index('Respondent')
print(rsp_df)

#根據Respondent(index)排序, 預設是asc排序
rsp_sort_df = rsp_df.sort_index()
print(rsp_sort_df)

#根據特定的col排序
sort_df = survey_df.sort_values(by='Age', ascending=False)
print(sort_df)

#根據兩個欄位排序
sort_two_df = survey_df.sort_values(by=['Age','YearsCode'], ascending=[False, True])[['Age','YearsCode']]
print(sort_two_df)

#將某個series直接排序
age_df = survey_df['Age'].sort_values()
print(age_df)

#前10名的ConvertedComp
top10 = survey_df['ConvertedComp'].nlargest(10)
print(top10)

#後10名的ConvertedComp
last10 = survey_df['ConvertedComp'].nsmallest(10)
print(last10)

#獲取ConvertedComp前10名的row
richest_users = survey_df.nlargest(10, 'ConvertedComp')
print(richest_users[['ConvertedComp', 'DevType', 'EdLevel']])

#iteration 迭代
#迭代column
for col_name, col_data in survey_df.items():
    print(col_name)
    print(col_data) #該column的所有資料
    break #看1欄