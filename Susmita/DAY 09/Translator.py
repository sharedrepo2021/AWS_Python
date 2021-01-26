# from translate import Translator
#
# text = input("Enter the text you want to translate: ")
# ToLang = input("Enter the Target language Name: ")
#
# translator = Translator(to_lang=ToLang)
# print('Here is your converted Text: ', translator.translate(text))



# import googletrans
#
# lang_dict = googletrans.LANGUAGES
#
# for key, value in lang_dict.items():
#     print(key, value)


# import goslate
#
# text = "I like food"
#
# gs = goslate.Goslate()
# translatedText = gs.translate(text, 'ml')
#
# print(translatedText)


from google_trans_new import google_translator

translator = google_translator()
translate_text = translator.translate('what is your name?', lang_tgt='ta')

print(translate_text)