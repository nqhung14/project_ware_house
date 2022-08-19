# import pyodbc 
# import pandas as pd

# connnect_db = pyodbc.connect("Driver={SQL Server};"
#                       "Server=localhost,1433;"
#                       "Database=naruto;"
#                       "UID=sa;"
#                       "PWD=Baoloc@1;")

# cursor = connnect_db.cursor()
# cursor.execute('SELECT * FROM Warehouse')

# for i in cursor:
#     print(i)

# data = pd.read_sql("SELECT * FROM warehouse", cnxn)
# print(type(data))



# ---------------------------------------------

import urllib
from sqlalchemy import create_engine, Table, MetaData, Column, Integer, String, ForeignKey
from sqlalchemy import text
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.orm import sessionmaker

server = 'localhost,1433' # to specify an alternate port
database = 'naruto'
username = 'sa'
password = 'Baoloc@1'

params = urllib.parse.quote_plus("DRIVER={ODBC Driver 17 for SQL Server};UID=sa;PWD=Baoloc@1;TrustServerCertificate=No;DATABASE=naruto;WSID=LAP00317;APP={Microsoft® Windows® Operating System};Trusted_Connection=No;SERVER=localhost;Description={my source}")

engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)
# engine = create_engine("mysql+mysqlconnector://sa:aaaa@localhost:1433/naruto")

# query DB
# connection = engine.connect()
# curser = connection.execute("Select * from Warehouse;")

# with engine.connect() as connection:
#     result = connection.execute(text("select * from Warehouse"))
#     for row in result:
#         print(row['StuffID'])
#         print(row['NameOfItem'])

Base = declarative_base()

# Base.metadata.create_all(engine)

class WareHouse(Base):
    __tablename__ = 'Warehouse'
    StuffID = Column(String(255), primary_key=True)
    NameOfItem = Column(String(255))
    Amount = Column(Integer())
    Category = Column(String(255))
    
    def __init__(self, StuffID, NameOfItem, Amount, Category):
        self.StuffID = StuffID
        self.NameOfItem = NameOfItem
        self.Amount = Amount
        self.Category = Category
        
# Session = sessionmaker(bind=engine)
# session = Session()

# item1 = WareHouse(StuffID='CV0002', NameOfItem='CoVe2', Amount=3, Category='Cove')
# session.add(item1)
# session.commit()

    


