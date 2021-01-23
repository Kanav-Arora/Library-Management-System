import pymongo 
uri = "mongodb+srv://m001-student:m001-mongodb-basics@sandbox.ynusx.mongodb.net/admin?retryWrites=true&w=majority"
myclient = pymongo.MongoClient(uri)
database = myclient["endsem"]

def register_insert(username, password):
    collection = database["login"]
    dict1 = {"username" : username, "password": password}
    x = collection.insert_one(dict1)

# def login_data(username,password):
#     x = database.login.count({"username":{"$eq":username},"password":{"$eq":password}})
#     if x==1:
#         return True
#     else:
#         return False
    
   