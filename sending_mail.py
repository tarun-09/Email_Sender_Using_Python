import smtplib
from email.message import EmailMessage


class SENDING_MAIL:
    def __init__(self):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        return server

    def onLogin(self, server, email, password):
        server.login(email, password)
        return server

    def onSend(self, server, user, to, subject, body):
        email = EmailMessage()
        email['From'] = user
        email['To'] = to
        email['Subject'] = subject
        email.set_content(body)
        server.send_message(email)
