import connect_db
from sqlalchemy.orm import sessionmaker

print('Input new item')
while True:
    ID_item = input('Stuff ID: ')
    NameOfItem = input('Name of item: ')
    Amount = int(input('Amount: '))
    Category = input('Catergory of item:')
    ask = input('Do you want input more? (Y/N) ')
    insert_new_item = connect_db.WareHouse(ID_item, NameOfItem, Amount, Category)
    if ask == "N":
        break

Session = sessionmaker(bind=connect_db.engine)
session_db = Session()
session_db.add(insert_new_item)
session_db.commit()
session_db.close()