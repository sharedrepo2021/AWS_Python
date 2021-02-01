import PyPDF2

from tkinter import Tk
from tkinter.filedialog import askopenfilename
from gtts import gTTS

class Pdftomp3():

    def __init__(self):
        self.tkin = Tk()
        self.strtext = ''


    def convertpdftomp3(self):
        self.tkin.withdraw()
        fileloc = askopenfilename()

        with open(fileloc, "rb") as pdffile:
            read_pdf = PyPDF2.PdfFileReader(pdffile)
            page = read_pdf.getPage(0)
            page_content = page.extractText()

        for text in page_content:
            self.strtext = self.strtext + text

        final_file = gTTS(text=self.strtext, lang='en')
        final_file.save("converted.mp3")


if __name__ == "__main__":
    pdftomp3 = Pdftomp3()
    pdftomp3.convertpdftomp3()
