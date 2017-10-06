# 3 types of items have weights of 1, 2 and 3 kg and values of 2$, 5$ and 8$ repectively
# Given a positive number as weight that a bag can carry, how many of ech item do we pick to put in the bag
# so that the total value is largest. Assume that the supply of items are unlimited.

WEIGHT_TO_VALUE ={
    1: 2,
    2: 5,
    3: 8
}

WEIGHT_TO_ZERO = {
    1: 0,
    2: 0,
    3: 0
}

def get_bag_max_value(weight):
    bag_max_value_map = {
        0: (0, WEIGHT_TO_ZERO)
    }
    for i in range(1, weight+1):                 
        max_value = 0
        weight_to_value = WEIGHT_TO_ZERO.copy()
        for w in WEIGHT_TO_VALUE:
            if w <= i:
                bag_max_value = bag_max_value_map[i-w]
                val = WEIGHT_TO_VALUE[w] + bag_max_value[0]
                if val > max_value:
                    weight_to_value = dict(bag_max_value[1])
                    weight_to_value.update({
                        w: weight_to_value[w] + 1
                    })
                    max_value = val
        bag_max_value_map.update({
            i: (max_value, weight_to_value)
        })

    return bag_max_value_map[weight]

if __name__ == '__main__':
    bag_max_value = get_bag_max_value(98)
    print(bag_max_value[0], bag_max_value[1])


