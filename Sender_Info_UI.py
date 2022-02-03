from tkinter import *


class LOGIN:

    def __init__(self):
        bg = "#BFD3D6"
        master = Tk()
        master.geometry('500x250')
        master.configure(bg=bg)
        master.title("Email App")

        titleLabel = Label(master, text="Email App", width=20, bg=bg, fg="#100A2D", font=('Calibri', 20)).place(x=100,
                                                                                                                y=10)
        Label(master, text="Fill your details to login", width=30, bg=bg, font=('Calibri', 12)).place(x=115, y=45)

        Label(master, text="Email", bg=bg, font=('Calibri', 15)).place(x=30, y=85)
        email = Entry(master, width=30, borderwidth=2, font=('Calibri', 15))
        email.place(x=155, y=85)

        Label(master, text="Password", bg=bg, font=('Calibri', 15)).place(x=30, y=135)
        password = Entry(master, width=30, borderwidth=2, font=('Calibri', 15))
        password.place(x=155, y=135)

        login = Button(master, text="Login", width=10, font=('Calibri', 13), command=self.onLogin).place(x=245, y=195)
        master.mainloop()

    @staticmethod
    def onLogin():
        print('You are logged in')
