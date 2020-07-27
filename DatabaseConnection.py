from py2neo import Database, Graph, Node, Relationship
from constant import *

# Database("bolt://camelot.example.com:7687") # Using Database class connect to data neo4j
class Database:

    def getConnection():
        db = Graph(host=HOST,scheme=SCHEME,port=PORT, secure=SECURE,auth=(USER, PASSWORD))  # Using Graph class connect to data neo4j
        session = db.begin()
        return session

# a = Node("Employee", name="Ramesh") # Node label and properties
# # tx.create(a)    # create a single node using session object
#
# b = Node("Employee", name="Suresh") # Node label and properties
# tx.create(a, b)    # create node using session object
#
# tx.commit()

# b = Node("Person", name="Bob")
# ab = Relationship(a, "KNOWS", b)
# tx.create(ab)

# db.exists(ab)

# bgin = db.begin()
# node = Node("Emp", name="Mahesh")
# bgin.create(node)
# bgin.commit()
# print(db.exists(node))
# query = "MATCH (n) return (n)"  # Query for Get all Node from databse
# nodes = db.run(query) # Execute query
# for node in nodes: # iterate all node
#     print(node) # display node


