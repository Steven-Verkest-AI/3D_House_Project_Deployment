# make a dataframe from the tiles

import rasterio
import numpy as np
import pandas as pd

path = "D:\\PROJECT_BECODE\\DSM_split\\tile_12040.tif"
dataset = rasterio.open(path)

band1 = dataset.read(1)
#print(band1)
#df = pd.DataFrame({'Column1':band1[:0],'Column2':band1[:,1],})
df = pd.DataFrame(band1)
#print(df)

##############################################################################################################
# make a csv file from the dataframe so you can put it into SQLlite

df.to_csv('D:\\PROJECT_BECODE\\DSM_CSV\\csv_tile_12040.csv')

##############################################################################################################
# put csv files into SQLlite -> https://medium.com/analytics-vidhya/writing-multiple-csv-files-to-sql-databases-using-sqlalchemy-1f3b85af56d6  & https://www.youtube.com/watch?v=VSzNYfDQp8Y
'''
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


class finalTable(Base): #TODO this is the architectuer of the table with the tiff-files -> needs 10 columns
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
        '''

##############################################################################################################

# find out how i can acces the database with sqlalchemy? ->

#was trying things out in the connecto_to_DB.py file


##############################################################################################################
# convert dataframe back to geotiff -> https://stackoverflow.com/questions/55644662/convert-a-pandas-dataframe-to-geotiff-image

#did not finish this step because we skipped some things the last day