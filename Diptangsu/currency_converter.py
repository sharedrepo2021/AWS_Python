from forex_python.converter import CurrencyRates
c = CurrencyRates()
Currency = c.get_rate(input('Enter from currency: '), input('Enter to currency: '))
amount = float(input('Enter the amount to be converted: '))
converted_currency = amount * Currency

print(converted_currency)