# Connections
# Local MongoDB Instance on Default Port
mongosh
mongosh "mongodb://localhost:27017" # default port
mongosh --port 28015 # use the port 28015
mongosh "mongodb://mongodb0.example.com:28015" # MongoDB Instance on a Remote Host¶
mongosh --host mongodb0.example.com --port 28015
# To connect to a remote MongoDB instance and authenticate against the admin database as user alice:
mongosh "mongodb://mongodb0.example.com:28015" --username alice --password alice --authenticationDatabase admin
# Using the +srv connection string modifier automatically sets the tls option to true for the connection. 
mongosh "mongodb+srv://server.example.com/"
mongosh "mongodb://mongodb0.example.com:28015/?tls=true"
mongosh "mongodb://mongodb0.example.com:28015" --tls
# The following connection string URI connects to database db1.
mongosh "mongodb://localhost:27017/db1"
# To disconnect from a deployment and exit mongosh, you can:
Type .exit, exit, or exit().
Type quit or quit().
Press Ctrl + D.
Press Ctrl + C twice.


# Usage
# use myNewDB
# db.myNewCollection1.insertOne( { x: 1 } )

# Views
# Create view by createCollection()
db.createCollection(
  "<viewName>",
  {
    "viewOn" : "<source>",
    "pipeline" : [<pipeline>],
    "collation" : { <collation> }
  }
)
# Create view by createView() 
db.createView(
  "<viewName>",
  "<source>",
  [<pipeline>],
  {
    "collation" : { <collation> }
  }
)
# Views are read-only
The following read operations can support views:
db.collection.find()
db.collection.findOne()
db.collection.aggregate()
db.collection.countDocuments()
db.collection.estimatedDocumentCount()
db.collection.count()
db.collection.distinct()








