from connect_db import WareHouse, engine, Session
from sqlalchemy.orm import sessionmaker

session_db = Session(bind=engine)

def read_item_DB(stuffID): 
# stuffID_input = input('Input ID: ')
    update_item = session_db.query(WareHouse).filter(WareHouse.StuffID==stuffID).first()
    return update_item

print(read_item_DB('CV0012').NameOfItem)

# print('Name of item: ' + update_item.NameOfItem + '\n' + 'Amount of item: ' + str(update_item.Amount) + '\n' 
#       + 'Category of item: ' + update_item.Category )
