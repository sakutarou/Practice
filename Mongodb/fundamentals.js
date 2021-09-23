const { MongoClient, ServerApiVersion } = require("mongodb");
const uri = "mongodb+srv://root:root123@mycluster.xgf87.mongodb.net/myFirstDatabase?retryWrites=true&w=majority";
//const client = new MongoClient(uri,{ serverApi: ServerApiVersion.v1 })

const client = new MongoClient(uri,{
    serverApi:{
        
    }
})