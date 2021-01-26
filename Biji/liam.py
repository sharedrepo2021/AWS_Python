import requests


class Currencyconverter:

    def __init__(self, url):
        data = requests.get(url).json()
        # Extracting only the rates from the json data
        self.rates = data["rates"]

    def convert(self, from_currency, to_currency, amount):
        self.data = requests.get(url).json()
        self.currencies = self.data['rates']
        initial_amount = amount
        # first convert it into USD if it is not in USD.
        # because our base currency is USD

        # if from_currency != 'USD':
        amount = amount / self.currencies[from_currency]
        # limiting the precision to 4 decimal places

        amount = round(amount * self.currencies[to_currency], 4)
        print('{} {} = {} {}'.format(initial_amount, from_currency, amount, to_currency))


if __name__ == '__main__':
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    objcc = Currencyconverter(url)
    from_country = input("From Country: ")
    to_country = input("TO Country: ")
    amount = int(input("Amount: "))
    objcc.convert(from_country, to_country, amount)
