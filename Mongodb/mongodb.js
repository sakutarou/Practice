const { MongoClient } = require('mongodb'); //呼叫並操作 MongoDB;
const uri = "mongodb+srv://root:root@mycluster.xgf87.mongodb.net/myFirstDatabase?retryWrites=true&w=majority";//建立一個叫做 myFirstDatabase 的資料庫
const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });
client.connect(err => {
  const collection = client.db("test").collection("devices");
  // perform actions on the collection object
  client.close();
});