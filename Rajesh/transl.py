from google_trans_new import google_translator
translator = google_translator()
translate_text = translator.translate('what is your name?',lang_tgt='ml')
print(translate_text)