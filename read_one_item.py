import connect_db
from connect_db import WareHouse
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=connect_db.engine)
session_db = Session()

stuffID_input = input('Input ID: ')
update_item = session_db.query(WareHouse).filter(WareHouse.StuffID==stuffID_input).first()

print('Name of item: ' + update_item.NameOfItem + '\n' + 'Amount of item: ' + str(update_item.Amount) + '\n' 
      + 'Category of item: ' + update_item.Category )
