#=============================   Import Dependencies  =========================================#
from fastapi import FastAPI
import pandas as pd
import uvicorn
from pydantic import BaseModel, validator
import numpy as np
from io import BytesIO
import datetime

from database import write_to_all_songs


class Test(BaseModel):
    text: str

class Search(BaseModel):
    artist_name: str


# # ===================================Declaring FASTAPI============================================
# FastApi declaration
app = FastAPI(title='Emotional Recommender', version='1.0',
              description='BERT Models are used to predict the emotion from song lyrics')


# ===================================Validating File ============================================
class Artist(BaseModel):
    artist_name: str
    song_name: str
    
    @validator('*')
    def is_String(cls, v):
        if type(v) == int:
            raise ValueError('value must be a string')
        return v

class Lyrics(BaseModel):
    lyrics: str

    @validator('*')
    def is_String(cls, v):
        if type(v) == int:
            raise ValueError('value must be a string')
        return v

# # ===================================File Prediction============================================

def user_predict(data):
    # pred_val = model.make_predict(data)
    return text # Return pred_val

# # ===================================USER PREDICTION END POINT FASTAPI============================================
@app.post("/song_input")
def artist_recommendation(user_input: Artist):
    data_dict = user_input.dict()
    # Converting to dictionary and to dataframe
    df = pd.DataFrame.from_dict([data_dict])  # type: ignore
    result = predict(df)
    df["mood"] = result1
    df['timestamp'] = datetime.datetime.now()
    df['recommendation_id'] = uuid.uuid1()
    print(df)
    write_to_database(df)
    return {"result": df["mood"]}

@app.post("/lyrics")
def artist_predict(user_input: Lyrics):
    data_dict = user_input.dict()
    # Converting to dictionary and to dataframe
    df = pd.DataFrame.from_dict([data_dict])  # type: ignore
    result = predict(df)
    df["emotion"] = result
    df['timestamp'] = datetime.datetime.now()
    df['id'] = uuid.uuid1()
    print(df)
    write_to_database(df)
    return {"result": df["emotion"]}

#  ===================================SEARCH END-POINT FASTAPI============================================
@app.post("/artist_name_search")
def search(search: Search):
    kword = search.artist_name
    # get the query result from database with the keyword sending from streamlit app
    db_fetch = get_from_database(kword)
    byteData = db_fetch.to_csv(index=False, encoding='utf-8').encode()
    return {"result": byteData}


if __name__ == '__main__':
    songs = pd.read_csv("dataset/lyrics_1.csv")
    write_to_all_songs(songs)
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
