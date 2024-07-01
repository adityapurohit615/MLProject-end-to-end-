# ye file generic functionality ke liye use hoti hai like reading a
# data base and other things and for the time being we will be using it
# for reading a database

import os
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv # ye load kardega saara enviornment vaiables
import pymysql # this will be responsible to connect with the db

load_dotenv()
host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
db = os.getenv("db")
port = os.getenv("port")

def read_sql_data():
    # there are multiple libraries that can be used to read the data
    # from a mysql database. we will be using 2 libraries
    # 1. mysql-connector-python
    # 2. pymysql
    # also we will be needing the information to access the data base like host, user, password, database
    # and all this information is stored in our .env file because it is sensitive information and we can
    # access this information using another library called "python-dotenv"

    logging.info("Reading Sql data base started")
    try:
        # mydb = pymysql.connect(
        #     host = host,
        #     user = user,
        #     password = password,
        #     db = db
        # )

        logging.info("Connection Established")
        engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{db}")
        df = pd.read_sql("Select * from main",engine)
        print(df.head())

        return df


    except Exception as ex:
        raise CustomException(ex,sys)









