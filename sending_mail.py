import os
import smtplib

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

print(EMAIL_ADDRESS)
print(EMAIL_PASSWORD)
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)

    subject = 'Invitation for dinner'
    body = 'I would like to invite you for dinner at my home at 7 pm today.'

    msg = f'Subject:{subject}\n\n{body}'

    smtp.sendmail('tarunagrawalgarg@gmail.com', 'tarun.agrawal_cs.aiml19@gla.ac.in', msg)

