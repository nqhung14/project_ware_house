from connect_db import WareHouse, engine, Session
from sqlalchemy.orm import sessionmaker

session_db = Session(bind=engine)

# Query all data of WareHouse
all_item = session_db.query(WareHouse).all()
for row in all_item:
    print('Item_ID:', row.StuffID,',Name of Item:', row.NameOfItem, ',Amount of item:', row.Amount,
          ',Category of item:', row.Category)