from tkinter import *
from PIL import ImageTk, Image

bg = "#BFD3D6"
master = Tk()
master.geometry('500x500')
master.configure(bg=bg)
master.title("Email App")


titleLabel = Label(master, text="Email App", width=20, bg=bg, fg="#100A2D", font=('Calibri', 20)).place(x=100, y=10)
Label(master, text="ABOUT", width=30, bg=bg, font=('Calibri', 12)).place(x=115, y=45)

canvas = Canvas(master, width=300, height=300)
canvas.pack()
img = ImageTk.PhotoImage(Image.open("FingerImages/1.png"))
canvas.create_image(20, 20, anchor=NW, image=img)

master.mainloop()