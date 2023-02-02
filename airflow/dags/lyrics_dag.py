from datetime import timedelta, datetime
from airflow.decorators import dag, task
from airflow.utils.dates import days_ago
from dag_lib import call_song_bert_api, call_lyrics_bert_api
import pandas as pd


@dag(
    dag_id='lyrics_read_predict_store_dag',
    description='Lyrics Ingest - Predict - Store DAG',
    schedule=None, #timedelta(minutes=2),
    start_date=days_ago(n=0, hour=1)
)
def lyrics_ingest_predict_dag():
    @task
    def read_data(file) -> pd.DataFrame:
        file_path = f'/g/EPITA S3/Action Learning/dev1/music-mood-recognition/dataset/airflow_input_data/{file}'
        lines = []
        with open(file_path, "r") as file_obj:
            file_data = file_obj.read()
            lines = file_data.splitlines()
        df = pd.DataFrame(lines, columns=['lyrics'])
        df_for_predict = df
        return df_for_predict
    
    @task
    def call_api(df_for_predict) -> pd.DataFrame:
        mood_list = []
        for i in df_for_predict.index:
            lyrics = df_for_predict['lyrics'][i]
            mood = call_lyrics_bert_api(lyrics)
            mood_list.append(mood)
        df_for_predict['Mood'] = mood_list
        return df_for_predict
    
    @task
    def store_predictions(predicted_df):
        op_file_name = f'predicted_lyrics_file_{int(round(datetime.now().timestamp()))}'
        file_path = f'/g/EPITA S3/Action Learning/dev1/music-mood-recognition/dataset/airflow_output_data/{op_file_name}'
        predicted_df.to_csv(file_path)

    # Task Chaining
    df_for_predict = read_data('lyrics-sample-data-1.csv')
    predicted_df = call_api(df_for_predict)
    store_predictions(predicted_df)

_ = lyrics_ingest_predict_dag()
