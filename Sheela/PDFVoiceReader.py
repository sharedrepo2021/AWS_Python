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

if __name__ == '__main__':

    filepath = input("Enter the pdf file path to read:")
    print(filepath)
    pdfAudioReader(filepath)