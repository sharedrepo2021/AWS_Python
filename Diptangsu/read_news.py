from newspaper import Article
import nltk
import pyttsx3


url = 'https://timesofindia.indiatimes.com/india/wont-repeal-farm-laws-let-sc-decide-govt-hardens-stance/articleshow/80180510.cms'

article = Article(url)
article.download()
article.parse()
article.nlp()

text = article.text

# article.text()

speaker = pyttsx3.init()
speaker.say(text)
speaker.runAndWait()
