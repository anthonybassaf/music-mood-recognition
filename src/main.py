#=============================   Import Dependencies  =========================================#
from fastapi import FastAPI
import pandas as pd
import uvicorn
from pydantic import BaseModel, validator
import numpy as np
from io import BytesIO
import datetime
from song_name_emotion import get_bert_model
from tensorflow.train import latest_checkpoint
from database import write_to_all_songs
from predict import get_song_bert_predictions

#================================= Validating File  ============================================#
class Data(BaseModel):
    text: str

#================================= Declaring FASTAPI  ============================================#
# FastApi declaration
app = FastAPI(title='Emotional Recommender', version='1.0',
              description='BERT Models are used to predict the emotion from song lyrics')

#================================= Load Model and it's weights ==========================================+#
song_bert = get_bert_model()
lyrics_bert = song_bert

latest = latest_checkpoint('./../models/song_bert_training_weights/')
lyrics_latest = latest_checkpoint('./../models/lyrics_bert_training_weights/')

if latest != None:
    song_bert.load_weights(latest)

if lyrics_latest != None:
    lyrics_bert.load_weights(lyrics_latest)

#================================= File Prediction ==========================================+#
@app.post("/lyrics")
def user_lyrics(lyrics: Data):
    input = lyrics.dict()
    mood = get_song_bert_predictions(lyrics_bert, input)
    return {"mood": mood}

@app.post("/title_artist")
def user_artist_title(title_artist: Data):
    input = title_artist.dict()
    mood = get_song_bert_predictions(song_bert, input)
    return {"mood": mood}

if __name__ == '__main__':
    songs = pd.read_csv("./../dataset/lyrics_1.csv")
    write_to_all_songs(songs)

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
