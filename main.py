from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import backend

"--------------------------------------------------------Login Window---------------------------------------------------------------------------"

def login_window():

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

    # rounded button 
    # image =Image.open("D:/project test/images/Rounded Button.png", Image.ANTIALIAS)
    # rounded = ImageTk.PhotoImage(image)

    def value(idEnter, passEnter):
        # global idEnter
        # global passEnter
        idval = idEnter.get()
        passval = passEnter.get()
        out = backend.login_data(idval,passval)
        if out==1:
            messagebox.showinfo("Success","Welcome")
            home_window()
        else:
            messagebox.showinfo("Failed","Invalid Credentials")


    # Login Button
    loginButton = Button(myFrame, text = "Next", borderwidth = 0, command= lambda: value(idEnter,passEnter))
    loginButton.grid(row = 2, column = 0, columnspan = 2, padx= 50, pady = 30)
    loginButton.config(highlightthickness=0)

    # registration button
    register = Button(myFrame, text = "Create new account", fg = "white", bg = "#3b404e", relief = FLAT, command= register_window)
    register.grid(row = 3, column = 0, columnspan = 2, padx= 50)
    register.config(highlightthickness=0)

"----------------------------------------------------------------------------------------------------------------------------------------------------"


"--------------------------------------------------------Register Window---------------------------------------------------------------------------"


def register_window():

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

    # rounded button 
    # image =Image.open("images/Rounded Button.png")
    # image = image.resize((110, 40), Image.ANTIALIAS)
    # rounded = ImageTk.PhotoImage(image)

    def value(idEnter, passEnter):
        
        idval = idEnter.get()
        passval = passEnter.get()
        backend.register_insert(idval, passval)

    # account creation
    loginButton = Button(myFrame, text = "Next", borderwidth = 0, command= lambda: value(idEnter,passEnter))
    loginButton.grid(row = 2, column = 0, columnspan = 2, padx= 50, pady = 30)
    loginButton.config(highlightthickness=0)

    # login frame
    register = Button(myFrame, text = "Sign in", fg = "white", bg = "#3b404e", relief = FLAT, command= login_window)
    register.grid(row = 3, column = 0, columnspan = 2, padx= 50)
    register.config(highlightthickness=0)    

"----------------------------------------------------------------------------------------------------------------------------------------------------"


"--------------------------------------------------------Home Window---------------------------------------------------------------------------"

def home_window():

    for child in myFrame.winfo_children():
        child.destroy()

    addBook = Button(myFrame,text = "Add Book", fg = "#FFFFFF", bg = "#3b404e", relief = GROOVE, borderwidth= 2)
    addBook.config(highlightbackground = "#3b404e", highlightthickness = 2, highlightcolor= "#3b404e")
    addBook.grid(row = 0,padx = 160, pady = 8, sticky = "nesw")

    deleteBook = Button(myFrame,text = "Delete Book", fg = "#FFFFFF", bg = "#3b404e", relief = GROOVE, command = delete_window)
    deleteBook.config(highlightbackground = "#3b404e", highlightthickness = 2, highlightcolor= "#3b404e")
    deleteBook.grid(row = 1, padx = 160, pady = 8, sticky = "nesw")

    viewBook = Button(myFrame,text = "View Book", fg = "#FFFFFF", bg = "#3b404e", relief = GROOVE)
    viewBook.config(highlightbackground = "#3b404e", highlightthickness = 2, highlightcolor= "#3b404e")
    viewBook.grid(row = 2, padx = 160, pady = 8, sticky = "nesw")

    issueBook = Button(myFrame,text = "Issue Book", fg = "#FFFFFF", bg = "#3b404e", relief = GROOVE)
    issueBook.config(highlightbackground = "#3b404e", highlightthickness = 2, highlightcolor= "#3b404e")
    issueBook.grid(row = 3, padx = 160, pady = 8, sticky = "nesw")

    returnBook = Button(myFrame,text = "Return Book", fg = "#FFFFFF", bg = "#3b404e", relief = GROOVE)
    returnBook.config(highlightbackground = "#3b404e", highlightthickness = 2, highlightcolor= "#3b404e")
    returnBook.grid(row = 4, padx = 160, pady = 8, sticky = "nesw")

    defaulterBook = Button(myFrame,text = "Book Defaulters", fg = "#FFFFFF", bg = "#3b404e", relief = GROOVE)
    defaulterBook.config(highlightbackground = "#3b404e", highlightthickness = 2, highlightcolor= "#3b404e")
    defaulterBook.grid(row = 5, padx = 160, pady = 8, sticky = "nesw")

"----------------------------------------------------------------------------------------------------------------------------------------------------"


"--------------------------------------------------------Delete Book Window---------------------------------------------------------------------------"

def delete_window():
    for child in myFrame.winfo_children():
        child.destroy()
    
    def delete():
        sno.grid_forget()
        entry_box_sno.grid_forget()
        name_book.grid_forget()
        entry_box_book.grid_forget()
        next_button.grid_forget()
        
        backend.delete_book(entry_box_sno.get(),entry_box_book.get())

        label_1= Label(myFrame, text ="\n\nSerial no. : "+entry_box_sno.get()+"\nBook Name : "+entry_box_book.get()+"\nis successfully deleted from the record.", relief = RAISED, fg = "white", bg = "#3b404e", bd=0 , font = ("Calibri",12), width=35, anchor="center")
        label_1.grid(row = 0, column = 0, padx=60, pady=5)
        
        #next button for going to the next step
        next_button_1=Button(myFrame, image=rounded_button, borderwidth=0, command = home_window)
        next_button_1.grid(row = 1, column = 0, pady=30)
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


    #importing button image, resizing it, creating an alias name
    button_image=Image.open("images/Rounded Button.png")
    button_image=button_image.resize((110,40),Image.ANTIALIAS)
    rounded_button=ImageTk.PhotoImage(button_image)

    #next button for going to the next step
    next_button=Button(myFrame, image=rounded_button, borderwidth=0, command=delete)
    next_button.grid(row = 2, column = 0, columnspan = 2, pady=30)
    next_button.config(highlightthickness=0)


"----------------------------------------------------------------------------------------------------------------------------------------------------"



root = Tk()
root.title("Login")
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



login_window()

root.mainloop()