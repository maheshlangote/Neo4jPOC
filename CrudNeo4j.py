
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
        return node

    def updateNode(self):
        query = "MERGE (n:Employee {name: 'Mehak'})SET n.age = 100, n.coat = 'Yellow' RETURN n"
        node = self.session.run(query)
        self.session.commit()
        return node

    def deleteNode(self):
        query= "MATCH (n) DETACH DELETE "
        nodes = self.session.run(query)
        return nodes

    def deleteSingleRelationalNode(self, id):
        query = "MATCH (n) WHERE id(n)={id} DETACH DELETE (n)".format(id=id)
        node = self.session.run(query)
        return node

obj = Crud()
obj.getAllNode()
obj.createNode(name="Mehak", age=27, department= "networking")
obj.updateNode()
obj.getAllNode()
frm = obj.getSignleNode(0)
relation = "KNOWS"
to = obj.getSignleNode(4)
obj.createRelationship(frm, relation, to)
obj.deleteSingleRelationalNode(3)



