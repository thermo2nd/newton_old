from newton.trade.tools import last_price
from newton.rules.entry.base import Entry


class SellHigherEntry(Entry):
    def __init__(self, currency_pair, amount, sell_price, name=None):
        super().__init__(currency_pair=currency_pair, amount=amount, action='ask', name=name)
        self.sell_price = sell_price

    def can_entry(self):
        return last_price(self.currency_pair) > self.sell_price
