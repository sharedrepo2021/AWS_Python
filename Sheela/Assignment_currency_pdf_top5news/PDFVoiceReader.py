import PyPDF2
import pyttsx3

def pdfAudioReader(filepath):

    url = filepath
    path = open(url, 'rb')
    pdfReader = PyPDF2.PdfFileReader(path)

    for page in pdfReader.pages:
        text = page.extractText()

    speak = pyttsx3.init()
    speak.say(text)
    speak.runAndWait()

def specificPage(filepath, pagenum):
    url = filepath
    path = open(url, 'rb')
    pdfReader = PyPDF2.PdfFileReader(path)
    try:
        pages = pdfReader.getPage(int(pagenum))
        text = pages.extractText()
        print(text)
        speaker = pyttsx3.init()
        speaker.say(text)
        speaker.runAndWait()
    except:
        print("Page not found")

if __name__ == '__main__':

    filepath = input("Enter the pdf file path to read:")
    option = input("Mention do you want to read entire pdf(E), specific page(S) :")
    if option == "E":
        pdfAudioReader(filepath)
    if option== "S":
        pagenum = input("Enter the specific page you want to read :")
        specificPage(filepath, pagenum)

