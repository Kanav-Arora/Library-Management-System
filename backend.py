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
# add_book("B1","Harry Puttar", "J.K Rowling", "2021-01-15",700, "Fiction")
# add_book("B2","catcher in the rye", "n.a", "2021-01-15",700, "Fiction")
"---------------------------------------------------------------------------------------------"


"---------------------------------Delete Book-------------------------------------------------"
def delete_book(sr, name):
    collection = database["book_list"]
    x = collection.count_documents({"serial number":sr})
    y = collection.delete_one({"serial number":sr})
    collection = database["defaulters"]
    y = collection.delete_one({"serial number":sr})
    collection = database["issued_book"]
    y = collection.delete_one({"serial number":sr})
    if x==1:
        return True
    else:
        return False
    
    
    
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
    x = collection.count_documents({"$expr":{"$eq":["$serial number",sr]}})
    value = True
    if x==1:
        x = collection.find({"$expr":{"$eq":["$serial number",sr]}},{"available":1,"_id":0})
        
        for i in x:
            # dictionary which will either be {'available':'yes'} or {'available':'no'}
            if i=={"available":"yes"}:
                value = True
            else:
                value= False
    else:
        value= False
    if value==True:
        x = collection.update_one({"serial number":sr},{"$set":{"available":"no"}})
        y = collection.find({"$expr":{"$eq":["$serial number",sr]}})
        bookname = ""
        for i in y:
            bookname = i["name"]
        collection = database["issued_book"]
        due = datetime.datetime.strptime(date, '%Y-%m-%d')+ datetime.timedelta(days=7)
        duedate = datetime.datetime.strptime(str(due), "%Y-%m-%d %H:%M:%S")
        dict1 = {"serial number":sr, "student name":student, "issue date": date, "due date": str(duedate.date()) }
        x = collection.insert_one(dict1)
        return True,bookname
    else:
        return False, ""

# test
# issue_book("B1","kanav","2021-01-20")
# issue_book("B2","arnav","2021-02-02")
"---------------------------------------------------------------------------------------------"


"---------------------------------Return Book-------------------------------------------------"
def return_book(sr):
    collection = database["issued_book"]
    y = collection.count_documents({"$expr":{"$eq":["$serial number",sr]}})
    if y==1:
        x = collection.delete_one({"serial number":sr})
        collection = database["book_list"]
        x = collection.update_one({"serial number":sr},{"$set":{"available":"yes"}}) 
        return True, sr
    else:
        return False, " "

# test
# return_book("B1")
"---------------------------------------------------------------------------------------------"


"----------------------------------Defaulter--------------------------------------------------"
def defaulter():
    collection1 = database["defaulters"]
    collection2 = database["issued_book"]
    collection3 = database["book_list"]
    today = datetime.datetime.now()
    print(today)
    x = collection2.find({})
    # dictionaries of issued books (i)
    for i in x:
        due = i["due date"]
        duedate = datetime.datetime.strptime(due, "%Y-%m-%d")
        if duedate<today:
            y = collection1.find({})
            # dictionaries of defaulters (j)
            flag = True
            for j in y:
                if j["serial number"]==i["serial number"]:
                    flag = False
            if flag==True:
                k = collection3.find({})
                bookname = ""
                for m in k:
                    if m["serial number"]==i["serial number"]:
                        bookname = m["name"]
                date1  = datetime.datetime.strptime(i["due date"], '%Y-%m-%d')
                delta = today - date1
                fine = delta.days * 5
                dict1 = {"serial number":i["serial number"], "book name":bookname , "defaulter name": i["student name"], "due date": i["due date"], "number of days": delta.days, "fine" : fine }
                z = collection1.insert_one(dict1)
# defaulter()
"---------------------------------------------------------------------------------------------"
