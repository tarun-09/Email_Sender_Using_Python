from tkinter import *
from PIL import ImageTk, Image

bg = "#BFD3D6"
master = Tk()
master.geometry('500x600')
master.configure(bg=bg)
master.title("Email App")


titleLabel = Label(master, text="Email App", width=20, bg=bg, fg="#100A2D", font=('Calibri', 20)).place(x=100, y=10)
Label(master, text="ABOUT", width=30, bg=bg, font=('Calibri', 12)).place(x=115, y=45)

# Image 1
image1 = Image.open("FingerImages/1.png")
resize_image1 = image1.resize((100, 100))
test1 = ImageTk.PhotoImage(resize_image1)

label1 = Label(image=test1)
label1.image = test1
label1.place(x=10, y=85)


# Image 2
image2 = Image.open("FingerImages/2.png")
resize_image2 = image2.resize((100, 100))
test2 = ImageTk.PhotoImage(resize_image2)

label2 = Label(image=test2)
label2.image = test2
label2.place(x=10, y=205)


# Image 3
image3 = Image.open("FingerImages/3.png")
resize_image3 = image3.resize((100, 100))
test3 = ImageTk.PhotoImage(resize_image3)

label3 = Label(image=test3)
label3.image = test3
label3.place(x=10, y=325)


# Image 4
image4 = Image.open("FingerImages/4.png")
resize_image4 = image4.resize((100, 100))
test4 = ImageTk.PhotoImage(resize_image4)

label4 = Label(image=test4)
label4.image = test4
label4.place(x=10, y=445)

master.mainloop()