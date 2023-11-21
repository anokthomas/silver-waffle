from forex_python.converter import CurrencyRates
def currency_converter(amount,from_converter,to_converter):
    c = CurrencyRates()
    exchange_rate = c.get_rate(from_currency,to_currency)
    convertedamount = amount*exchange_rate
    return convertedamount

print("Welcome to currency converter")
amount = float(input("Enter currency"))
from_currency = input("Enter currency to convert:".upper())
to_currency = input("Enter currency to convert to:".upper())
convertedamount = currency_converter(amount,from_currency,to_currency)
print(convertedamount)
