import requests
import json
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import neattext as nt
import pandas as pd
#import gensim
import en_core_web_sm

nlp = en_core_web_sm.load()
# import tensorflow_hub as hub
#import tensorflow as tf
#import tensorflow_text



#================================ CLEAN TEXT ============================#
def clean_text(text):
    docx = nt.TextFrame(text)
    song = docx.remove_stopwords().text
    song = docx.remove_puncts().text
    song = docx.remove_special_characters().text

    return song

#================================ PREDICT MODEL ============================#
def recommend(text)-> pd.DataFrame:
    song = clean_text(text)
    response = requests.post("http://127.0.0.1:8000/text", json={"text": song})
    response = json.loads(response.text)
    result = query_db(response)
    return result


tracklist = []

#================================ TOP TEN SONGS ===============================#
songs = pd.read_csv("C:/Users/A.M. MUKTAR/Desktop/ACTION LEARNING/Music_app/dataset/lyrics.csv")
def top_ten():
    for i in songs["dzr_sng_id"][:10].values:
        response = requests.get(f"https://api.deezer.com/track/{i}")
        response = json.loads(response.text)
        tracklist.append(response)
    return tracklist

#============================ VECTORIZE SEARCH PARAMETERS =======================#
sims = []
doc_id = []


def vectorize_search(song_lyrics):
    song_ref = song_lyrics["Lyrics"][0]
    ref_song = nlp(song_ref)
    # for i in range(len(song_lyrics)):
    #     sim = 
    return ref_song

#============================  GET SIMILAR MOVIES BASED ON COSINE SIMILARITY =====================#
# def get_similar(title_vec, tfidf_all_vec):
#     similarity = cosine_similarity(title_vec, tfidf_all_vec).flatten()
#     indices = np.argpartition(similarity, -1)[-1:]
#     results = movie_df.iloc[indices]
#     return results


#============================  GET SIMILAR MOVIES BASED ON COSINE SIMILARITY =====================#
def query_db(mood)-> pd.DataFrame:
    mood = "Sad"
    same_mood = songs[songs["Mood"]==mood]
    return same_mood