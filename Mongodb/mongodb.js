//呼叫並操作 MongoDB;
const { MongoClient } = require('mongodb'); 
//建立一個叫做 myFirstDatabase 的資料庫的連結點
const uri = "mongodb+srv://root:root123@mycluster.xgf87.mongodb.net/myFirstDatabase?retryWrites=true&w=majority";
// 建立 MongoClient 物件並給予連結及驗證
const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });


// client.connect(err => {
//   const collection = client.db("test").collection("devices");
//   // perform actions on the collection object
//   // console.log("Database Created!");
//   let obj1 = {"name":"john", "age":3};
//   collection.insertOne(obj1);
//   client.close();
// });

async function run() {
  try {
    await client.connect();
    const database = client.db("insertDB");
    const foods = database.collection("foods");
    // create documents to insert
    // const docs = [
    //   { name: "cake", healthy: false },
    //   { name: "lettuce", healthy: true },
    //   { name: "donu"}
    // ]

    // const options = { ordered: true };
    // const result = await foods.insertMany(docs, options);

    // const options = {
    //   // sort matched documents in descending order by rating
    //   sort: { "name": 1 },
    //   // Include only the `title` and `imdb` fields in the returned document
    //   projection: { _id: 1, name: 1 },
    // };
    // const query = {"name":"cake"};
    // const food = await foods.findOne(query,options);

    // const query = {"name":"cake"};
    // const options = {
    //   // sort returned documents in ascending order by _id (A->Z)
    //   sort: { _id: -1},
    //   // Include only the `title` and `name` fields in each returned document
    //   projection: { _id:1, name:1}
    // }
    // const cursor = foods.find(query, options);
    // // print a message if no documents were found
    // if ((await cursor.count()) === 0) {
    //   console.log("No documents found!");
    // }
    // await cursor.forEach(console.log);

    // // create a filter for a movie to update
    // const filter = { name: "cake" };
    // // this option instructs the method to create a document if no documents match the filter
    // const options = { upsert: true };
    // // create a document that sets the plot of the movie
    // const updateDoc = {
    //   $set: {
    //     healthy : true,
    //   },
    // };
    // const result = await foods.updateMany(filter, updateDoc, options);
    // console.log(
    //   `${result.matchedCount} document(s) matched the filter, updated ${result.modifiedCount} document(s)`,
    // );

    // create a query for a movie to update
    const query = { name : "cake" };
    // create a new document that will be used to replace the existing document
    const replacement = {
      name : "caky",
    };
    const result = await foods.replaceOne(query, replacement);
    console.log(`Modified ${result.modifiedCount} document(s)`);

  } finally {
    await client.close();
  }
}
run().catch(console.dir);



