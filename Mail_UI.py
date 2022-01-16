from tkinter import *

bg = "#BFD3D6"
# Main Screen
master = Tk()
master.geometry('500x750')
master.configure(bg=bg)
master.title("Email App")

# Graphics
titleLabel = Label(master, text="Email App", width=20, bg=bg, fg="#100A2D", font=('Calibri', 20)).place(x=100, y=10)
Label(master, text="Fill your details to login", width=30, bg=bg, font=('Calibri', 12)).place(x=115, y=45)

Label(master, text="Email", bg=bg, font=('Calibri', 15)).place(x=30, y=85)
email = Entry(master, width=30, borderwidth=2, font=('Calibri', 15))
email.place(x=155, y=85)

Label(master, text="Password", bg=bg, font=('Calibri', 15)).place(x=30, y=135)
password = Entry(master, width=30, borderwidth=2, font=('Calibri', 15))
password.place(x=155, y=135)


def onLogin():
    print(f'You are logged in with {email.get()} and {password.get()}')


login = Button(master, text="Login", width=10, font=('Calibri', 13), command=onLogin).place(x=190, y=195)

Label(master, text="Compose Your E-mail", width=30, bg=bg, font=('Calibri', 15)).place(x=90, y=240)

Label(master, text="To", bg=bg, font=('Calibri', 15)).place(x=30, y=285)
user = Entry(master, width=30, borderwidth=2, font=('Calibri', 15))
user.place(x=155, y=285)

Label(master, text="Subject", bg=bg, font=('Calibri', 15)).place(x=30, y=335)
subject = Entry(master, width=30, borderwidth=2, font=('Calibri', 15))
subject.place(x=155, y=335)

Label(master, text="Message", bg=bg, font=('Calibri', 15)).place(x=30, y=385)
body = Text(master, width=30, height=10, borderwidth=2, font=('Calibri', 15))
body.place(x=155, y=385)

def onSend():
    print(f'You have sent mail to {user.get()} with Subject {subject.get()} and Body {body.get(1.0,"end")}')


login = Button(master, text="Send", width=10, font=('Calibri', 13), command=onSend).place(x=190, y=655)

master.mainloop()
