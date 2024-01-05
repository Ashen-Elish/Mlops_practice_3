# инициализируем базу данных Airflow
airflow initdb
# запускаем веб-сервер Airflow в фоновом режиме
airflow webserver -D
# запускаем планировщик Airflow в фоновом режиме
airflow scheduler -D
# запускаем наш рабочий процесс
airflow trigger_dag dag
