import smtplib
import os
from email.message import EmailMessage
import re


class SendingEmail:
    def __init__(self):
        self.fromemail = 0
        self.fromemailpass = 0
        self.finallist = []
        self.errorlist = []

    def send_mail(self, toemaillist, subject, message):

        self.fromemail = os.environ.get('EMAIL_USER')
        self.fromemailpass = os.environ.get('EMAIL_PASS')

        for a in toemaillist:
            isvalid = self.check(a)

            if isvalid:
                self.finallist.append(a)
            else:
                self.errorlist.append(a)

        if len(self.errorlist) > 0:
            print("Mail not sent to the following email as they were Invalid", self.errorlist)

        if len(self.errorlist) != len(toemaillist):

            msg = EmailMessage()
            msg['Subject'] = subject
            msg['From'] = self.fromemail
            msg['To'] = ', '.join(self.finallist)
            msg.set_content(message)
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.login(self.fromemail, self.fromemailpass)
            server.send_message(msg)
            server.quit()
            print(' Mail has been sent successfully .')

        else:
            print("No Valid Email ID were there to send email")



    def check(self, email):
        regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
        if (re.search(regex, email)):
            return True
        else:
            return False



if __name__ == '__main__':


    print("SEND EMAIL")
    toemaillist = []
    toemail = ""

    numtoemaidid = int(input("Enter the number of email id to be added to the To list"))

    for i in range(numtoemaidid):
        toemaidid = input("Enter the email id to send the email :")
        toemaillist.append(toemaidid)

    subject = input("Enter the subject of the Email :")
    message = input("Enter the message for the Email :")

    sendemail = SendingEmail()
    sendemail.send_mail(toemaillist, subject, message)
