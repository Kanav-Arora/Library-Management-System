"""
This code only has the first window where we ask the user to input the name of defaulter,what fault he/she has done and press the next button.

the next window will take direct the user according to his/her choice.

this code can open two kinds of modes
1) late submission
2) book lost
"""
from tkinter import *
from PIL import ImageTk,Image

#creating window, giving title and size
root=Tk()
root.title("Defaulter Identification")
#root.iconbitmap()
root.geometry("600x500")
root.resizable(0,0)

#putting background image
back_ground=ImageTk.PhotoImage(Image.open("C:/Users/surbh/python_projects/0_mMD5SlIbFvgkGo3l.jpeg"))
back_ground_label=Label(root,image=back_ground)
back_ground_label.place(x=0,y=0,relwidth=1,relheight=1)

#-------------------------------------------------------------------------
#                         FIRST WINDOW
#-------------------------------------------------------------------------

#frame for defaulter identification
frame_1 = LabelFrame(root,bg="#3b404e", text = "Defaulter Identification",bd=3, fg = "white", padx=5, pady=5, labelanchor = "n")
frame_1.place(relx = 0.5, rely = 0.5, relwidth = 0.7, relheight = 0.6, anchor = CENTER)

#label asking for name of defaulter
name= Label(frame_1, text = "Name of Defaulter:", relief = RAISED, fg = "white", bg = "#3b404e", bd=0 , font = ("Calibri",12), padx= 20, pady = 20)
name.grid(row = 0, column = 0, padx= 15, pady = 20)

#entry box to type the name of defaulter
entry_box_name=Entry(frame_1,highlightbackground= "#3b404e", bg = "#3b404e", borderwidth = 2, fg = "white")
entry_box_name.grid(row = 0, column = 1, padx= 50, pady = 5)

#label asking for the fault
fault= Label(frame_1, text = "Fault:", relief = RAISED, fg = "white", bg = "#3b404e", bd=0 , font = ("Calibri",12))
fault.grid(row = 1, column = 0)

r=IntVar()          #integer variable 

#function for disabling the other radio button when one is selected
def disable():
    if r.get()==1:
        radio_button_2.config(state=DISABLED)
    else:
        radio_button_1.config(state=DISABLED)

#radio button 1 for late submission
radio_button_1=Radiobutton(frame_1, text="late submission", font = ("Calibri",12), width=16, fg="white",bg = "#3b404e",selectcolor="#3b404e", activebackground="#3b404e", anchor="sw", variable=r, value=1, command=disable)
radio_button_1.grid(row=1,column=1)

#radio button 2 for book lost
radio_button_2=Radiobutton(frame_1, text="book lost", font = ("Calibri",12),width=16, fg="white", bg = "#3b404e",selectcolor="#3b404e", activebackground="#3b404e", anchor="sw", variable=r ,value=2, command=disable)
radio_button_2.grid(row=2,column=1)

#importing button image, resizing it, creating an alias name
button_image=Image.open("C:/Users/surbh/PythonCSEProject/images/Rounded Button.png")
button_image=button_image.resize((110,40),Image.ANTIALIAS)
rounded_button=ImageTk.PhotoImage(button_image)

#next button for going to the next step
next_button=Button(frame_1, image=rounded_button, borderwidth=0)
next_button.grid(row = 3, column = 0, columnspan = 2, padx= 50, pady = 30)
next_button.config(highlightthickness=0)

root.mainloop()