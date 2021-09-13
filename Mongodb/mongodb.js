var MongoClient = require("mongodb").MongoClient; //呼叫並操作 MongoDB
var url = "mongodb+srv://root:root@mycluster.xgf87.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"; //建立一個叫做 mydb 的資料庫

console.log("hello");
MongoClient.connect(url,function(err,db){
    if(err) throw err;
    console.log("DataBase created!");
    db.close();
});