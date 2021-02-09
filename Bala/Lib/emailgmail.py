import os
import smtplib
from email.message import EmailMessage


class Handle_Send_Email:
    def __init__(self):
        self.eaddress = os.environ.get('EMAIL_USER')
        self.epassword = os.environ.get('EMAIL_PASS')
        self.sender = 'bala08mur@gmail.com'

    def send_email(self, subject, receiver, content):
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = self.sender
        msg['To'] = receiver
        txt = content
        msg.set_content(txt)

        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(self.eaddress, self.epassword)
        server.send_message(msg)
        server.quit()
