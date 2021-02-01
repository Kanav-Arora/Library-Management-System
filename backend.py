import pymongo 
import datetime
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
def add_book(sr, name, author, date, price, category, status = "yes"):
    collection = database["book_list"]
    dict1 = {"serial number": sr, "name": name, "author": author, "date": date, "price":price, "category": category, "available":status}
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
def issue_book(sr, student, date):
    collection = database["book_list"]
    x = collection.find({"$expr":{"$eq":["$serial number",sr]}},{"available":1,"_id":0})
    value = True
    for i in x:
        # dictionary which will either be {'available':'yes'} or {'available':'no'}
        if i=={"available":"yes"}:
            value = True
        else:
            value= False
    if value==True:
        x = collection.update_one({"serial number":sr},{"$set":{"available":"no"}}) 
        collection = database["issued_book"]
        due = datetime.datetime.strptime(date, '%Y-%m-%d')+ datetime.timedelta(days=7)
        duedate = datetime.datetime.strptime(str(due), "%Y-%m-%d %H:%M:%S")
        dict1 = {"serial number":sr, "student name":student, "issue date": date, "due date": str(duedate.date()) }
        x = collection.insert_one(dict1)

# test
# issue_book("B1","kanav","2020-01-31")
"---------------------------------------------------------------------------------------------"


"---------------------------------Return Book-------------------------------------------------"
def return_book(sr):
    collection = database["issued_book"]
    x = collection.delete_one({"serial number":sr})
    collection = database["book_list"]
    x = collection.update_one({"serial number":sr},{"$set":{"available":"yes"}}) 

# test
# return_book("B1")
"---------------------------------------------------------------------------------------------"


"----------------------------------Defaulter--------------------------------------------------"

"---------------------------------------------------------------------------------------------"
