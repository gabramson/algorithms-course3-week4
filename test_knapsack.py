import KnapsackPacker

def test_knapsack():
    knapsack_packer = KnapsackPacker.KnapsackPacker(20, 5)
    knapsack_packer.add_item(2,3)
    knapsack_packer.add_item(3,4)
    knapsack_packer.add_item(4,5)
    knapsack_packer.add_item(5,8)
    knapsack_packer.add_item(9,10)
    assert 26 == knapsack_packer.get_max_value()
