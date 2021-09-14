# npm install mongodb 下載 mongodb 的套件
# 即便連上資料庫、建立了集合，只要還沒放資料，資料庫便不會被建置
# node 檔案名稱 => 執行檔案

# 連上 Mongodb 並以 MongoClient 的函數進行操作
# var MongoClient = require('mongodb').MongoClient;
# 建立資料庫
# MongoClient.connect(url,function(err,db){})
# 建立 mydb 的資料庫物件
# var dbo = db.db("mydb")
# 建立集合
# dbo.createCollection("customers", function(err, res) {})
# 上面步驟快速完成
# const collection = client.db("test").collection("devices");

# insertOne() 方法
# const result = await haiku.insertOne(doc);
# console.log(`A document was inserted with the _id: ${result.insertedId}`);
# insertMany() 方法
# // this option prevents additional documents from being inserted if one fails
# const options = { ordered: true };
# const result = await foods.insertMany(docs, options);
# console.log(`${result.insertedCount} documents were inserted`);

# findOne() 方法
# const options = {
#     // sort matched documents in descending order by rating
#     sort: { "imdb.rating": -1 },
#     // Include only the `title` and `imdb` fields in the returned document
#     projection: { _id: 0, title: 1, imdb: 1 },
# };
# const movie = await movies.findOne(query, options);


