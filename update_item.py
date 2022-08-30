from connect_db import WareHouse, engine, Session
from sqlalchemy.orm import sessionmaker

session_db = Session(bind=engine)

print('Input ID of item to update ')
while True:
    stuffID_input = input('Stuff ID: ')
    update_item = session_db.query(WareHouse).filter(WareHouse.StuffID==stuffID_input).first()
    print('Pls update new Item: ')
    name_update = input('Input new Name: ')
    amount_update = input('Input new Amount: ')
    category_update = input('Input new Category: ')
    update_item.NameOfItem = name_update
    update_item.Amount = amount_update
    update_item.NameOfItem = name_update
    ask = input('Do you want input more? (Y/N) ')
    if ask == "N":
        break

session_db.commit()
print(update_item.Amount)


