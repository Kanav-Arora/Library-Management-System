"""
This code deletes the record of an already existing book in database.

As input from user it takes:
1) book serial number
2) book name
"""
from tkinter import *
from PIL import ImageTk,Image
import backend

#creating window, giving title and size
root=Tk()
root.title("Delete Book")
#root.iconbitmap()
root.geometry("600x500")
root.resizable(0,0)

#putting background image
back_ground=ImageTk.PhotoImage(Image.open("images/0_mMD5SlIbFvgkGo3l.jpeg"))
back_ground_label=Label(root, image=back_ground)
back_ground_label.place(x=0, y=0, relwidth=1, relheight=1)

#frame for delete book
frame_1 = LabelFrame(root, bg="#3b404e", text = "Delete Book",bd=3, fg = "white", padx=5, pady=5, labelanchor = "n")
frame_1.place(relx = 0.5, rely = 0.5, relwidth = 0.7, relheight = 0.6, anchor = CENTER)

def delete():
    sno.grid_forget()
    entry_box_sno.grid_forget()
    name_book.grid_forget()
    entry_box_book.grid_forget()
    next_button.grid_forget()
    
    backend.delete_book(entry_box_sno.get(),entry_box_book.get())

    label_1= Label(frame_1, text ="\n\nSerial no. : "+entry_box_sno.get()+"\nBook Name : "+entry_box_book.get()+"\nis successfully deleted from the record.", relief = RAISED, fg = "white", bg = "#3b404e", bd=0 , font = ("Calibri",12), width=35, anchor="center")
    label_1.grid(row = 0, column = 0, padx=60, pady=5)
    
    

    #next button for going to the next step
    next_button_1=Button(frame_1, image=rounded_button, borderwidth=0)
    next_button_1.grid(row = 1, column = 0, pady=30)
    next_button_1.config(highlightthickness=0)

#label asking for serial number of book
sno= Label(frame_1, text = "Serial No. :", relief = RAISED, fg = "white", bg = "#3b404e", bd=0 , font = ("Calibri",12), padx= 20, pady = 20)
sno.grid(row = 0, column = 0, padx= 20, pady = 15)

#entry box to type the serial number of book
entry_box_sno=Entry(frame_1, highlightbackground= "#3b404e", bg = "#3b404e", borderwidth = 2, fg = "white")
entry_box_sno.grid(row = 0, column = 1, padx= 50, pady = 5)

#label asking for name of book
name_book= Label(frame_1, text = "Name of Book :", relief = RAISED, fg = "white", bg = "#3b404e", bd=0 , font = ("Calibri",12), padx= 20, pady = 20)
name_book.grid(row = 1, column = 0, padx= 20, pady = 15)

#entry box to type the name of book
entry_box_book=Entry(frame_1, highlightbackground= "#3b404e", bg = "#3b404e", borderwidth = 2, fg = "white")
entry_box_book.grid(row = 1, column = 1, padx= 50, pady = 5)


#importing button image, resizing it, creating an alias name
button_image=Image.open("images/Rounded Button.png")
button_image=button_image.resize((110,40),Image.ANTIALIAS)
rounded_button=ImageTk.PhotoImage(button_image)

#next button for going to the next step
next_button=Button(frame_1, image=rounded_button, borderwidth=0, command=delete)
next_button.grid(row = 2, column = 0, columnspan = 2, pady=30)
next_button.config(highlightthickness=0)

root.mainloop()