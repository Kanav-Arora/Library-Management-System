from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import backend

"--------------------------------------------------------Login Window---------------------------------------------------------------------------"

def login_window(round):

    myFrame.config(text= "Login")

    for child in myFrame.winfo_children():
        child.destroy()

    # User ID Label
    ID = Label(myFrame, text = "Username:", relief = RAISED, fg = "white", bg = "#3b404e", bd=0 , font = ("Calibri",12), padx= 20, pady = 20)
    ID.grid(row = 0, column = 0, padx= 15, pady = 20)

    # User Password Label
    Password = Label(myFrame, text = "Password:", relief = RAISED, fg = "white", bg = "#3b404e", bd=0 , font = ("Calibri",12))
    Password.grid(row = 1, column = 0, padx= 50, pady = 5)

    # User ID field
    idEnter = Entry(myFrame, highlightbackground= "#3b404e", bg = "#3b404e", borderwidth = 2, fg ="white")
    idEnter.grid(row = 0, column = 1, padx= 50, pady = 5)

    # User Password field
    passEnter = Entry(myFrame, highlightbackground= "#3b404e", bg = "#3b404e", borderwidth = 2, fg = "white")
    passEnter.grid(row = 1, column = 1, padx= 50, pady = 5)

    def value(idEnter, passEnter):

        idval = idEnter.get()
        passval = passEnter.get()
        out = backend.login_data(idval,passval)
        if out==1:
            messagebox.showinfo("Success","Welcome")
            home_window(round)
        else:
            messagebox.showinfo("Failed","Invalid Credentials")


    # Login Button
    loginButton = Button(myFrame, image = round, borderwidth = 0, bg = "#3b404e",fg = "white",command= lambda: value(idEnter,passEnter))
    loginButton.grid(row = 2, column = 0, columnspan = 2, padx= 50, pady = 30)
    loginButton.config(highlightthickness=0)

    # registration button
    register = Button(myFrame, text = "Create new account", fg = "white", bg = "#3b404e", relief = FLAT, command= lambda: register_window(round))
    register.grid(row = 3, column = 0, columnspan = 2, padx= 50)
    register.config(highlightthickness=0)

"----------------------------------------------------------------------------------------------------------------------------------------------------"


"--------------------------------------------------------Register Window---------------------------------------------------------------------------"


def register_window(round):

    myFrame.config(text= "Register")

    for child in myFrame.winfo_children():
        child.destroy()

    
        # User ID Label
    ID = Label(myFrame, text = "Username:", relief = RAISED, fg = "white", bg = "#3b404e", bd=0 , font = ("Calibri",12), padx= 20, pady = 20)
    ID.grid(row = 0, column = 0, padx= 15, pady = 20)

    # User Password Label
    Password = Label(myFrame, text = "Password:", relief = RAISED, fg = "white", bg = "#3b404e", bd=0 , font = ("Calibri",12))
    Password.grid(row = 1, column = 0, padx= 50, pady = 5)

    # User ID field
    idEnter = Entry(myFrame, highlightbackground= "#3b404e", bg = "#3b404e", borderwidth = 2, fg = "white")
    idEnter.grid(row = 0, column = 1, padx= 50, pady = 5)

    # User Password field
    passEnter = Entry(myFrame, highlightbackground= "#3b404e", bg = "#3b404e", borderwidth = 2, fg = "white")
    passEnter.grid(row = 1, column = 1, padx= 50, pady = 5)


    def validity(idEnter, passEnter):
        list1 = list(idEnter)
        uservalid = True
        for i in list1:
            if i==" ":
                uservalid = False
        
        if uservalid == False:
            return "Username should not contain spaces"
        
        else:
        
            low, up, special, digit = 0,0,0,0
            if len(passEnter)>=8:
                for i in passEnter:
                     
                    if (i.islower()): 
                        low+=1            
            
                    if (i.isupper()): 
                        up+=1            
            
                    if (i.isdigit()): 
                        digit+=1            
            
                if low>=1 and up>=1 and digit>=1 and low+up+digit+special==len(passEnter):
                    return 1
                else:
                    print(low,up,special,digit)
                    return "Password should be of minimum length 8 and contain an uppercase and lowercase character and should be alphanumeric."
            else:
                
                return "Password should be of minimum length 8"
            


    def value(idEnter, passEnter):
        
        idval = idEnter.get()
        passval = passEnter.get()
        check = validity(idval,passval)
        if check==1:
            out = backend.register_insert(idval, passval)
            if out==True:
                messagebox.showinfo("Failed","Username unavailable")
            elif out==False:
                messagebox.showinfo("Success","Registered Successfully")
                login_window(round)

        else:
            messagebox.showinfo("Failed",check)

    # account creation
    loginButton = Button(myFrame, image = round, borderwidth = 0, command= lambda: value(idEnter,passEnter))
    loginButton.grid(row = 2, column = 0, columnspan = 2, padx= 50, pady = 30)
    loginButton.config(highlightthickness=0)

    # login frame
    register = Button(myFrame, text = "Sign in", fg = "white", bg = "#3b404e", relief = FLAT, command= lambda: login_window(round))
    register.grid(row = 3, column = 0, columnspan = 2, padx= 50)
    register.config(highlightthickness=0)    

"----------------------------------------------------------------------------------------------------------------------------------------------------"


"--------------------------------------------------------Home Window---------------------------------------------------------------------------"

def home_window(round):
    myFrame.config(text= "Home Page")

    for child in myFrame.winfo_children():
        child.destroy()

    addBook = Button(myFrame,text = "Add Book", fg = "#FFFFFF", bg = "#3b404e", relief = GROOVE, borderwidth= 2, command =  lambda: add_window(round))
    addBook.config(highlightbackground = "#3b404e", highlightthickness = 2, highlightcolor= "#3b404e")
    addBook.grid(row = 0,padx = 160, pady = 8, sticky = "nesw")

    deleteBook = Button(myFrame,text = "Delete Book", fg = "#FFFFFF", bg = "#3b404e", relief = GROOVE, command = lambda:delete_window(round))
    deleteBook.config(highlightbackground = "#3b404e", highlightthickness = 2, highlightcolor= "#3b404e")
    deleteBook.grid(row = 1, padx = 160, pady = 8, sticky = "nesw")

    viewBook = Button(myFrame,text = "View Book", fg = "#FFFFFF", bg = "#3b404e", relief = GROOVE, command = lambda: view_window(round))
    viewBook.config(highlightbackground = "#3b404e", highlightthickness = 2, highlightcolor= "#3b404e")
    viewBook.grid(row = 2, padx = 160, pady = 8, sticky = "nesw")

    issueBook = Button(myFrame,text = "Issue Book", fg = "#FFFFFF", bg = "#3b404e", relief = GROOVE, command=lambda: issue_window(round))
    issueBook.config(highlightbackground = "#3b404e", highlightthickness = 2, highlightcolor= "#3b404e")
    issueBook.grid(row = 3, padx = 160, pady = 8, sticky = "nesw")

    returnBook = Button(myFrame,text = "Return Book", fg = "#FFFFFF", bg = "#3b404e", relief = GROOVE,command = lambda: return_window(round))
    returnBook.config(highlightbackground = "#3b404e", highlightthickness = 2, highlightcolor= "#3b404e")
    returnBook.grid(row = 4, padx = 160, pady = 8, sticky = "nesw")

    defaulterBook = Button(myFrame,text = "Book Defaulters", fg = "#FFFFFF", bg = "#3b404e", relief = GROOVE)
    defaulterBook.config(highlightbackground = "#3b404e", highlightthickness = 2, highlightcolor= "#3b404e", command = lambda: modes(round))
    defaulterBook.grid(row = 5, padx = 160, pady = 8, sticky = "nesw")

"----------------------------------------------------------------------------------------------------------------------------------------------------"


"--------------------------------------------------------Add Book Window---------------------------------------------------------------------------"
def add_window(round):

    myFrame.config(text= "Add Book")

    for child in myFrame.winfo_children():
        child.destroy()

    def add(round):
        sr = book_id_Enter.get()
        name = book_name_Enter.get()
        author = author_name_Enter.get()
        date = date_name_Enter.get()
        price = price_name_Enter.get()
        category = category_name_Enter.get()
        for child in myFrame.winfo_children():
            child.destroy()
        
        label_1 = Label(myFrame)

        val = backend.add_book(sr, name, author, date, price, category)
        if val==True:
            
            label_1.config(text ="\n\nSerial no. : "+sr+"\nBook Name : "+name+"\nis successfully added to the database.", relief = RAISED, fg = "white", bg = "#3b404e", bd=0 , font = ("Calibri",12), width=35, anchor="center")
            
        elif val==False:
            error = Label(myFrame, text = "Unsuccessful!!", fg = "white",relief = RAISED, bg = "#3b404e", bd=0 , font = ("Calibri",12), width=35, anchor="center", )
            error.config(highlightbackground="red", highlightthickness=1)
            label_1.config(text ="\n\nSerial no. : "+sr+"\nBook Name : "+name+"\nalready exists in the database.", relief = RAISED, fg = "white", bg = "#3b404e", bd=0 , font = ("Calibri",12), width=35, anchor="center")
            error.grid(row=0, column = 0, padx=60, pady=5)
        label_1.grid(row = 1, column = 0, padx=60, pady=5)

            # Login Button
        loginButton = Button(myFrame, image = round, borderwidth = 0, command = lambda: home_window(round))
        loginButton.grid(row = 6, column = 0, columnspan = 2, padx= 30, pady = 15)
        loginButton.config(highlightthickness=0)


    # Name of book Label
    book_name = Label(myFrame, text = "Book Name:", relief = RAISED, fg = "white", bg = "#3b404e", bd=0 , font = ("Calibri",12), padx= 15)
    book_name.grid(row = 0, column = 0, padx= 15, pady = 5)

    # Name Of Author Label
    author_name = Label(myFrame, text = "Name of Author:", relief = RAISED, fg = "white", bg = "#3b404e", bd=0 , font = ("Calibri",12), padx= 15)
    author_name.grid(row = 2, column = 0,padx= 15, pady = 5)

    # Date Label
    date_name = Label(myFrame, text = "Date \n (YYYY-MM-DD):", relief = RAISED, fg = "white", bg = "#3b404e", bd=0 , font = ("Calibri",12), padx= 15)
    date_name.grid(row = 5, column = 0,padx= 15, pady = 5)

    # Price Label
    price_name = Label(myFrame, text = "Price:", relief = RAISED, fg = "white", bg = "#3b404e", bd=0 , font = ("Calibri",12), padx= 15)
    price_name.grid(row = 4, column = 0, padx= 15, pady = 5)

    # BOOK ID Label
    book_id = Label(myFrame, text = "Book ID:", relief = RAISED, fg = "white", bg = "#3b404e", bd=0 , font = ("Calibri",12))
    book_id.grid(row = 1, column = 0, padx= 15, pady = 5)

    # Category Label
    category_name = Label(myFrame, text = "Category:", relief = RAISED, fg = "white", bg = "#3b404e", bd=0 , font = ("Calibri",12))
    category_name.grid(row = 3, column = 0,padx= 15, pady = 5)

    # Name Of Book field
    book_name_Enter = Entry(myFrame, highlightbackground= "#3b404e", bg = "#3b404e", borderwidth = 2, fg ="white",border=3)
    book_name_Enter.grid(row = 0, column = 1, padx= 70, pady = 5)

    # Name Of Author field
    author_name_Enter = Entry(myFrame, highlightbackground= "#3b404e", bg = "#3b404e", borderwidth = 2, fg ="white",border=3)
    author_name_Enter.grid(row = 2, column = 1,padx= 70, pady = 5)

    # BOOK ID field
    book_id_Enter = Entry(myFrame, highlightbackground= "#3b404e", bg = "#3b404e", borderwidth = 2, fg = "white",border=3)
    book_id_Enter.grid(row = 1, column = 1, padx= 70, pady = 5)

    # Price field
    price_name_Enter = Entry(myFrame, highlightbackground= "#3b404e", bg = "#3b404e", borderwidth = 2, fg = "white",border=3)
    price_name_Enter.grid(row = 4, column = 1,padx= 70, pady = 5)

    # Category field
    category_name_Enter = Entry(myFrame, highlightbackground= "#3b404e", bg = "#3b404e", borderwidth = 2, fg = "white",border=3)
    category_name_Enter.grid(row = 3, column = 1, padx= 70, pady = 5)

    # Date field
    date_name_Enter = Entry(myFrame, highlightbackground= "#3b404e", bg = "#3b404e", borderwidth = 2, fg = "white",border=3)
    date_name_Enter.grid(row = 5, column = 1,padx= 70, pady = 5)

    # Login Button
    loginButton = Button(myFrame, image = round, borderwidth = 0, command = lambda: add(round))
    loginButton.grid(row = 6, column = 0, columnspan = 2, padx= 30, pady = 15)
    loginButton.config(highlightthickness=0)



"----------------------------------------------------------------------------------------------------------------------------------------------------"


"--------------------------------------------------------Delete Book Window---------------------------------------------------------------------------"

def delete_window(round):
    myFrame.config(text= "Delete Book")

    for child in myFrame.winfo_children():
        child.destroy()
    
    def delete(round):
        sno.grid_forget()
        entry_box_sno.grid_forget()
        name_book.grid_forget()
        entry_box_book.grid_forget()
        next_button.grid_forget()
        
        val = backend.delete_book(entry_box_sno.get(),entry_box_book.get())

        label_1 = Label(myFrame)

        if val==1:
            
            label_1.config(text ="\n\nSerial no. : "+entry_box_sno.get()+"\nBook Name : "+entry_box_book.get()+"\nis successfully deleted from the record.", relief = RAISED, fg = "white", bg = "#3b404e", bd=0 , font = ("Calibri",12), width=35, anchor="center")
            
        else:
            error = Label(myFrame, text = "Unsuccessful!!", fg = "white",relief = RAISED, bg = "#3b404e", bd=0 , font = ("Calibri",12), width=35, anchor="center", )
            error.config(highlightbackground="red", highlightthickness=1)
            label_1.config(text ="\n\nSerial no. : "+entry_box_sno.get()+"\nBook Name : "+entry_box_book.get()+"\ndoes not exists.", relief = RAISED, fg = "white", bg = "#3b404e", bd=0 , font = ("Calibri",12), width=35, anchor="center")
            error.grid(row=0, column = 0, padx=60, pady=5)
        label_1.grid(row = 1, column = 0, padx=60, pady=5)
        
        #next button for going to the next step
        next_button_1=Button(myFrame, image=rounded_button, borderwidth=0, command = lambda: home_window(round))
        next_button_1.grid(row = 2, column = 0, pady=30)
        next_button_1.config(highlightthickness=0)

    #label asking for serial number of book
    sno= Label(myFrame, text = "Serial No. :", relief = RAISED, fg = "white", bg = "#3b404e", bd=0 , font = ("Calibri",12), padx= 20, pady = 20)
    sno.grid(row = 0, column = 0, padx= 20, pady = 15)

    #entry box to type the serial number of book
    entry_box_sno=Entry(myFrame, highlightbackground= "#3b404e", bg = "#3b404e", borderwidth = 2, fg = "white")
    entry_box_sno.grid(row = 0, column = 1, padx= 50, pady = 5)

    #label asking for name of book
    name_book= Label(myFrame, text = "Name of Book :", relief = RAISED, fg = "white", bg = "#3b404e", bd=0 , font = ("Calibri",12), padx= 20, pady = 20)
    name_book.grid(row = 1, column = 0, padx= 20, pady = 15)

    #entry box to type the name of book
    entry_box_book=Entry(myFrame, highlightbackground= "#3b404e", bg = "#3b404e", borderwidth = 2, fg = "white")
    entry_box_book.grid(row = 1, column = 1, padx= 50, pady = 5)


    #next button for going to the next step
    next_button=Button(myFrame, image=round, borderwidth=0, command=lambda: delete(round))
    next_button.grid(row = 2, column = 0, columnspan = 2, pady=30)
    next_button.config(highlightthickness=0)


"----------------------------------------------------------------------------------------------------------------------------------------------------"


"--------------------------------------------------------View Book Window---------------------------------------------------------------------------"
def view_window(round):
    
    myFrame.config(text= "View Book")
    for child in myFrame.winfo_children():
            child.destroy()

    #title
    title = Label(myFrame, text="%-15s%-29s%-20s%-10s" % ('S.No','Title', 'Author','Status'),relief  = RAISED, bg="#3b404e", fg='white', width=45, anchor="center",bd = 0 , font = ("Calibri",12))
    title.grid(row = 0, column = 0, columnspan = 2, padx = 10, pady = 8)
    
    
    # break line
    line = Label(myFrame, text = "----------------------------------------------------------------------------", relief = RAISED, fg = "white", bg = "#3b404e", bd = 0 , font = ("Calibri",12), width = 49, anchor = 'center')
    line.grid (row = 1, column = 0, columnspan = 2, padx = 5, pady = 5)

    my_list = backend.view_book()

    #try:
    y = 3
    for i in my_list:

        # data label
        data = Label(myFrame, text="%-15s%-35s%-30s" % (i[0], i[1], i[2])+" "+i[3], bg="#3b404e", fg='white', width=50, anchor='w')
        data.grid(row = y, column = 0, columnspan = 2, pady = 1)
        y += 1

    back_button = Button(myFrame, image = round, borderwidth = 0, anchor="center", command= lambda: home_window(round))
    back_button.grid(row = y+1, padx=5, pady = 8, columnspan = 2)
    back_button.config(highlightthickness=0)

"----------------------------------------------------------------------------------------------------------------------------------------------------"


"--------------------------------------------------------Issue Book Window---------------------------------------------------------------------------"
def issue_window(round):
    myFrame.config(text= "Issue Book")
    for child in myFrame.winfo_children():
            child.destroy()

    def issuewindow2(round):
        serial = entry_sno.get()
        name = entry_name.get()
        date = entry_date.get()
        for child in myFrame.winfo_children():
            child.destroy()
        result,book = backend.issue_book(serial,name,date)
            
        if result==True:
            label_1= Label(myFrame, text ="\n\nSerial no. : "+serial+"\nBook Name : "+book+"\nhas been issued to "+name+"\non "+date, relief = RAISED, fg = "white", bg = "#3b404e", bd=0 , font = ("Calibri",12), width=35, anchor="center")
            label_1.grid(row = 0, column = 0, padx=60, pady=5)
        else:
            label_1= Label(myFrame, text ="\n\nBook is currently unavailable.", relief = RAISED, fg = "white", bg = "#3b404e", bd=0 , font = ("Calibri",12), width=35, anchor="center")
            label_1.grid(row = 0, column = 0, padx=60, pady=5)

        #next button for going to the next step
        next_button_1=Button(myFrame, image = round,borderwidth=2,bg = "#3b404e", fg = "white",relief= GROOVE,command= lambda: home_window(round))
        next_button_1.grid(row = 1, column = 0, pady=30)
                

    #label asking for serial number of book
    sno= Label(myFrame, text = "Serial No. :", relief = RAISED, fg = "white", bg = "#3b404e", bd=0 , font = ("Calibri",12), padx=20, pady = 5)
    sno.grid(row = 0, column = 0, padx= 20, pady = 15)

    #entry box to type the serial number of book
    entry_sno=Entry(myFrame, highlightbackground= "#3b404e", bg = "#3b404e", borderwidth = 2, fg = "white")
    entry_sno.grid(row = 0, column = 1, padx= 50, pady = 5)

    #label asking for name of book
    name_student= Label(myFrame, text = "Name of Student :", relief = RAISED, fg = "white", bg = "#3b404e", bd=0 , font = ("Calibri",12), padx=20, pady = 5)
    name_student.grid(row = 1, column = 0, padx= 20, pady = 15)

    #entry box to type the name of book
    entry_name=Entry(myFrame, highlightbackground= "#3b404e", bg = "#3b404e", borderwidth = 2, fg = "white")
    entry_name.grid(row = 1, column = 1, padx= 50, pady = 5)

    # label for date
    issue_date= Label(myFrame, text = "Issue Date :\n(YYYY-MM-DD)", relief = RAISED, fg = "white", bg = "#3b404e", bd=0 , font = ("Calibri",12), padx=20, pady = 5)
    issue_date.grid(row = 2, column = 0, padx= 20, pady = 15)

    #entry box to type the name of book
    entry_date=Entry(myFrame, highlightbackground= "#3b404e", bg = "#3b404e", borderwidth = 2, fg = "white")
    entry_date.grid(row = 2, column = 1, padx= 50, pady = 5)

    #next button for going to the next step
    next_button=Button(myFrame, image=round, borderwidth=0, bg = "#3b404e", command = lambda: issuewindow2(round))
    next_button.grid(row = 3, column = 0, columnspan = 2, pady = 5)
    next_button.config(highlightthickness=0)


"----------------------------------------------------------------------------------------------------------------------------------------------------"


"--------------------------------------------------------Return Book Window---------------------------------------------------------------------------"
def return_window(round):

    myFrame.config(text= "Return Book")

    for child in myFrame.winfo_children():
            child.destroy()

    def return_window2(round):
        serial = book_id_Enter.get()
        name = student_name_Enter.get()
        for child in myFrame.winfo_children():
            child.destroy()

        value, number = backend.return_book(serial)
        message = Label(myFrame,relief = RAISED, fg = "white", bg = "#3b404e", bd=0 , font = ("Calibri",12), width=35, anchor="center")
        if value==True:
            message.config(text = "The book with serial number: "+number+"\nhas been returned by "+name+".") 
        elif type(value)!=bool:
            message.config(text = "The book of serial number: "+number+"\nis a late return.\nKindly pay fine of Rs. "+ str(value))
        elif value==False:
            message.config(text = "The book of serial number: "+number+"\nis not in the database.")
        message.grid(row = 0, column = 0, padx=60, pady=5)

        #next button for going to the next step
        next_button_1=Button(myFrame, image = round,borderwidth=2,bg = "#3b404e", fg = "white", relief= GROOVE,command= lambda: home_window(round))
        next_button_1.grid(row = 1, column = 0, pady=30)
        


    # Name Of Student Label
    student_name = Label(myFrame, text = "Name of student:", relief = RAISED, fg = "white", bg = "#3b404e", bd=0 , font = ("Calibri",12), padx= 20, pady = 15)
    student_name.grid(row = 0, column = 0, padx= 15, pady = 20)

    # BOOK ID Label
    book_id = Label(myFrame, text = "Book ID:", relief = RAISED, fg = "white", bg = "#3b404e", bd=0 , font = ("Calibri",12), padx= 20, pady = 15)
    book_id.grid(row = 1, column = 0, padx= 15, pady = 20)

    # Name Of Student field
    student_name_Enter = Entry(myFrame, highlightbackground= "#3b404e", bg = "#3b404e", borderwidth = 2, fg ="white",border=3)
    student_name_Enter.grid(row = 0, column = 1, padx= 50, pady = 5)

    # BOOK ID field
    book_id_Enter = Entry(myFrame, highlightbackground= "#3b404e", bg = "#3b404e", borderwidth = 2, fg = "white",border=3)
    book_id_Enter.grid(row = 1, column = 1, padx= 50, pady = 5)
   
    #next button for going to the next step
    next_button=Button(myFrame, image=round, borderwidth=0, bg = "#3b404e", command= lambda: return_window2(round))
    next_button.grid(row = 2, column = 0, columnspan = 2, pady = 15)
    next_button.config(highlightthickness=0)

"----------------------------------------------------------------------------------------------------------------------------------------------------"


"--------------------------------------------------------Defaulter Window---------------------------------------------------------------------------"

def modes(round):
    myFrame.config(text= "Defaulter")
    for child in myFrame.winfo_children():
        child.destroy()
    r = IntVar()          #integer variable 

    #label asking for the fault
    mode = Label(myFrame, text = "Mode:", relief = RAISED, fg = "white", bg = "#3b404e", bd=0 , font = ("Calibri",12))
    mode.place(relx = 0.2, rely = 0.35)

    #radio button 1 for late submission
    radio_button_1 = Radiobutton(myFrame, text = "defaulter's list", font = ("Calibri",12), width = 16, fg = "white", bg = "#3b404e",selectcolor = "#3b404e", activebackground = "#3b404e", anchor = "w", variable = r, value = 1, command = lambda: table(round, radio_button_1,radio_button_2))
    radio_button_1.place(relx = 0.5, rely = 0.3)

    #radio button 2 for book lost
    radio_button_2 = Radiobutton(myFrame, text = "book lost", font = ("Calibri",12), width = 16, fg = "white", bg = "#3b404e", selectcolor = "#3b404e", activebackground = "#3b404e", anchor = "w", variable = r ,value = 2, command = lambda: booklost(round, radio_button_1,radio_button_2))
    radio_button_2.place(relx = 0.5, rely = 0.45)


def table(round, radio_button_1, radio_button_2):
        
        radio_button_2.deselect
        
        for child in myFrame.winfo_children():
                child.destroy()

        #titles of defaulter's list
        Title = Label(myFrame, text = "%-10s%-25s%-15s%-10s"%('Sr. No.','Name of Student','Due Date','Fine'), relief = RAISED, fg = "white", bg = "#3b404e", bd = 0 , font = ("Calibri",12))
        Title.grid(row = 3, column = 0, columnspan = 2, padx = 15, pady = 8)

        line = Label(myFrame, text = "----------------------------------------------------------------------------", relief = RAISED, fg = "white", bg = "#3b404e", bd = 0 , font = ("Calibri",12), width = 49, anchor = 'w')
        line.grid (row = 4, column = 0, columnspan = 2, pady = 5)

        res = backend.defaulter_list()
        y = 5
        try:
            for i in res:
               
                
                def_list = Label(myFrame, text= "%-10s%-25s%-15s%-10s"%(i[0],i[1],i[2],i[3]) , relief = RAISED, fg = "white", bg ="#3b404e", bd = 0 , font = ("Calibri",12))
                def_list.grid(row = y, column = 0, columnspan = 2, pady=1)
                y += 1
                
        except:
            messagebox.showinfo("Failed","Unable to fetch files from database")

        #next button for going to the next step
        #this will take you to main menu
        next_button_3 = Button(myFrame, image = round, borderwidth = 0, command= lambda: home_window(round))
        next_button_3.grid(row = y+1, column = 0, columnspan = 2, pady=8)
        next_button_3.config(highlightthickness = 0)


def booklost(round, radio_button_1, radio_button_2):
        radio_button_1.deselect

        for child in myFrame.winfo_children():
                child.destroy()

        #label asking for name of defaulter
        name = Label(myFrame, text = "Name of Defaulter:", relief = RAISED, fg = "white", bg = "#3b404e", bd = 0 , font = ("Calibri",12), padx= 40, pady = 10)
        name.grid(row = 4, column = 0)

        #entry box to type the name of defaulter
        entry_box_name = Entry(myFrame, highlightbackground = "#3b404e", bg = "#3b404e", borderwidth = 2, fg = "white")
        entry_box_name.grid(row = 4, column = 1)

        #label asking for name of book
        serial = Label(myFrame, text = "Serial number:", relief = RAISED, fg = "white", bg = "#3b404e", bd = 0 , font = ("Calibri",12), padx= 40, pady = 10)
        serial.grid(row = 3, column = 0)

        #entry box to type the name of book
        entry_serial = Entry(myFrame, highlightbackground = "#3b404e", bg = "#3b404e", borderwidth = 2, fg = "white")
        entry_serial.grid(row = 3, column = 1)

        r_2 = IntVar()       #integer variable

        def disable_2(round):
            
            
            if r_2.get()==3:
                radio_button_4.deselect
                name = entry_box_name.get()
                sr = entry_serial.get()
                price = backend.price(sr)

                #label to display original price        
                label_1 = Label(myFrame, text = name + " is fined for Rs."+str(price)+"\n", relief = RAISED, fg = "white", bg = "#3b404e", bd = 0 , font = ("Calibri",12), width=46, anchor = 'center')
                label_1.grid(row = 7, column = 0, columnspan = 2, padx = 20, pady = 2)

                next_button_1 = Button(myFrame, image = round, borderwidth = 0, command = lambda: home_window(round))
                next_button_1.grid(row = 8, column = 0, columnspan = 2, pady = 8)
                next_button_1.config(highlightthickness = 0)

            else:
                radio_button_3.deselect
                def book_lost():
                    name = entry_box_name.get()
                    sr = entry_serial.get()
                    val = backend.delete_book(sr)
                    add_window(round)


                #label to display message        
                label_2 = Label(myFrame, text = "To add new book details and delete current book details\n click on next", relief = RAISED, fg = "white", bg = "#3b404e", bd = 0 , font = ("Calibri",12))
                label_2.grid(row = 7, column = 0, columnspan = 2, padx = 5, pady = 2)

                next_button_1 = Button(myFrame, image = round, borderwidth = 0, command = book_lost)
                next_button_1.grid(row = 8, column = 0, columnspan = 2, pady = 8)
                next_button_1.config(highlightthickness = 0)




        #label asking for choice
        option = Label(myFrame, text = "Options:", relief = RAISED, fg = "white", bg = "#3b404e", bd=0 , font = ("Calibri",12), width = 5, anchor = 'center')
        option.grid(row = 5, column = 0,padx = 40, pady= 5, sticky='news')

        #radio button 3 for pay price
        radio_button_3 = Radiobutton(myFrame, text = "pay original price", font = ("Calibri",12), width = 22, fg = "white", bg = "#3b404e",selectcolor = "#3b404e", activebackground = "#3b404e", variable = r_2, value = 3, command = lambda:  disable_2(round))
        radio_button_3.grid(row = 5, column = 1, pady = 5)

        #radio button 4 for add new book
        radio_button_4 = Radiobutton(myFrame, text = "add new book", font = ("Calibri",12), width = 20, fg = "white", bg = "#3b404e", selectcolor = "#3b404e", activebackground = "#3b404e", anchor = "center", variable = r_2, value = 4, command = lambda: disable_2(round))
        radio_button_4.grid(row = 6, column = 1, pady = 5)
    
"----------------------------------------------------------------------------------------------------------------------------------------------------"


root = Tk()
root.title("Book Worm")
root.geometry("600x500")
root.resizable(0,0)

window_height = 500
window_width = 600

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

bg = ImageTk.PhotoImage(Image.open("images/0_mMD5SlIbFvgkGo3l.jpeg"))
myLabel = Label(root,image = bg)
myLabel.place(x=0,y=0,relwidth=1,relheight=1)

myFrame = LabelFrame(root,bg="#3b404e", text = "Account Login",bd=3, fg = "white", padx=5, pady=5, labelanchor = "n")
myFrame.place(relx = 0.5, rely = 0.5, relwidth = 0.7, relheight = 0.6, anchor = CENTER)

button_image=Image.open("images/Rounded Button.png")
button_image=button_image.resize((110,40),Image.ANTIALIAS)
rounded_button=ImageTk.PhotoImage(button_image)

login_window(rounded_button)
# add_window(rounded_button)



root.mainloop()