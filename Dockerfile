FROM apache/airflow:2.2.3

# Set Airflow environment variables for local development
ENV AIRFLOW__CORE__SQL_ALCHEMY_CONN=sqlite:////opt/airflow/airflow.db
ENV AIRFLOW__CORE__DAGS_FOLDER=/opt/airflow/dags

COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt