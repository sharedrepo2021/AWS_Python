import requests
import json

def displayNews(url):
    main_url = url
    print(main_url)
    news = requests.get(main_url).json()
    article = news["articles"]

    newarticle = []
    newarticledesc = []
    for arti in article:
        newarticle.append(arti['title'])
        newarticledesc.append(arti['description'])

    for i in range(5):
        print('\n', i+1, newarticle[i])
        print(newarticledesc[i], '\n')

if __name__ == '__main__':

    print("***************TOP 5 News*****************************")

    option_news = {
        1: 'India News',
        2: 'US News',
        3: 'BBC',
        4: 'Exit'
    }
    print(json.dumps(option_news, indent=4))
    while True:
        url = ""
        choice = input("Enter your choice: ")
        apikey = "4dccc5f982fe468096e887aabda3938a"
        if choice == "1":
            url = 'http://newsapi.org/v2/top-headlines?country=in&apiKey=' + apikey
        elif choice == "2":
            url = 'http://newsapi.org/v2/top-headlines?country=us&apiKey=' + apikey
        elif choice == "3":
            url = "https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=4dbc17e007ab436fb66416009dfb59a8"
        elif choice == "4":
            break
        else:
            print("Invalid choice!! Give numbers specified in the options")

        displayNews(url)