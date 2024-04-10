import pandas as pd
import wget
import sqlalchemy
from sqlalchemy import create_engine


final_df = []
for day in ['%0.2d' %i for i in range(1, 32)]:
    result = wget.download(f'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/'
                           f'csse_covid_19_daily_reports/01-{day}-2021.csv')
    df = pd.read_csv(result)
    final_df.append(df)
    df_final = pd.concat(final_df)

conn_string = 'postgresql://oluwaseyi:root@postgres:5432/covid19_data'
db = create_engine(conn_string)
df_final.to_sql('covid19_report', con=db, if_exists='append', index=False)
# docker run --name some-postgres -e  POSTGRES_USER=oluwaseyi -e POSTGRES_PASSWORD=0296 -e POSTGRES_DB=covid19_data --network oluwaseyi -d postgres
# docker run --name my-pgadmin -p 82:80 -e 'PGADMIN_DEFAULT_EMAIL=omolewaoluranti@gmail.com' -e 'PGADMIN_DEFAULT_PASSWORD=0296' --network oluwaseyi -d dpage/pgadmin4
# docker network create -d bridge oluwaseyi