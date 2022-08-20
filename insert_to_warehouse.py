import connect_db
from sqlalchemy.orm import sessionmaker

print('Input new item')
while True:
    StuffID = input('Stuff ID: ')
    NameOfItem = input('Name of item: ')
    Amount = input('Amount: ')
    Category = input('Catergory of item:')
    ask = input('Do you want input more? (Yes/No) ')
    insert_new_item = connect_db.WareHouse(StuffID, NameOfItem, Amount, Category)
    if ask == "No":
        break

Session = sessionmaker(bind=connect_db.engine)
session = Session()

session.add(insert_new_item)
session.commit()
session.close()