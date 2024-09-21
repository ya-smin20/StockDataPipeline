
FROM apache/airflow:2.10.1


COPY ./dags /opt/airflow/dags
COPY ./scripts /opt/airflow/scripts


ENV PYTHONPATH="${PYTHONPATH}:/opt/airflow/scripts"
