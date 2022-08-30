from connect_db import engine, WareHouse, Session
from sqlalchemy.orm import sessionmaker
# from api import WareHouse_DB, input_item

session_db = Session(bind=engine)


print('Input new item')
while True:
    ID_item = input('Stuff ID: ')
    NameOfItem = input('Name of item: ')
    Amount = int(input('Amount: '))
    Category = input('Catergory of item:')
    ask = input('Do you want input more? (Y/N) ')
    insert_new_item = WareHouse(ID_item, NameOfItem, Amount, Category)
    if ask == "N":
        break

# def input_item_DB(ID_item, NameOfItem, Amount, Category):
#     insert_new_item = WareHouse(ID_item, NameOfItem, Amount, Category)
#     return insert_new_item

# result = input_item_DB(WareHouse_DB.StuffID, WareHouse_DB.NameOfItem, WareHouse_DB.Amount, WareHouse_DB.Category)
# result = input_item

session_db.add(insert_new_item)
session_db.commit()
session_db.close()

