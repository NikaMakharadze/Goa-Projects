import os

usd =  0.36
eu = 0.34
gel = 1.0

currency_options = {
    "usd": usd,
    "eu": eu,
    "gel": gel
}

# Welcome Message 
print("Welcome To Currency Converter PY")

# While loop for currency input if user choose other currency then EU, GEL, USD.
print("Options: \nEU, USD, GEL")
while True:
    currency = input("Enter your Currency: ").lower()
    if currency in currency_options:
        break
    else:
        print("Invalid currency. Please enter one of the following: EU, USD, GEL.")

# Clear the terminal screen after a valid input
os.system('cls' if os.name == 'nt' else 'clear')

print(f"You selected {currency.upper()}.")

# while loop if user input other data type then float
while True:
    try:
        gel = float(input("Enter your GEL: "))
        break
    except ValueError:
        print("Please enter a valid amount of GEL.")

# Convert GEL to the selected currency
if currency == "usd":
    # Correct formula: GEL to USD
    converted_value = gel * usd
    print(f"{gel} GEL is equal to {converted_value:.2f} USD.")
elif currency == "eu":
    # Correct formula: GEL to EUR
    converted_value = gel * eu
    print(f"{gel} GEL is equal to {converted_value:.2f} EUR.")
else:
    # If GEL is selected, output GEL value
    print(f"{gel} GEL is equal to {gel} GEL.") 
