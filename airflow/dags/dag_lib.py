import neattext as nt
import pandas as pd
import requests
import json

def clean_text(text):
    docx = nt.TextFrame(text)
    song = docx.remove_stopwords().text
    song = docx.remove_puncts().text
    song = docx.remove_special_characters().text
    return song

def call_song_bert_api(song):
    song = clean_text(song)
    response = requests.post("http://172.20.224.1:8000/title_artist", json={"text": song})
    response = json.loads(response.text)
    return response['mood']

def call_lyrics_bert_api(lyrics):
    song = clean_text(lyrics)
    response = requests.post("http://172.20.224.1:8000/lyrics", json={"text": song})
    response = json.loads(response.text)
    return response['mood']
