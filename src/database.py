import pandas as pd 
from sqlalchemy import create_engine

########################################################
# database config
########################################################
# set up your database url
DATABASE_URL = 'postgresql://dsp:12345678@localhost:5432/music-db'

engine = create_engine(DATABASE_URL)


#=====================  WRITE DATA TO DATABASE     ===============================#
def write_to_all_songs(df):
    df.to_sql('artist_table', engine, if_exists='replace', index=False)
    return

def write_to_recommendations(df):
    df.to_sql('artist', engine, if_exists='replace', index=False)
    return

#======================  FETCH  FROM DATABASE      ===================================#
def get_from_all_songs(keyword)-> pd.DataFrame:
    search = pd.read_sql('artist_table', engine)
    search = search[search["Mood"]==keyword]
    return search


def get_from_recommendations()-> pd.DataFrame:
    search = pd.read_sql('artist_table', engine)
    return search