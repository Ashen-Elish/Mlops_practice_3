# Скрипт для обучения модели

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import mlflow
import mlflow.sklearn

# Загрузить обработанный датасет из локального файла
df = pd.read_csv("data/processed.csv")

# Начать отслеживание с mlflow
mlflow.start_run()

# Зарегистрировать параметры модели
mlflow.log_param("model", "LinearRegression")

# Выбрать независимые и зависимые переменные
X = df.drop('charges', axis=1)
y = df['charges']

# Разделить данные на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# Создать линейную регрессионную модель
model = LinearRegression()

# Обучить модель на обучающих данных
model.fit(X_train, y_train)

# Сохранить обученную модель в локальный файл
mlflow.sklearn.save_model(model, "model")

# Зарегистрировать артефакт с обученной моделью
mlflow.log_artifact("model")

# Завершить отслеж