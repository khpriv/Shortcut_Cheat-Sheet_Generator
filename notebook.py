"""
TO DO:
- api call to get stock price
- data structure to store in file:
    - name of stock
    - initial price
    - initial timestamp
    - current price
    - store historic price (or receive it)
- total the value of single stock
- introduce portfolio of stocks
- total the value of all/select stocks
- plot of price of stock or whole portfolio
- gui
"""

from datetime import datetime


class Stock:
    def __init__(self, index):
        if not index:
            raise ValueError('Unknown index')
        self._index = index
        self._timestamp = datetime.timestamp(datetime.now())
        self._price_bought = provide_price(index)

    def __str__(self):
        return 'Dont do this'

    @property
    def timestamp(self):
        return self._timestamp

    @property
    def price_bought(self):
        return self._price_bought

    def provide_price(self, index):
        ...

