import pyodbc 
import pandas as pd

connnect_db = pyodbc.connect("Driver={SQL Server};"
                      "Server=localhost,1433;"
                      "Database=naruto;"
                      "UID=sa;"
                      "PWD=Baoloc@1;")

cursor = connnect_db.cursor()
cursor.execute('SELECT * FROM Warehouse')

for i in cursor:
    print(i)

# data = pd.read_sql("SELECT * FROM warehouse", cnxn)
# print(type(data))



# ---------------------------------------------


# import urllib

# from sqlalchemy import create_engine, Table, MetaData, Column, Integer
# from sqlalchemy import text
# from sqlalchemy.ext.declarative import declarative_base
# from datetime import datetime

# server = 'localhost,1433' # to specify an alternate port
# database = 'naruto'
# username = 'sa'
# password = 'Baoloc@1'

# params = urllib.parse.quote_plus("'DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password")

# engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)




# Base = declarative_base()

# # Base.metadata.create_all(engine)

# class WareHouse(Base):
#     __tablename__ = 'Warehouse1'

#     id = Column(Integer(), primary_key=True)
#     name = Column(str())
#     amount = Column(Integer())
#     category = Column(str())
    

# # Base.metadata.create_all(engine)



    

    
# # # print(str(params))
# # # m = MetaData()
# # # t = Table('t', m,
# # #         Column('id', Integer, primary_key=True),
# # #         Column('x', Integer))
# # # m.create_all(engine)
# # # print(str(params))