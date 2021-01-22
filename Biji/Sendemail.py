import smtplib
from email.message import EmailMessage


class Sendmail:

    def __init__(self):
        sender = ""
        pwd = ""
        receiver =[]
        message=""

    def getinputs(self):
       self.sender = input("Enter your Email ID")
       self. pwd = input("Enter your password")
       self. receiver = input("TO: ")
       self.  message=EmailMessage()
       self.message['subject'] = input("Subject")
       self.message['From'] =self.sender
       self.message['To'] = self.receiver
       self.message.set_content(input("Enter the message:"))

    def sendmail(self):
        try:
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.ehlo()
            s.starttls()
            s.login(self.sender,self.pwd)
            s.sendmail(self.sender, self.receiver, self.message.as_string())
            s.close()
            print("Successfully sent email to '{}'".format(self.receiver))
        except smtplib.SMTPException:
            print("Error: unable to send email")


if __name__ == '__main__':
    objsendmail = Sendmail()
    objsendmail.getinputs()
    objsendmail.sendmail()

