# 載入 ptmongo 套件
import pymongo
import ssl
from bson.objectid import ObjectId

# 連線到雲端資料庫
client = pymongo.MongoClient("mongodb+srv://root:root123@mycluster.xgf87.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",ssl_cert_reqs = ssl.CERT_NONE)
# 把資料放進資料庫中
db = client.website # 選擇操作 website 的資料庫
collection = db.members # 選擇操作 members 集合

# 把一筆資料新增到集合中
# result = collection.insert_one({
#     "name":"john",
#     "email":"test@test.com",
#     "password":"test",
#     "level":1
# })

# 把多筆資料新增到集合中
# result = collection.insert_many([{
#     "name":"lary",
#     "email":"a@a.com",
#     "password":"a",
#     "level":2
# },{
#     "name":"mary",
#     "email":"b@b.com",
#     "password":"b",
#     "level":3
# }])

# 取得集合中的第一筆文件資料
# data = collection.find_one()
# # 取得集合中的某特定文件資料
# data = collection.find_one(ObjectId("6125cd276c1453fee8f20337"))

# print(data["_id"]) # 印出該內容中的id
# print(data["email"])

# 一次取得多筆文件的資料
# cursor = collection.find() # 這是一個讀寫頭
# print(cursor)
# for doc in cursor:
#     print(doc["name"])

# 更新集合中的一筆資料
# result = collection.update_one({
#     "email":"test@test.com"
# },{
#     "$set":{
#         "password":"123"
#     }
# })

# result = collection.update_many({
#     "name":"john"
# },{
#     "$set":{
#         "password":"kaka",
#         "level":2
#     }
# })

# result = collection.update_many({
#     "name":"john"
# },{
#     "$unset":{
#         "level":2
#     }
# })

# result = collection.update_many({
#     "name":"john"
# },{
#     "$inc":{  # mul
#         "level":2
#     }
# })

# 刪除集合中的資料
# result = collection.delete_one({
#     "name":"mary"
# })
# result = collection.delete_many({
#     "name":"mary"
# })

# 未成功、分類
result = collection.sort({"name":"mary"})

# print("符合條件的文件數量",result.matched_count)
# print("實際更新的文件數量",result.modified_count)


# 印出該文件的 id
# print(result.inserted_ids)
# print("資料新增成功")