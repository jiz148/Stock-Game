"""
Players class
"""

INIT_BALANCE = 10000


class Player:

    def __init__(self, world, name, init_balance=None, init_stock_list=None):
        """
        @param world: the world witch the player is in
        @param name: name of the player
        @param init_balance: initial balance of the player
        @param init_stock_list: initial stock list of the player

        stocks in the stock_list should be in the form of Tuple (Stock, quantity)
        """
        self.world = world
        self.name = name
        self.balance = init_balance if init_balance is not None else INIT_BALANCE
        self.stock_list = init_stock_list if init_stock_list is not None else []

    def buy_product(self):
        """
        Buys a product
        """
        pass

    def buy_stock(self):
        """
        Buys a stock
        """
        pass

    def sell_product(self):
        """
        Sells a Product
        """
        pass

    def sell_stock(self):
        """
        Sells a stock
        """
        pass
