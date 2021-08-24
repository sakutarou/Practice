# 載入 ptmongo 套件
import pymongo
# 連線到雲端資料庫
client = pymongo.MongoClient("mongodb+srv://root:root@mycluster.xgf87.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
# 把資料放進資料庫中
db = client.test # 選擇操作 test 的資料庫
collection = db.users # 選擇操作 users 集合
# 把資料新增到集合中
collection.insert_one({
    "name":"john",
    "gender":"男"
})
print("資料新增成功")

