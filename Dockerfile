FROM apache/airflow:2.1.2-python3.9

COPY ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt