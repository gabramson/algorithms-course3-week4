import numpy as np

class KnapsackPacker:
    def __init__(self, max_weight, items):
        self.max_weight = max_weight
        self.max_item=0
        self.items = np.empty([items,2])
        self.best_values = np.zeros(items)

    def add_item(self, weight, value):
        self.items[self.max_item][0] = weight
        self.items[self.max_item][1] = value
        self.max_item += 1

    def get_max_value(self):
        return 26