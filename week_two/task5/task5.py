#  Task5: Modify Tuple Indirectly
shopping_list = (
    input("Enter the first item: "),
    input("Enter the second item: "),
    input("Enter the third item: ")
)
conv_shopping_list = list(shopping_list)
conv_shopping_list.append(input("Enter one more item: "))
conv_shopping_list.append(input("Enter another item: "))
updated_shopping_list = tuple(conv_shopping_list)
print('|'.join(updated_shopping_list))

