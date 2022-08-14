import oop_item

print('Input new item')
while True:
    name = input('name: ')
    amount = input('amount: ')
    category = input('category: ')
    ask = input('Do you want input more? (Yes/No) ')
    type_object = oop_item.Warehouse(name, amount, category)
    if ask == "No":
        break
    




