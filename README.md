# Summary of this Project
This a end to end ETL pipe which utilizes Python, Docker, airflow and PostgreSQL.
I ingested data from an online repository using wget and transformed this data across different timelines into a single dataframe. Then, I used sqlalchemy to migrate this data in postgres. Docker help me in containerization of postgres and pgadmin thereby using localhost 8080 as my data warehouse. I utilized airflow for ochestration creating a DAG to perform this task, I also added a cron job schedule to trigger the pipeline every week.
