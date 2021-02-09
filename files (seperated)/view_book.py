from tkinter import *

from PIL import ImageTk, Image

root = Tk()
root.title('VIEW BOOK')
root.iconbitmap('/Users/apple/Downloads/library_icon.ico')
root.geometry("600x500")
root.resizable(0,0)

#Background Image
back_image = ImageTk.PhotoImage(Image.open("/Users/apple/Library-Management-System/images/0_mMD5SlIbFvgkGo3l.jpeg"))
myLabel = Label(image=back_image)
myLabel.place(x=0,y=0,relwidth=1,relheight=1)

#Frame
main_Frame = LabelFrame(root,bg="#3b404e", text = "View Book List",bd=3, fg = "white", padx=5, pady=5, labelanchor = "n")
main_Frame.place(relx = 0.5, rely = 0.5, relwidth = 0.7, relheight = 0.6, anchor = CENTER)

#Label
Label(main_Frame, text="%-15s%-20s%-20s%-20s" % ('S.No','Title', 'Author', 'Status'),bg="#3b404e", fg='white', width=48).grid(pady=2, row=0)
Label(main_Frame, text="--------------------------------------------------------------------", bg="#3b404e", fg='white').grid(pady=2, row=1, columnspan=4)

my_list = [["   1.", "Harry Potter", "J.K Rowling", " Yes"],["   2.", "Invisible Man", "H.G Wells", "  Yes"],[" 3.", "Dracula", "Bram S.", "    Yes"], [" 4.", "Beloved", "Toni M.", "    Yes"]]


#try:
y = 3
for i in my_list:

    Label(main_Frame, text="%-15s%-20s%-20s%-20s" % (i[0], i[1], i[2], i[3]), bg="#3b404e", fg='white', width=48).grid(pady=5, row=y)
    y += 1


#next button
image =Image.open("/Users/apple/Library-Management-System/images/Rounded Button.png")
image = image.resize((110, 40), Image.ANTIALIAS)
rounded = ImageTk.PhotoImage(image)

back_button = Button(main_Frame, image = rounded, borderwidth = 0, anchor="center")
back_button.grid(row = 7, padx=5, pady = 15)
back_button.config(highlightthickness=0)


root.mainloop()