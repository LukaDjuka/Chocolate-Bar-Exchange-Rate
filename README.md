# Chocolate Bar Exchange Rate

This is a program which uses an Exchange Rate API from exchangerate-api.com to get provide the user
with the up-to-date exchange rate info for all currencies supplied by the website.

This program uses Tkinter to present the user with a simple GUI used for inputting the amount of currency to be exchanged.
The program also provides the user with the option to show approximately how many Chocolate Bars can be purchased with the 
exchanged currency (in countries where the selected currency is commonly used).

Information about the pricing of chocolate bars in various countries was found using estimations based on the "cost of living" 
statistics supplied by [numbeo](https://www.numbeo.com/cost-of-living/).

## API NOTE
To use the program you need to sign-up for an account on the exchangerate-api.com website and
you will be provided with an API key. 
The key is then substituted into the string urls on lines 59 and 85 of the code.
The key which is currently found in this module is associated with a temporary email and is working as of June 21st, 2020.


By: Luka Djukic
