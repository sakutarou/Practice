//呼叫並操作 MongoDB;
const { MongoClient } = require('mongodb'); 
//建立一個叫做 myFirstDatabase 的資料庫的連結點
const uri = "mongodb+srv://root:root123@mycluster.xgf87.mongodb.net/myFirstDatabase?retryWrites=true&w=majority";
// 建立 MongoClient 物件並給予連結及驗證
const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });

// // Replace the following with values for your environment.
// const username = encodeURIComponent("root");
// const password = encodeURIComponent("root123");
// const clusterUrl = "mycluster.xgf87.mongodb.net/myFirstDatabase";
// const authMechanism = "DEFAULT"; //e.g. "SCRAM-SHA-256","SCRAM-SHA-1", and can be omitted in "MONGODB-CR"
// or GSSAPI mechanism with Kerberos, or PLAIN mechanism with LDAP (Lightweight Directory Access Protocol)
// // Replace the following with your MongoDB deployment's connection string.
// const uri =
//   `mongodb+srv://${username}:${password}@${clusterUrl}/?authMechanism=${authMechanism}`;
// // Create a new MongoClient
// const client = new MongoClient(uri);


// client.connect(err => {
//   const collection = client.db("test").collection("devices");
//   // perform actions on the collection object
//   // console.log("Database Created!");
//   let obj1 = {"name":"john", "age":3};
//   collection.insertOne(obj1);
//   client.close();
// });

// const simulateAsyncPause = () =>
//   new Promise( resolve =>{
//     setTimeOut(()=>resolve(),1000);
//   });
// let changeStream;

async function run() {
  try {
    await client.connect();
    const database = client.db("insertDB");
    const foods = database.collection("foods");

    // await simulateAsyncPause();
    // await collection.insertOne({
    //   title: "Record of a Shriveled Datum",
    //   content: "No bytes, no problem. Just insert a document, in MongoDB",
    // });
    // await simulateAsyncPause();
    // await changeStream.close();
    
    // console.log("closed the change stream");

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

    // create a filter for a food to update
    // const filter = { name: "cake" };
    // // this option instructs the method to create a document if no documents match the filter
    // const options = { upsert: true };
    // const updateDoc = {
    //   $set: { healthy : true },
    // };
    // const result = await foods.updateMany(filter, updateDoc, options);
    // console.log(`${result.matchedCount} document(s) matched the filter, updated ${result.modifiedCount} document(s)`,);

    // replace some attributes in documents
    // const query = { name : "cake" };
    // const replacement = { name : "caky" };
    // const result = await foods.replaceOne(query, replacement);
    // console.log(`Modified ${result.modifiedCount} document(s)`);

    // delete one document
    // const query = { name : "cake" }
    // const result = await foods.deleteOne(query);
    // if (result.deletedCount === 1 ){
    //   console.log("Scuuessfully deleted one record!");
    // }else{
    //   console.log("No documents have been deleted!");
    // }

    // delete many documents
    // Query for all foods with a name containing the string "ca"
    // const query = { name: { $regex: "ca" } };
    // const result = await foods.deleteMany(query);
    // console.log("Deleted " + result.deletedCount + " documents");

    // count documents
    // const query = { name : "lettuce" }
    // const estimate = await foods.estimatedDocumentCount();
    // const countLettuce = await foods.countDocuments(query);
    // console.log('estimated the number of documents in foods collection:' + countLettuce);
  
    // Retrieve the distinct values of a field
    // const query = { name : "lettuce"}
    // const fieldName = "healthy";
    // const distinctValues = await foods.distinct(fieldName,query);
    // console.log(distinctValues);

    // do something for all raw databases
    // const db = client.db("sample");
    // const result = await db.command({
    //   dbStats:0
    // });
    // console.log(foods);

    // Bulk write
    const result = await foods.bulkWrite([
      {insertOne:{
        document:{
          location:{
            address:{
              street: "3. Street",
              city: "Beiking",
              state: "China",
              zipcode: "99581"
            }
          }
        }
      }},
      {insertOne:{
        document:{
          location:{
            address:{
              street: "4. Street",
              city: "Washtong",
              state: "America",
              zipcode: "99517"
            }
          }
        }
      }},
      {updateMany:{
        filter:{"location.address.zipcode":"99517"},
        update:{$set:{"is_here":true}},
        upsert:true
      }},
      {deleteOne:{
        filter:{"location.address.street":"3. Street"}
      }}
    ])
    console.log(result);  
  } finally {
    await client.close();
  }
}
run().catch(console.dir);



