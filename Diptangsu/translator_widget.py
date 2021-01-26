from tkinter import *
from tkinter import ttk
from googletrans import LANGUAGES
from google_trans_new import google_translator


def translate():
    translator = google_translator()
    translate_text = translator.translate(text=Input_text.get(1.0, END),
                                          lang_src=get_lang_key(source_language.get()),
                                          lang_tgt=get_lang_key(destination_language.get()))
    Output_text.delete(1.0, END)
    Output_text.insert(END, translate_text)


def get_lang_key(lang_value):
    lang_dict = LANGUAGES

    for key, value in lang_dict.items():
        if value == lang_value:
            return key


root = Tk()
root.geometry('1050x500')
root.title('Translator widget')
root.config(bg='Ghost White')

Label(root, text='Enter text', font='arial 13 bold').place(x=200, y=50)
Input_text = Text(root, height=11, wrap=WORD, padx=5, pady=5, width=50)
Input_text.place(x=40, y=100)

Label(root, text='Output', font='arial 13 bold').place(x=800, y=50)
Output_text = Text(root, height=11, wrap=WORD, padx=5, pady=5, width=50)
Output_text.place(x=600, y=100)

language = list(LANGUAGES.values())

source_language = ttk.Combobox(root, values=language, width=20)
source_language.place(x=40, y=50)
source_language.set('english')

destination_language = ttk.Combobox(root, values=language, width=20)
destination_language.place(x=600, y=50)
destination_language.set('select output language')

translator_button = Button(root, text='Translate', font='arial 10 bold', pady=5, command=translate)
translator_button.place(x=490, y=100)

root.mainloop()
