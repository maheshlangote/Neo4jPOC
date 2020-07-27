
from DatabaseConnection import Database
from py2neo import Node, Record, Relationship


class Crud:
    session = Database.getConnection()
    def createNode(self, *args, **kwargs):
        node = Node("Employee", **kwargs) # Node label and properties
        self.session.create(node)    # create a single node using session object
        self.session.commit()
        return node

    def createRelationship(self, frm, to, relation):
        obj = Relationship(frm, relation, to)
        obj = self.session.create(Relationship(obj))
        return obj

    def getAllNode(self):
        query = "MATCH (n) return (n)"  # Query for Get all Node from databse
        nodes = self.session.run(query)
        print("count the record -->>",self.session.evaluate("MATCH (n) RETURN COUNT(n)"))
        for node in nodes:
            print(node)
        return nodes

    def getSignleNode(self, id):
        query = "MATCH (n) where id(n)={id} return (n)".format(id=id) # Query for Get single Node from database
        node = self.session.run(query)
        print(node.data())
        return node

    def updateNode(self):
        pass

    def deleteNode(self):
        query= "MATCH (n) DETACH DELETE "
        self.session.run(query)
        return True

    def deleteSingleRelationalNode(self, id):
        query = "MATCH (n) DETACH DELETE where id(n)={id}".format(id=id)
        node = self.session.run(query)
        return True

obj = Crud()

obj.getAllNode()
obj.createNode(name="Ajay", age=27, department= "networking")
frm = obj.getSignleNode(0)
relation = "KNOWS"
to = obj.getSignleNode(4)
obj.createRelationship(frm, relation, to)
obj.deleteSingleRelationalNode(3)

