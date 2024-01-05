FROM python:3.7

# устанавливаем MLflow
RUN pip install mlflow

# загружаем датасет с Kaggle
RUN pip install kaggle
RUN mkdir /data
RUN kaggle datasets download -d code/theoneandonlyp/medical-cost-personal-datasets -p /data
RUN unzip /data/medical-cost-personal-datasets.zip -d /data

# подготавливаем данные
RUN pip install pandas scikit-learn
COPY prepare_data.py /app/prepare_data.py
RUN python /app/prepare_data.py --input_file /data/insurance.csv --output_file /data/insurance_prepared.csv

# обучаем модель линейной регрессии и сохраняем ее в формате MLflow
COPY train_model.py /app/train_model.py
RUN python /app/train_model.py --input_file /data/insurance_prepared.csv --output_file /model

# запускаем MLflow с моделью и предоставляем REST API
ENTRYPOINT ["mlflow", "models", "serve", "-m", "/model", "-p", "5000"]
