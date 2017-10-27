#!/usr/bin/env python3
"""
Module Docstring
"""
import KnapsackPacker


__author__ = "Your Name"
__version__ = "0.1.0"
__license__ = "MIT"


def main():
    """ Main entry point of the app """
    myfile = open("knapsack_big.txt", "r")
    parameters = myfile.readline().split()
    knapsack_packer = KnapsackPacker.KnapsackPacker(int(parameters[0]), int(parameters[1]))
    for line in myfile:
        item = line.split()
        knapsack_packer.add_item(int(item[1]), int(item[0]))
    print(knapsack_packer.get_max_value())

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
