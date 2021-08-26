# -*- coding: utf-8 -*-
import pandas as pd

# datas = pd.Series([12,20,30,66,1])
# print(datas);print(datas.max());print(datas.median());print(datas.mean());
# datas = datas*2;print(datas);data = datas==40;print(data) 
# datas = pd.Series([12,20,30,66,1],index=[0,1,3,5,"a"])
# print("資料型態",datas.dtype,"資料數量",datas.size,"資料索引",datas.index)
# print(datas[3],datas["a"])
# print("總和",datas.sum(),"乘總和",datas.prod(),"最大值",datas.max(),"最小值",datas.min())
# print("標準差",datas.std(),"算術平均",datas.mean(),"中位數",datas.median())
# print("最大三個數\n",datas.nlargest(3),"\n最小二個數\n",datas.nsmallest(2))
# print("隨意取兩個",datas.sample(2))

# datas = pd.Series(["你好","Python","Pandas"])
# print(datas.str.lower(),datas.str.upper(),datas.str.len())
# print(datas.str.cat(sep=","))
# print(datas.str.contains("P"))
# print(datas.replace("你好","hello"))
# condition = [True,False,True,True,False]
# condition = datas > 15
# filterdatas = datas[condition]
# print(condition)
# print(filterdatas)





dataf = pd.DataFrame({
    "name":["John","Lily",'Leo'],
    "Age":[12,14,92]
},index = ["a","b","c"])
# dataf["salary"] = [30000,31000,50000]
# dataf["happy"] = pd.Series([300,310,620],index = ["a","b","c"])
# print(dataf["name"]);print(dataf.iloc[1]);print(dataf.loc["c"])
# print("資料數量",dataf.size,"資料型態（列,欄）",dataf.shape,"資料索引",dataf.index)
# names = dataf["name"];print(names.str.upper())
# print(dataf)
condition = dataf["Age"] < 15
print(dataf[condition]["name"])



# googleplay 專案
# data = pd.read_csv("googleplaystore.csv")
# condition = data["Rating"] <= 5
# data =data[condition]
# print(data["Rating"].nlargest())


# data["Installs"] = pd.to_numeric(data["Installs"].str.replace("[],+]","").replace("Free",""))
# print(data["Installs"].mean())

# keyword = input("請輸入搜尋名稱關鍵字：")
# condition = data["App"].str.contains(keyword,case=False)
# condition = data["App"] == keyword
# print(data[condition]["Category"])
