"""
    This is a program which uses an Exchange Rate API from exchangerate-api.com to get provide the user
    with the up-to-date exchange rate info for all currencies supplied by the website.
    This program uses Tkinter to present the user with a simple GUI used for inputting the amount of currency to be
    exchanged.
    The program also provides the user with the option to show approximately how many
    Chocolate Bars can be purchased with the exchanged currency.

    API NOTE: To use the program you need to sign-up for an account on the exchangerate-api.com website and
    you will be provided with a key. The key is then substituted into the string urls on lines 59 and 85.
    The key which is currently found in this module is associated with a temporary email.


    By: Luka Djukic
"""

import requests
from tkinter import *
from tkinter import ttk

# Creating the root box
root = Tk()
root.title("Chocolate Bar Converter")
root.geometry("700x400")

# It's advised to place this Frame (mainframe) within the root and then place further widgets inside this frame
# Likely since the ttk module's Frame class is more versatile than basic instance of root()
mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

# Modifying the weight of the columns and rows to ensure that the frame placed within the root expands with resizing
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
# mainframe.rowconfigure(6, weight=1)

# Labels to visually represent where data should be entered
fromLabel = ttk.Label(mainframe, text="Convert:").grid(column=0, row=0, sticky=(W, E))
toLabel = ttk.Label(mainframe, text="To:").grid(column=0, row=3, sticky=(W, E))

# Values which hold the text associated with the amount to convert from and the answer
fromNumber = StringVar()
toNumber = StringVar()

# An Entry box which takes the amount to be exchanged
fromEntry = ttk.Entry(mainframe, width=20, textvariable=fromNumber)
fromEntry.grid(column=0, row=1, sticky=(W, E))


# A Label which provides the exchanged quantity
ttk.Label(mainframe, textvariable=toNumber).grid(column=0, row=4, sticky=(W, E))


"""
    A function which is called when the convert button is pressed on the GUI.
    Converts the amount of money in the provided currency to the requested one (in GUI).
"""
def convert(*args):
    if fromNumber.get() == '':
        print("Please enter an amount")
        return 1
    try:
        value = float(fromNumber.get())     # amount to exchange
        conversion_url = 'https://prime.exchangerate-api.com/v5/82ed7ec526e7714784b8c9ff/latest/' + fromCurrency.get()
        conversion_response = requests.get(conversion_url)
        conversion_data = conversion_response.json()
        new_conversion_dictionary = conversion_data['conversion_rates']

        answer = value * float(new_conversion_dictionary[toCurrency.get()])
        toNumber.set(answer)
        choco_info()

    except ValueError:
        raise("Value Error - Please enter a proper numerical value")
        pass


# The Button to initiate the conversion
ttk.Button(mainframe, text="Convert", command=convert).grid(column=4, row=2, sticky=(W, E))

# Strings variables which hold the values which are selected in the ComboBox. Do this so can use these values as keys
# into a dictionary
fromCurrency = StringVar()
toCurrency = StringVar()


""" Exchange rate api requesting process
    Doing this to get the list of currencies to put into Combobox
"""
url = 'https://prime.exchangerate-api.com/v5/82ed7ec526e7714784b8c9ff/latest/USD'
response = requests.get(url)
data = response.json()

# A variable which is used to get the Currency key codes for the ComboBoxes
conversion_rate_dict = data['conversion_rates']

# The combo boxes for selecting which currencies to convert from and to. Readonly to ensure no user additions
convertFromBox = ttk.Combobox(mainframe, state="readonly", values=list(conversion_rate_dict), textvariable=fromCurrency).grid(column=3, row=1, sticky=(W, E))
convertToBox = ttk.Combobox(mainframe, state="readonly", values=list(conversion_rate_dict), textvariable=toCurrency).grid(column=3, row=4, sticky=(W, E))

# The dictionary which holds the average price of a chocolate bar for each currency. Found through approximations
chocolate_bar_prices = {'USD': 2.00, 'AED': 2.5, 'ARS': 60, 'AUD': 3.5, 'BGN': 1.6, 'BRL': 4.0, 'BSD': 2.0, 'CAD': 2.0, 'CHF': 2.0, 'CLP': 800.0, 'CNY': 3.0, 'COP': 2700.0, 'CZK': 25.0, 'DKK': 20.0, 'DOP': 40.0, 'EGP': 4.5, 'EUR': 1.5, 'FJD': 2.0, 'GBP': 1.5, 'GTQ': 7.5, 'HKD': 7.5, 'HRK': 10.0, 'HUF': 300.0, 'IDR': 5000.0, 'ILS': 6.5, 'INR': 15.0, 'ISK': 1.5, 'JPY': 120.0, 'KRW': 1200.0, 'KZT': 200.0, 'MXN': 10.0, 'MYR': 1.5, 'NOK': 30.0, 'NZD': 3.5, 'PAB': 1.0, 'PEN': 2.0, 'PHP': 25.0, 'PKR': 50.0, 'PLN': 5.0, 'PYG': 3500.0 , 'RON': 5.5, 'RUB': 30.0, 'SAR': 2.0, 'SEK': 20.0, 'SGD': 1.5, 'THB': 15.0, 'TRY': 2.5, 'TWD': 20.0, 'UAH': 13.0, 'UYU': 40.0, 'ZAR': 11.0}

# A label which is created in global scope so that the following 'choco_info()' function is able to configure the text
# and visibility of the provided chocolate bar information (if the user requests to see it)
choco_answer = ttk.Label(mainframe)


"""
    A function which is called when the user presses the Checkbutton on the GUI.
    This function alters the choco_answer label to be visible and provide the user with information about how many
    chocolate bars can be purchased with the amount of exchanged currency - in countries associated with the currency.
"""
def choco_info():
    try:
        num_choco_bars = float(toNumber.get()) / float(chocolate_bar_prices[toCurrency.get()])

        choco_text = "This amount of currency can purchase you: \n" + str(
            num_choco_bars) + "\nChocolate Bars in the countries where the currency is used"
        choco_answer.config(text=choco_text)
        if choco_check.get() == 1:
            choco_answer.grid(column=0, row=6, sticky=(W, E))
        else:
            choco_answer.config(text='')
            choco_answer.grid_remove()
    except ValueError:
        pass


# A variable which is used to check whether the Checkbutton is "On" or "Off"
choco_check = IntVar()

# The CheckButton for the user to select whether they want to see chocolate bar information
choco_button = ttk.Checkbutton(mainframe, text="Chocolate Bar Info", variable=choco_check, command=choco_info)
choco_button.grid(column=3, row=5, sticky=(W, E))


root.mainloop()
