###
# Given a list of product pair which belongs to the same category like (2, 3), (4, 1), (3, 5),
# (1, 7), (6, 8), return the number of different product category and list each products in each 
# category
###

# Initilize the list of product category (as a list of product set) called categories as an empty list
# Iterate over the list of product pair
# For each product pair, look at each of the product ID
# Check if product ID is already in one of categories array item
# If yes, join product category list from both products
# Otherwise create a new set of product category, add both product to it then add the set to the categories list 
# Finally, return the categories list size as the number of category
# Iterate over the categories list and print out each element in the set as product in the category
# Time complexity is O(n*n) where n = number of product pairs

# Given a list of categories (stored as sets)
# find the index of the correct set for the category if any
# if not found, return -1
def find_product_category(product, categories):
    for index, category in enumerate(categories):
        if product in category:
            return index
    return -1

# print out the list of category's products
def print_category_list(categories):
    for index, category in enumerate(categories):
        print('Category ' + str(index) + ': ' + str(category))

# Given a list of product pair which are the same category
# Return the list of categories
def categorize(product_pairs):
    # initialize an empty list of categories
    categories = [];

    # iterate over the product pairs
    for pair in product_pairs:
        cat1 = find_product_category(pair[0], categories)
        cat2 = find_product_category(pair[1], categories)

        if cat1 >= 0:
            if cat2 >= 0:
                categories[cat1].update(categories[cat2])
                del categories[cat2]
            else:
                categories[cat1].add(pair[1])
        else:
            if cat2 >= 0:
                categories[cat2].add(pair[0])
            else:
                categories.append(set(pair))

    return categories
    
if __name__ == "__main__":
    product_pairs = [(2, 3), (4, 1), (3, 5), (5, 6)]
    categories = categorize(product_pairs);
    print(f'Number of categories: {len(categories)}')
    print_category_list(categories)

