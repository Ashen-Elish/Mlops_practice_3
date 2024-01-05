# останавливаем веб-сервер и планировщик Airflow
airflow stop webserver
airflow stop scheduler
# удаляем файлы и папки, связанные с Airflow
rm -rf ~/airflow
rm -rf ~/airflow.cfg
rm -rf ~/airflow.db
rmdir ~/airflow
