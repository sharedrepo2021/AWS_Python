import os
import smtplib

Email_address = 'pythondev2021@gmail.com'
Email_password = 'pass4python'

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(Email_address, Email_password)

    subject = input("Enter the subject of the email:: ")
    body = input("Type the msg here:: ")
    msg = f'Subject : {subject}\n\n{body}'

    smtp.sendmail(Email_address, 'dipan.saha@gmail.com', msg)