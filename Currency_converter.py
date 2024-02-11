CURRENCIES = {
    'USD': 1,
    'EUR': 1.06,
    'YEN': 0.0067,
    'GBP': 1.23,
    'AUD': 0.64,
    'CAD': 0.74
}

def to_usd(currency, amount):
    if currency not in CURRENCIES:
        raise Exception(currency + " is not supported")
    if amount < 0:
        raise Exception("Invalid amount")
    x = CURRENCIES[currency]
    usd_value = amount * x
    return usd_value

def from_usd(currency, amount):
    if currency not in CURRENCIES:
        raise Exception(currency + " is not supported")
    if amount < 0:
        raise Exception("Invalid amount")
    cur = CURRENCIES[currency]
    temp_val = amount / cur
    new_val = round(temp_val, 4)
    return new_val

def convert():
    try:
        from_currency = input("Enter the currency you want to convert from this list:USD,EUR,YEN,GBP,AUD,CAD:").upper()
        amount = float(input("Enter the amount of money you wish to convert:$"))
        to_currency = input("Enter the currency you want to convert to from this list:USD,EUR,YEN,GBP,AUD,CAD:").upper()

        usd_value = to_usd(from_currency, amount)
        converted_value = from_usd(to_currency, usd_value)
        print(str(amount) + " " + from_currency + " is " + str(converted_value) + " " + to_currency)

         
    
    except Exception as e:
        print(e)

convert()