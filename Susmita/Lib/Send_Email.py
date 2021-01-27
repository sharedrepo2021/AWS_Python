import smtplib


class Email:
    def __init__(self):
        self.email_address = 'pythondev2021@gmail.com'
        self.email_password = 'pass4python'

    def send_email(self, subject, body):
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()

            smtp.login(self.email_address, self.email_password)
            msg = f'Subject : {subject}\n\n{body}'

            smtp.sendmail(self.email_address, 'dipan.saha@gmail.com', msg)
