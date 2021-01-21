import smtplib
import os
from email.message import EmailMessage
import re


class SendingEmail:
    def __init__(self):
        self.fromemail = 0
        self.fromemailpass = 0

    def send_mail(self, toemaillist, subject, message):

        self.fromemail = os.environ.get('EMAIL_USER')
        self.fromemailpass = os.environ.get('EMAIL_PASS')

        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = self.fromemail
        msg['To'] = ', '.join(toemaillist)
        msg.set_content(message)

        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(self.fromemail, self.fromemailpass)
        server.send_message(msg)
        server.quit()
        print(' Mail has been sent successfully .')



if __name__ == '__main__':

    print("SEND EMAIL")
    toemaillist = []
    toemail = ""

    numtoemaidid = int(input("Enter the number of email id to be added to the To list"))

    for i in range(numtoemaidid):
        toemaidid = input("Enter the email id to send the email :")

        while not re.match("^[a-z0-9]+[\.]?[a-z0-9]+[@]\w+[.]\w{2,3}$", toemaidid):
            print("Invalid Email ID! Make sure you give proper email ID")
            break

        toemaillist.append(toemaidid)

    subject = input("Enter the subject of the Email :")
    message = input("Enter the message for the Email :")

    sendemail = SendingEmail()
    sendemail.send_mail(toemaillist, subject, message)
