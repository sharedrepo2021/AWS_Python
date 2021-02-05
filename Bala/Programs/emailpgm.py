from emailgmail import SendEmail

_send_to = ['bala.rmur@gmail.com']
_sub = 'Subject'
_text = 'This is the text message'

_send_email_to = SendEmail()
_send_email_to.sendemail(_sub, _send_to, _text)
