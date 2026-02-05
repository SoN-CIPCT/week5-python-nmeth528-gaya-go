# List Exercise
# Create a list that contains 6 items.
fruits = ["apple", "banana", "grape", "pear", "strawberry", "orange" ]
# Print the items in the list to the output console.
print(fruits)
# Print the first two items in the list using a slice.
first_two = fruits[0:2]
print("The first two items in the list are: "+first_two[0]+", "+first_two[1])
# Print the middle two items in the list using a slice.
middle_two = fruits[2:4]
print("The middle two items in the list are: "+middle_two[0]+", "+middle_two[1])
#print the first and last items in the list using indexes.
print("The first and last items in the list are: "+fruits[0]+", "+fruits[5])

# Tuple Exercise
# Create a tuple with five foods.
menu = ("salad", "soup", "steak", "pasta", "risotto")
# Print each item on the menu using a for loop.
print("Menu:")
for food in menu:
    print(food)
# Copy the tuple replacing two of the foods on the menu.
revised_menu = ("salad", "soup", "calamari", "pizza", "risotto")
# Print each item on the revised menu using a loop.
print("Revised Menu:")
for food in revised_menu:
    print(food)
