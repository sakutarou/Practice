# -*- coding: utf-8 -*- 
# 電腦中的檔案系統
# 各自管理，檔案格式不統一
# 資料庫系統 Data Base Management System
# 中心化、標準化、程式化的資料管理系統

# 關聯式資料庫：強調資料間的關聯性
# MySQL、MSSQL、PostgreSQL、OracleSQL
# 非關聯式資料庫：強調資料分散、水平擴展的能力
# MongoDB、BigTable、Cassandra

# MongoDB 
# JSON 格式友善、簡潔的文件模型、容易水平擴展
# 在網路上先進入 MongoDB 的網站，建立好 DataBase 與連結入口
# pip install pymongo[srv] 
# 記得有些電腦要處理 ssl 的問題

# 資料庫結構
# Mongo DB 的結構：資料庫 DataBase、集合Collection、文件Documents

# 新增 JSON 格式的資料
# result = 集合.insert_one(文件資料)
# result.inserted_id 取得新增資料的編號
# 新增多筆資料
# result = collection.insert_many([{data1},{data2},{data3}])
# result.inserted_ids

# 取得文件資料
# 集合.find_one() # 取得集合中的第一筆資料
# 根據編號 ObjectId 物件取得文件資料，必須從 bson.objectId 封包載入
# 集合.find_one(文件編號)
# e.g.
# from bson.objectid import ObjectId
# collection = db.website
# data = collection.find_one(
#     ObjectId("....")
# )
# print(data["name"]) 顯示該資料中的 name 欄位內容
# print(data["_id"])
# 取得所有文件資料
# 集合.find()
# collection = db.website
# cursor = collection.find()
# print(cursor) # Cursor 物件
# 使用 for 迴圈逐一取得文件
# for doc in cursor:
#   print(doc)
