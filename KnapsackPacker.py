import numpy as np

class KnapsackPacker:
    def __init__(self, max_weight, items_count):
        self.max_weight = int(max_weight)
        self.max_item = 0
        self.items_count = int(items_count)
        self.items = np.empty([items_count, 2])
        self.lookup = {}

    def add_item(self, weight, value):
        self.items[self.max_item][0] = int(weight)
        self.items[self.max_item][1] = int(value)
        self.max_item += 1

    def get_max_value(self):
        retval = self.__get_subproblem(self.max_weight, self.items_count)
        return retval

    def __get_subproblem(self, weight, item):
        if item == 0:
            return 0
        if (weight, item) in self.lookup.keys():
            return self.lookup.get((weight, item))
        item_weight = self.items[item-1][0]
        if item == 1 and weight >= item_weight:
            return item_weight
        case1 = self.__get_subproblem(weight, item-1)
        if weight < item_weight:
            best_value = case1
        else:
            item_value = self.items[item-1][1]
            case2 = self.__get_subproblem(weight-int(item_weight), item-1)+item_value
            best_value = self.__get_maximum(case1, case2)
        self.lookup[weight, item] = best_value
        return best_value

    def __get_maximum(self, a, b):
        return a if a > b else b
