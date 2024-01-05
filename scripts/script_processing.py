# Скрипт для обработки данных

import pandas as pd
import mlflow

# Загрузить датасет из локального файла
df = pd.read_csv("data/insurance.csv")

# Начать отслеживание с mlflow
mlflow.start_run()

# Зарегистрировать параметры обработки данных
mlflow.log_param("drop_first", True)
mlflow.log_param("test_size", 0.3)
mlflow.log_param("random_state", 0)

# Проверить типы данных и пропущенные значения
df.info()
df.isnull().sum()

# Вывести первые пять строк датафрейма
df.head()

# Вывести статистику по датафрейму
df.describe()

# Вывести уникальные значения столбца sex
unique_values = df['sex'].unique()
print(unique_values)

# Вывести уникальные значения столбца region
unique_values = df['region'].unique()
print(unique_values)

# Заменить строки 'yes' и 'no' на бинарные значения 1 и 0
df['smoker'] = df['smoker'].replace({'yes': 1, 'no': 0})

# Преобразовать столбец smoker в числовые значения
df['smoker'] = df['smoker'].astype(int)

# Просмотреть обновленный датафрейм
df.head()

# Заменить строки 'yes' и 'no' на бинарные значения 1 и 0
df['sex'] = df['sex'].replace({'yes': 1, 'no': 0})

# Заменить строки 'male' и 'female' на бинарные значения 1 и 0
df['sex'] = df['sex'].replace({'male': 1, 'female': 0})

# Просмотреть обновленный датафрейм
df.head()

# Создать бинарные фиктивные переменные для каждой категории, кроме первой, и удалить исходный столбец
df = pd.get_dummies(df, drop_first=True)

# Просмотреть обновленный датафрейм
df.head()

# Сохранить обработанный датасет в локальный файл
df.to_csv("data/processed.csv", index=False)

# Зарегистрировать артефакт с обработанным датасетом
mlflow.log_artifact("data/processed.csv")

# Завершить отслеживание с mlflow
mlflow.end_run()
