from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import backend

root = Tk()
root.title("Login")
root.geometry("600x500")
root.resizable(0,0)

bg = ImageTk.PhotoImage(Image.open("images/0_mMD5SlIbFvgkGo3l.jpeg"))
myLabel = Label(root,image = bg)
myLabel.place(x=0,y=0,relwidth=1,relheight=1)

myFrame = LabelFrame(root,bg="#3b404e", text = "Account Login",bd=3, fg = "white", padx=5, pady=5, labelanchor = "n")
myFrame.place(relx = 0.5, rely = 0.5, relwidth = 0.7, relheight = 0.6, anchor = CENTER)

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
image =Image.open("images/Rounded Button.png")
image = image.resize((110, 40), Image.ANTIALIAS)
rounded = ImageTk.PhotoImage(image)

def value():
    global idEnter
    global passEnter
    idval = idEnter.get()
    passval = passEnter.get()
    out = backend.login_data(idval,passval)
    if out==1:
        messagebox.showinfo("Success","Welcome")
    else:
        messagebox.showinfo("Failed","Invalid Credentials")


# Login Button
loginButton = Button(myFrame, image = rounded, borderwidth = 0, command= value)
loginButton.grid(row = 2, column = 0, columnspan = 2, padx= 50, pady = 30)
loginButton.config(highlightthickness=0)

# registration button
register = Button(myFrame, text = "Create new account", fg = "white", bg = "#3b404e", relief = FLAT)
register.grid(row = 3, column = 0, columnspan = 2, padx= 50)
register.config(highlightthickness=0)

root.mainloop()