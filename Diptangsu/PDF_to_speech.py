import pyttsx3
import PyPDF2

book = open(r'G:\Study Matterial\candcppbasics.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(book)

while True:
    pages = pdf_reader.getPage(int(input('Enter the page number you want to read: ')))
    text = pages.extractText()

    speaker = pyttsx3.init()
    speaker.say(text)
    speaker.runAndWait()
