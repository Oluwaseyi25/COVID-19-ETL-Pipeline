import pandas as pd
import wget
import sqlalchemy
from sqlalchemy import create_engine
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

dag = DAG(dag_id='covid_dag', start_date=datetime(2024,1,5), schedule_interval='0 1 1-31/7 * *')


def download_upload_data():
    final_df = []
    for day in ['%0.2d' %i for i in range(1, 32)]:
        result = wget.download(f'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/01-{day}-2021.csv')
        df = pd.read_csv(result)
        final_df.append(df)
        df_final = pd.concat(final_df)

    conn_string = 'postgresql://oluwaseyi:root@postgres_seyi:5432/covid19_data'
    db = create_engine(conn_string)
    df_final.to_sql('covid19_report', con=db, if_exists='append', index=False)

with dag:
    download_upload_data_task = PythonOperator(task_id='download_upload_data',
                                          python_callable=download_upload_data)  #assigning the function as task

download_upload_data_task
