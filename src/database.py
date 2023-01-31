import pandas as pd 
from sqlalchemy import create_engine

########################################################
# database config
########################################################
# set up your database url
DATABASE_URL = 'postgresql://postgres:password@localhost:5430/music-db'

engine = create_engine(DATABASE_URL)


#######  WRITE DATA TO DATABASE   ############
def write_to_all_songs(df):
    df.to_sql('artist_table', engine, if_exists='append', index=False)
    return

def write_to_recommendations(df):
    df.to_sql('recommendation_table', engine, if_exists='append', index=False)
    return

########  FETCH  FROM DATABASE    ############
def get_from_database(keyword)-> pd.DataFrame:
    search = pd.read_sql('artist_table', engine)
    return 