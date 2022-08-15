import connect_db
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=connect_db.engine)
session = Session()

StuffID = 'CV00002'
NameOfItem = 'Co ve dau to 1.0mm'
Amount = 3
Category = 'Co ve'

insert_new_item = connect_db.WareHouse(StuffID, NameOfItem, Amount, Category)
session.add(insert_new_item)

session.commit()
session.close()