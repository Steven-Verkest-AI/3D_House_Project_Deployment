# find out how i can acces the database with sqlalchemy? -> https://medium.com/analytics-vidhya/writing-multiple-csv-files-to-sql-databases-using-sqlalchemy-1f3b85af56d6  & https://www.youtube.com/watch?v=VSzNYfDQp8Y

import pyodbc
import pandas as pd
import sqlalchemy as db
import urllib
params = 'Driver={ODBC Driver 17 for SQL Server;}' \
    'Server=Servername;' \
    'Database=Database name' \
    'UID=User'\
    'PWD=Password;'

params =urllib.parse.quote_plus(params)
engine = db.create_engine("mssql+pyodbc:///?odbc_connect={}".format(params))
connection = engine.connect()

'''
Once the connection is made, you can define the folder where all your CSV files are kept and
all the filenames can be stored in a list variable.
Just make sure these files have same number and names of columns so that they can be written as a 
single table to SQL Database'''

import os
import glob
import chardet
os.chdir('D:\PROJECT_BECODE\DSM_CSV')
extension = 'tif'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

from sqlalchemy.orm import mapper
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

metadata = db.MetaData()
session = sessionmaker()
session.configure(bind=engine)
my_session = session()
Base = declarative_base()

'''You can first create a table in SQL Database (using SQL query),
make sure it has same number of columns and column names as CSV files, plus you can 
add a DataSource column to write the filename so that you know the datasource file 
while querying the data)'''

class finalTable(Base):
    __tablename__ = 'Users'
    CustomerID = db.Column(db.String(255),primary_key = True)
    Customer = db.Column(db.String(255))
    Phone = db.Column(db.String(255))
    # etc

for i in range(len(all_filenames)):
    with open(all_filenames[i],'rb') as f:
        result =chardet.detect(f.read())
        df = pd.read_csv(all_filenames[i],encoding = result['encoding'])
        df.to_sql('Users',con=engine,index=False,if_exists='append')
        query = db.update(finalTable).where(finalTable.DataSource ==None).values(Datasource=all_filenames[i])
        connection.execute(query)



