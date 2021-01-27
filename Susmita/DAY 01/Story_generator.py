import random
import PyPDF2
import pyttsx3


when = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago', 'Last friday']
who = ['a rabbit', 'an elephant', 'a mouse', 'a turtle', 'my friend']
name = ['Ali', 'Miriam', 'Hoouk', 'Shyam', 'Ram']
residence = ['New York', 'Los Angeles', 'Serampore', 'Kolkata']
went = ['cinema', 'university', 'school', 'laundry']
happened = ['made a lot of friends', 'found a secret key', 'solved a mistery', 'wrote a book']

# print( random.choice(when) + ', ' + random.choice(who) + ' that lived in ' + random.choice(residence) + ', went to the ' + random.choice(went) + ' and ' + random.choice(happened))
f = open(r"C:\Users\Owner\Desktop\Story.pdf", "w")
f.write(random.choice(when) + ', ' + random.choice(who) + ' that lived in ' + random.choice(residence) + ', went to the ' + random.choice(went) + ' and ' + random.choice(happened))
f.close()
# path of the PDF file
path = open(r'C:\Users\Owner\Desktop\Story.pdf', 'rb')

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