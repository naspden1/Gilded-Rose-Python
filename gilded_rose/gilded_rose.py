class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def decrease_quality_based_on_quality_limit(self, item_quality, quality_limit, dec_amount=1):
        dec = 0
        if item_quality > quality_limit:
            dec = dec_amount
        return dec

    def decrease_quality_based_on_quality_and_sell_in_limits(self, item_quality, quality_limit, item_sell_in, sell_in_limit,dec_amount=1):
        dec = 0
        if item_sell_in < sell_in_limit and item_quality > quality_limit:
            dec = dec_amount
        return dec

    def increase_quality_based_on_quality_limit(self, item_quality, quality_limit):
        inc = 0
        if item_quality < quality_limit:
            inc = 1
        return inc

    def increase_quality_based_on_quality_and_sell_in_limits(self, item_quality, quality_limit, item_sell_in, sell_in_limit):
        inc = 0
        if item_sell_in < sell_in_limit and item_quality < quality_limit:
            inc = 1
        return inc

    def update_quality(self):
        for item in self.items:
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in -= 1

            if item.name == "Aged Brie":
                item.quality += self.increase_quality_based_on_quality_limit(item.quality, 50)
                item.quality += self.increase_quality_based_on_quality_and_sell_in_limits(item.quality, 50, item.sell_in, 0)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                 if item.sell_in < 0:
                     item.quality = 0
                 else:
                    item.quality += self.increase_quality_based_on_quality_limit(item.quality, 50)
                    item.quality += self.increase_quality_based_on_quality_and_sell_in_limits(item.quality, 50, item.sell_in, 10)
                    item.quality += self.increase_quality_based_on_quality_and_sell_in_limits(item.quality, 50, item.sell_in, 5)
            elif item.name == "Conjured Mana Cake":
                item.quality -= self.decrease_quality_based_on_quality_limit(item.quality, 0, dec_amount=2)
                if item.quality < 0: 
                    item.quality = 0
                item.quality -= self.decrease_quality_based_on_quality_and_sell_in_limits(item.quality, 0, item.sell_in, 0, dec_amount=2)
                if item.quality < 0: 
                    item.quality = 0                    
            elif item.name != "Sulfuras, Hand of Ragnaros":
                item.quality -= self.decrease_quality_based_on_quality_limit(item.quality, 0)
                item.quality -= self.decrease_quality_based_on_quality_and_sell_in_limits(item.quality, 0, item.sell_in, 0)
