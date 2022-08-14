import connect_db
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=connect_db.engine)
session = Session()

# id = 'CV00002'
name = 'Co ve dau to 1.0mm'
amount = 3
category = 'Co ve'

insert_new_item = connect_db.WareHouse( name, amount, category)
session.add(insert_new_item)

session.commit()