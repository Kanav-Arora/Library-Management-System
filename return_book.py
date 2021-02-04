from tkinter import *

from PIL import ImageTk,Image


root = Tk()
root.title("Return Book")
root.geometry("600x500")
root.resizable(0,0)

bg = ImageTk.PhotoImage(Image.open("/Users/kushagrasinha/Library-Management-System/images/0_mMD5SlIbFvgkGo3l.jpeg"))
myLabel = Label(root,image = bg)
myLabel.place(x=0,y=0,relwidth=1,relheight=1)

myFrame = LabelFrame(root,bg="#3b404e", text = "Return Book",bd=3, fg = "white", padx=5, pady=5, labelanchor = "n")
myFrame.place(relx = 0.5, rely = 0.5, relwidth = 0.7, relheight = 0.6, anchor = CENTER)

# Name Of Student Label
student_name = Label(myFrame, text = "Name of student:", relief = RAISED, fg = "white", bg = "#3b404e", bd=0 , font = ("Calibri",12), padx= 20, pady = 20)
student_name.grid(row = 0, column = 0, padx= 15, pady = 20)

# BOOK ID Label
book_id = Label(myFrame, text = "Book ID:", relief = RAISED, fg = "white", bg = "#3b404e", bd=0 , font = ("Calibri",12))
book_id.grid(row = 1, column = 0, padx= 50, pady = 5)

# Name Of Student field
student_name_Enter = Entry(myFrame, highlightbackground= "#3b404e", bg = "#3b404e", borderwidth = 2, fg ="white",border=3)
student_name_Enter.grid(row = 0, column = 1, padx= 30, pady = 5)

# BOOK ID field
book_id_Enter = Entry(myFrame, highlightbackground= "#3b404e", bg = "#3b404e", borderwidth = 2, fg = "white",border=3)
book_id_Enter.grid(row = 1, column = 1, padx= 30, pady = 5)

# rounded button 
image =Image.open("/Users/kushagrasinha/Library-Management-System/images/Rounded Button.png")
image = image.resize((110, 40), Image.ANTIALIAS)
rounded = ImageTk.PhotoImage(image)



# Login Button
loginButton = Button(myFrame, image = rounded, borderwidth = 0)
loginButton.grid(row = 2, column = 0, columnspan = 2, padx= 50, pady = 30)
loginButton.config(highlightthickness=0)



root.mainloop()