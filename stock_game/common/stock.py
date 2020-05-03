"""
Stock class
"""


class Stock:

    def __init__(self, init_price):
        self.price = init_price
        self.next_price = self.price

    def prince_change_of_time(self):
        """
        Changes the stock's **current** price during the round-end period
        """
        pass

    def price_change_of_trading(self):
        """
        Changes its **next-round** price during the round
        """
        pass
