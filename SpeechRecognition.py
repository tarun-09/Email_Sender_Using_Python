import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()

email_list = {
    'vaibhav': 'vaibhavgoel0230@gmail.com',
    'prateek': 'prateek.jain_cs.aiml19@gla.ac.in',
    'pratik': 'prateek.jain_cs.aiml19@gla.ac.in',
    'ayush': 'ayush.pandey_cs19@gla.ac.in',
    'tarun': 'tarun.agrawal_cs.aiml19@gla.ac.in',
    'ritesh': 'ritesh.chauhan_cs.aiml19@gla.ac.in'
}


def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_info():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass


def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("tarunagrawalgarg@gmail.com", "dkroibyyeetvhuma")
    email = EmailMessage()
    email['From'] = "tarunagrawalgarg@gmail.com"
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


def get_email_info():
    # talk('Enter your Username And Password for Sending Email:')
    # sender = input("Username:")
    # password = input("Password:")
    talk('To Whom you want to send email')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk('What is the subject of your email?')
    subject = get_info()
    talk('Tell me the text in your email')
    message = get_info()
    send_email(receiver, subject, message)
    talk('Congo! Your email is sent...')
    talk('Do you want to send more email?')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()


get_email_info()
