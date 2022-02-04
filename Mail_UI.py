from tkinter import *
from email.message import EmailMessage


class MAIL:

    def __init__(self):
        bg = "#BFD3D6"
        # Main Screen
        master = Tk()
        master.geometry('500x500')
        master.configure(bg=bg)
        master.title("Email App")

        # Graphics
        titleLabel = Label(master, text="Email App", width=20, bg=bg, fg="#100A2D", font=('Calibri', 20)).place(x=100,
                                                                                                                y=10)

        Label(master, text="Compose Your E-mail", width=30, bg=bg, font=('Calibri', 15)).place(x=90, y=50)

        Label(master, text="To", bg=bg, font=('Calibri', 15)).place(x=30, y=85)
        to = Entry(master, width=30, borderwidth=2, font=('Calibri', 15))
        to.place(x=155, y=85)

        Label(master, text="Subject", bg=bg, font=('Calibri', 15)).place(x=30, y=135)
        subject = Entry(master, width=30, borderwidth=2, font=('Calibri', 15))
        subject.place(x=155, y=135)

        Label(master, text="Message", bg=bg, font=('Calibri', 15)).place(x=30, y=185)
        body = Text(master, width=30, height=10, borderwidth=2, font=('Calibri', 15))
        body.place(x=155, y=185)
        check = Button(master, text="Check", width=10, font=('Calibri', 13)).place(x=245, y=455)

        master.mainloop()
        list = (to, subject, body)
        return list

    def onSend(self, server, email, to, subject, body):
        email = EmailMessage()
        email['From'] = email
        email['To'] = to
        email['Subject'] = subject
        email.set_content(body)
        server.send_message(email)
        print("SEND")
