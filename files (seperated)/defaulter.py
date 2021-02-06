"""
This code is the GUI for identifying the defaulters in library Management System.
Firstly the user will have a choice between two modes:
1) defaulter's list
2) book lost

if the user chooses defaulter' list the program will show:
1) display defaulter's list
    =>serial number of issued book
    =>name of student
    =>due date
    =>fine
2) next button for going to main menu

if the user chooses book lost the program will show:
1) entry field for name of student
2) entry field for name of book
3) it will ask the users choice for:
    =>paying original price of the book
      and then display:
         1) the original price of lost book
         2) next button to go to the main menu
    =>to exchange another book to the library
      and then display:
         1) text saying that the book is deleted from the database 
         2) next button to add new details(this will direct the user to add_book.py) 
"""
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

#creating window, giving title and size
root=Tk()
root.title("Defaulter Identification")
#root.iconbitmap()
root.geometry("600x500")
root.resizable(0,0)

#putting background image
back_ground = ImageTk.PhotoImage(Image.open("images/0_mMD5SlIbFvgkGo3l.jpeg"))
back_ground_label = Label(root, image = back_ground)
back_ground_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

#importing button image, resizing it, creating an alias name
button_image = Image.open("images\Rounded Button.png")
button_image = button_image.resize((110,40), Image.ANTIALIAS)
rounded_button = ImageTk.PhotoImage(button_image)

#frame for defaulter identification
frame_1 = LabelFrame(root, bg = "#3b404e", text = "Defaulter Identification", bd = 3, fg = "white", padx = 5, pady = 5, labelanchor = "n")
frame_1.place(relx = 0.5, rely = 0.5, relwidth = 0.7, relheight = 0.6, anchor = CENTER)



r = IntVar()          #integer variable 

#function for disabling the other radio button when one is selected
def disable():
    if r.get()==1:
        radio_button_2.deselect

        for child in frame_1.winfo_children():
                child.destroy()

        #titles of defaulter's list
        Title = Label(frame_1, text = "%-10s%-25s%-15s%-10s"%('Sr. No.','Name of Student','Due Date','Fine'), relief = RAISED, fg = "white", bg = "#3b404e", bd = 0 , font = ("Calibri",12))
        Title.grid(row = 3, column = 0, columnspan = 2, padx = 15, pady = 8)

        line = Label(frame_1, text = "----------------------------------------------------------------------------", relief = RAISED, fg = "white", bg = "#3b404e", bd = 0 , font = ("Calibri",12), width = 49, anchor = 'w')
        line.grid (row = 4, column = 0, columnspan = 2, pady = 5)

        cur = [
        ['A1','Arnav Batra','17-01-2001','100'],
        ['B1','Kanav Arora','15-05-2002','100'],
        ['C1','Kushagra Sinha','19-04-2002','100'],
        ['D1','Satvik Jalan','15-12-2001','100'],
        ['E1','Surbhi Goel','10-08-2002','100'] ]

        try:
            global y
            y = 5

            for i in cur:
                def_list = Label(frame_1, text= "%-10s%-25s%-15s%-10s"%(i[0],i[1],i[2],i[3]) , relief = RAISED, fg = "white", bg ="#3b404e", bd = 0 , font = ("Calibri",12))
                def_list.grid(row = y, column = 0, columnspan = 2, pady=1)
                y += 1
            
        except:
            messagebox.showinfo("Failed to fetch files from database")

        #next button for going to the next step
        #this will take you to main menu
        next_button_3 = Button(frame_1, image = rounded_button, borderwidth = 0)
        next_button_3.grid(row = y+1, column = 0, columnspan = 2, pady=8)
        next_button_3.config(highlightthickness = 0)

    else:
        radio_button_1.deselect

        for child in frame_1.winfo_children():
                child.destroy()

        #label asking for name of defaulter
        name = Label(frame_1, text = "Name of Defaulter:", relief = RAISED, fg = "white", bg = "#3b404e", bd = 0 , font = ("Calibri",12), padx= 40, pady = 10)
        name.grid(row = 3, column = 0)

        #entry box to type the name of defaulter
        entry_box_name = Entry(frame_1, highlightbackground = "#3b404e", bg = "#3b404e", borderwidth = 2, fg = "white")
        entry_box_name.grid(row = 3, column = 1)

        #label asking for name of book
        name_book = Label(frame_1, text = "Name of Book:", relief = RAISED, fg = "white", bg = "#3b404e", bd = 0 , font = ("Calibri",12), padx= 40, pady = 10)
        name_book.grid(row = 4, column = 0)

        #entry box to type the name of book
        entry_box_book = Entry(frame_1, highlightbackground = "#3b404e", bg = "#3b404e", borderwidth = 2, fg = "white")
        entry_box_book.grid(row = 4, column = 1)

        r_2 = IntVar()       #integer variable

        def disable_2():
            if r_2.get()==3:
                radio_button_4.deselect

                global price
                price='100'

                #label to display original price        
                label_1 = Label(frame_1, text = "Origial price to be paid: Rs."+price+"\n", relief = RAISED, fg = "white", bg = "#3b404e", bd = 0 , font = ("Calibri",12), width=46, anchor = 'center')
                label_1.grid(row = 7, column = 0, columnspan = 2, padx = 20, pady = 2)

                #next button for going to the next step
                #this will take you back to main menu
                next_button_1 = Button(frame_1, image = rounded_button, borderwidth = 0)
                next_button_1.grid(row = 8, column = 0, columnspan = 2, pady = 8)
                next_button_1.config(highlightthickness = 0)

            else:
                radio_button_3.deselect

                #label to display message        
                label_2 = Label(frame_1, text = "To add new book details and delete current book details\n click on next", relief = RAISED, fg = "white", bg = "#3b404e", bd = 0 , font = ("Calibri",12))
                label_2.grid(row = 7, column = 0, columnspan = 2, padx = 5, pady = 2)

                #next button for going to the next step
                #this button will take you to add book deetails
                next_button_2 = Button(frame_1, image = rounded_button, borderwidth = 0)
                next_button_2.grid(row = 8, column = 0, columnspan = 2, pady = 8)
                next_button_2.config(highlightthickness = 0)

        #label asking for choice
        option = Label(frame_1, text = "Options:", relief = RAISED, fg = "white", bg = "#3b404e", bd=0 , font = ("Calibri",12), width = 5, anchor = 'center')
        option.grid(row = 5, column = 0,padx = 40, pady= 5, sticky='news')

        #radio button 3 for pay price
        radio_button_3 = Radiobutton(frame_1, text = "pay original price", font = ("Calibri",12), width = 22, fg = "white", bg = "#3b404e",selectcolor = "#3b404e", activebackground = "#3b404e", variable = r_2, value = 3, command = disable_2)
        radio_button_3.grid(row = 5, column = 1, pady = 5)

        #radio button 4 for add new book
        radio_button_4 = Radiobutton(frame_1, text = "add new book", font = ("Calibri",12), width = 20, fg = "white", bg = "#3b404e", selectcolor = "#3b404e", activebackground = "#3b404e", anchor = "center", variable = r_2, value = 4, command = disable_2)
        radio_button_4.grid(row = 6, column = 1, pady = 5)

#label asking for the fault
mode = Label(frame_1, text = "Mode:", relief = RAISED, fg = "white", bg = "#3b404e", bd=0 , font = ("Calibri",12))
mode.place(relx = 0.2, rely = 0.35)

#radio button 1 for late submission
radio_button_1 = Radiobutton(frame_1, text = "defaulter's list", font = ("Calibri",12), width = 16, fg = "white", bg = "#3b404e",selectcolor = "#3b404e", activebackground = "#3b404e", anchor = "w", variable = r, value = 1, command = disable)
radio_button_1.place(relx = 0.5, rely = 0.3)

#radio button 2 for book lost
radio_button_2 = Radiobutton(frame_1, text = "book lost", font = ("Calibri",12), width = 16, fg = "white", bg = "#3b404e", selectcolor = "#3b404e", activebackground = "#3b404e", anchor = "w", variable = r ,value = 2, command = disable)
radio_button_2.place(relx = 0.5, rely = 0.45)

root.mainloop()