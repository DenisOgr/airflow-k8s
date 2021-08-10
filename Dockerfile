FROM apache/airflow:1.10.15-python3.7

# pip install --use-deprecated legacy-resolver "apache-airflow[google]==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"

COPY ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt