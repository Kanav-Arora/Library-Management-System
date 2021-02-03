from tkinter import *
from PIL import ImageTk,Image
import backend

root = Tk()
root.title("Home")
root.geometry("600x500")
root.resizable(0,0)

bg = ImageTk.PhotoImage(Image.open("images/0_mMD5SlIbFvgkGo3l.jpeg"))
myLabel = Label(root,image = bg)
myLabel.place(x=0,y=0,relwidth=1,relheight=1)

"""
    Frame: myFrame
    Frame declared
        bg color hex value: #3b404e
        fg color hex value: #FFFFFF
"""
myFrame = LabelFrame(root,bg="#3b404e", text = "Library Management System",bd=3, fg = "#FFFFFF", padx=5, pady=10, labelanchor = "n")
myFrame.place(relx = 0.5, rely = 0.5, relwidth = 0.7, relheight = 0.6, anchor = CENTER)

addBook = Button(myFrame,text = "Add Book", fg = "#FFFFFF", bg = "#3b404e", relief = GROOVE, borderwidth= 2)
addBook.config(highlightbackground = "#3b404e", highlightthickness = 2, highlightcolor= "#3b404e")
addBook.grid(row = 0,padx = 160, pady = 8, sticky = "nesw")

deleteBook = Button(myFrame,text = "Delete Book", fg = "#FFFFFF", bg = "#3b404e", relief = GROOVE)
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

root.mainloop()