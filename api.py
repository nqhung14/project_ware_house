from ast import Delete
from asyncio.windows_events import NULL
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from connect_db import Session, engine, WareHouse


app=FastAPI()

session_db = Session(bind=engine)

class WareHouse_DB(BaseModel):
    StuffID_DB:str
    NameOfItem_DB: str
    Amount_DB: int
    Category_DB: str
          
@app.get('/')
def index():
    return{"message:":"Hello world"}

@app.get('/get-item/{item_id}')
def read_item(item_id: str):
    read_item_db = session_db.query(WareHouse).filter(WareHouse.StuffID==item_id).first()
    return read_item_db

@app.get('/get-all-item')
def get_all_items():
    items=session_db.query(WareHouse).all()
    return items

@app.put('/update-item/{item_id}')
def update_item_DB(item:WareHouse_DB, item_id:str):
    update_item = session_db.query(WareHouse).filter(WareHouse.StuffID==item_id).first()
    # Update value of item
    update_item.NameOfItem = item.NameOfItem_DB
    update_item.Amount = item.Amount_DB
    update_item.Category = item.Category_DB
    
    session_db.commit()
    return update_item

@app.post('/create-item')
def create_new_item(item: WareHouse_DB):
    
    query_db = session_db.query(WareHouse).filter(WareHouse.StuffID==item.StuffID_DB).first()
    
    if query_db is not None:
         raise HTTPException(status_code=400,detail="Item already exists")
     
    create_item = WareHouse(item.StuffID_DB,item.NameOfItem_DB,
                            item.Amount_DB, item.Category_DB)
    session_db.add(create_item)
    session_db.commit()
    return create_item

@app.delete('/delete-item/{item_id}')
def delete_item(item_id):
    query_db = session_db.query(WareHouse).filter(WareHouse.StuffID==item_id).first()
    
    if query_db is None:
         raise HTTPException(status_code=400,detail="Item not exists")
    
    session_db.delete(query_db)
    session_db.commit
    return query_db
    
    
    



