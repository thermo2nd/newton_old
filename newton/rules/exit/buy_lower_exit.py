from newton.trade.tools import last_price
from newton.rules.exit.base import Exit


class BuyLowerExit(Exit):
    def __init__(self, exit_price, name=None):
        super().__init__(name=name)
        self.exit_price = exit_price

    def can_exit(self, trade):
        return self.exit_price > last_price(trade.currency_pair)
