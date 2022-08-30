import urllib
from sqlalchemy import create_engine, Table, MetaData, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

server = 'localhost,1433' # to specify an alternate port
database = 'naruto'
username = 'sa'
password = 'Baoloc@1'

params = urllib.parse.quote_plus("DRIVER={ODBC Driver 17 for SQL Server};UID=sa;PWD=Baoloc@1;TrustServerCertificate=No;DATABASE=naruto;WSID=LAP00317;APP={Microsoft® Windows® Operating System};Trusted_Connection=No;SERVER=localhost;Description={my source}")
engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)
Session = sessionmaker()

Base = declarative_base()
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

    


