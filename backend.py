import pymongo 
uri = "mongodb+srv://m001-student:m001-mongodb-basics@sandbox.ynusx.mongodb.net/admin?retryWrites=true&w=majority"
myclient = pymongo.MongoClient(uri)
database = myclient["endsem"]

"----------------------------Register and login----------------------------------------------"
def register_insert(username, password):
    collection = database["login"]
    dict1 = {"username" : username, "password": password}
    x = collection.insert_one(dict1)

def login_data(username,password):
    x = database.login.count_documents({"$expr":{"$and":[{"$eq":["$username",str(username)]},{"$eq":["$password",str(password)]}]}})
    return x
"---------------------------------------------------------------------------------------------"


"----------------------------------Add Book---------------------------------------------------"
def add_book(sr, name, author, date, price, category):
    collection = database["book_list"]
    dict1 = {"serial number": sr, "name": name, "author": author, "date": date, "price":price, "category": category}
    x = collection.insert_one(dict1)

# test
# add_book("B1","Harry Puttar", "J.K Rowling", "2020-01-30",700, "Fiction")
"---------------------------------------------------------------------------------------------"


"---------------------------------Delete Book-------------------------------------------------"
def delete_book(sr, name):
    collection = database["book_list"]
    x = collection.delete_one({"serial number":sr})

# test
# delete_book("B1", "Harry Puttar")
"---------------------------------------------------------------------------------------------"


"----------------------------------View Book-------------------------------------------------"
def view_book():
    collection = database["book_list"]
    x = collection.find({})
    return x
# test
# view_book()
"---------------------------------------------------------------------------------------------"


"---------------------------------Issue Book-------------------------------------------------"

"---------------------------------------------------------------------------------------------"


"---------------------------------Return Book-------------------------------------------------"

"---------------------------------------------------------------------------------------------"


"----------------------------------Defaulter-------------------------------------------------"

"---------------------------------------------------------------------------------------------"
