from connect_db import WareHouse, Session
from sqlalchemy import delete
from item_orm import engine

session_db = Session(bind=engine)

print('Input id of item to delete: ')
while True:
    stuffID_input = input('Stuff ID: ')
    delete_item_by_id = session_db.query(WareHouse).filter(WareHouse.StuffID==stuffID_input).first()
    ask = input('Do you want input more? (Y/N) ')
    if ask == "N":
        break

session_db.delete(delete_item_by_id)
session_db.commit()
