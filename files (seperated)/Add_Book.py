from tkinter import *

from PIL import ImageTk,Image


root = Tk()
root.title("Return Book")
root.geometry("600x500")
root.resizable(0,0)

bg = ImageTk.PhotoImage(Image.open("/Users/arnavbatra/Library-Management-System/images/0_mMD5SlIbFvgkGo3l.jpeg"))
myLabel = Label(root,image = bg)
myLabel.place(x=0,y=0,relwidth=1,relheight=1)

myFrame = LabelFrame(root,bg="#3b404e", text = "Return Book",bd=3, fg = "white", padx=5, pady=5, labelanchor = "n")
myFrame.place(relx = 0.5, rely = 0.5, relwidth = 0.7, relheight = 0.9, anchor = CENTER)

# Name of book Label
book_name = Label(myFrame, text = "Book Name:", relief = RAISED, fg = "white", bg = "#3b404e", bd=0 , font = ("Calibri",12), padx= 20, pady = 20)
book_name.grid(row = 0, column = 0, padx= 15, pady = 5)

# Name Of Author Label
author_name = Label(myFrame, text = "Name of Author:", relief = RAISED, fg = "white", bg = "#3b404e", bd=0 , font = ("Calibri",12), padx= 20, pady = 20)
author_name.grid(row = 2, column = 0, padx= 5, pady = 5)

# Date Label
date_name = Label(myFrame, text = "Date \n (DD/MM/YYYY):", relief = RAISED, fg = "white", bg = "#3b404e", bd=0 , font = ("Calibri",12), padx= 20, pady = 20)
date_name.grid(row = 5, column = 0, padx= 5)

# Price Label
price_name = Label(myFrame, text = "Price:", relief = RAISED, fg = "white", bg = "#3b404e", bd=0 , font = ("Calibri",12), padx= 20, pady = 20)
price_name.grid(row = 4, column = 0, padx= 15, pady = 5)

# BOOK ID Label
book_id = Label(myFrame, text = "Book ID:", relief = RAISED, fg = "white", bg = "#3b404e", bd=0 , font = ("Calibri",12))
book_id.grid(row = 1, column = 0, padx= 50, pady = 5)

# Category Label
category_name = Label(myFrame, text = "Category:", relief = RAISED, fg = "white", bg = "#3b404e", bd=0 , font = ("Calibri",12))
category_name.grid(row = 3, column = 0, padx= 50, pady = 5)

# Name Of Book field
book_name_Enter = Entry(myFrame, highlightbackground= "#3b404e", bg = "#3b404e", borderwidth = 2, fg ="white",border=3)
book_name_Enter.grid(row = 0, column = 1, padx= 30, pady = 5)

# Name Of Author field
author_name_Enter = Entry(myFrame, highlightbackground= "#3b404e", bg = "#3b404e", borderwidth = 2, fg ="white",border=3)
author_name_Enter.grid(row = 2, column = 1, padx= 30, pady = 5)

# BOOK ID field
book_id_Enter = Entry(myFrame, highlightbackground= "#3b404e", bg = "#3b404e", borderwidth = 2, fg = "white",border=3)
book_id_Enter.grid(row = 1, column = 1, padx= 30, pady = 5)

# Price field
price_name_Enter = Entry(myFrame, highlightbackground= "#3b404e", bg = "#3b404e", borderwidth = 2, fg = "white",border=3)
price_name_Enter.grid(row = 4, column = 1, padx= 30, pady = 5)

# Category field
category_name_Enter = Entry(myFrame, highlightbackground= "#3b404e", bg = "#3b404e", borderwidth = 2, fg = "white",border=3)
category_name_Enter.grid(row = 3, column = 1, padx= 30, pady = 5)

# Date field
date_name_Enter = Entry(myFrame, highlightbackground= "#3b404e", bg = "#3b404e", borderwidth = 2, fg = "white",border=3)
date_name_Enter.grid(row = 5, column = 1, padx= 30)

# rounded button
image =Image.open("/Users/arnavbatra/Library-Management-System/images/Rounded Button.png")
image = image.resize((110, 40), Image.ANTIALIAS)
rounded = ImageTk.PhotoImage(image)



# Login Button
loginButton = Button(myFrame, image = rounded, borderwidth = 0)
loginButton.grid(row = 6, column = 0, columnspan = 2, padx= 50, pady = 15)
loginButton.config(highlightthickness=0)



root.mainloop()