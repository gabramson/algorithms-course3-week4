import numpy as np

class KnapsackPacker:
    def __init__(self, max_weight, items_count):
        self.max_weight = max_weight
        self.max_item = 0
        self.items_count = items_count
        self.items = np.empty([items_count, 2])

    def add_item(self, weight, value):
        self.items[self.max_item][0] = weight
        self.items[self.max_item][1] = value
        self.max_item += 1

    def get_max_value(self):
        last_values = np.zeros(self.max_weight+1)
        next_values = np.empty(self.max_weight+1)
        for i in range(0, self.items_count):
            if i%100 == 0:
                print(i)
            w = int(self.items[i][0])
            v = int(self.items[i][1])
            for x in range(0, self.max_weight+1):
                if w > x:
                    next_values[x] = last_values[x]
                    continue
                next_values[x] = self.get_maximum(last_values[x], last_values[x-w]+v)
            last_values = np.copy(next_values)
        return next_values[self.max_weight]

    def get_maximum(self, a, b):
        return a if a > b else b
