import connect_db
from connect_db import WareHouse
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=connect_db.engine)
session_db = Session()

# Query all data of WareHouse
all_item = session_db.query(WareHouse).all()
for row in all_item:
    print('Item_ID:', row.StuffID,',Name of Item:', row.NameOfItem, ',Amount of item:', row.Amount,
          ',Category of item:', row.Category)