import PyPDF2
import pyttsx3

# path of the PDF file
path = open(r'C:\Users\dipan\Desktop\test.pdf', 'rb')

# creating a PdfFileReader object
pdfReader = PyPDF2.PdfFileReader(path)

# the page with which you want to start
# this will read the page of 1st page.
from_page = pdfReader.getPage(0)

# extracting the text from the PDF
text = from_page.extractText()

# reading the text
speak = pyttsx3.init()
speak.say(text)
speak.runAndWait()
