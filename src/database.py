import pandas as pd 
from sqlalchemy import create_engine

########################################################
# database config
########################################################
# set up your database url
DATABASE_URL_1 = 'postgresql://postgres:password@localhost:5430/artist-db'
DATABASE_URL_2 = 'postgresql://postgres:password@localhost:5430/lyrics-db'

engine_1 = create_engine(DATABASE_URL_1)
engine_2 = create_engine(DATABASE_URL_2)

#######  WRITE DATA TO DATABASE   ############
def write_to_database(df):
    df.to_sql('artist-db', engine, if_exists='append', index=False)
    return

def write_to_database(df):
    df.to_sql('lyrics-db', engine, if_exists='append', index=False)
    return

########  FETCH  FROM DATABASE    ############
def get_from_database(keyword)-> pd.DataFrame:
    search = pd.read_sql('artist-db', engine)
    return 