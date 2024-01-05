# Скрипт для оценки модели

import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import mlflow
import mlflow.sklearn

# Загрузить обработанный датасет из локального файла
df = pd.read_csv("data/processed.csv")

# Начать отслеживание с mlflow
mlflow.start_run()

# Выбрать независимые и зависимые переменные
X = df.drop('charges', axis=1)
y = df['charges']

# Разделить данные на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# Загрузить обученную модель из локального файла
model = mlflow.sklearn.load_model("model")

# Сделать прогнозы на тестовых данных
y_pred = model.predict(X_test)

# Посчитать MAE (среднюю абсолютную ошибку)
mae = mean_absolute_error(y_test, y_pred)
print(f'Mean Absolute Error: {mae:.2f}')

# Зарегистрировать метрику MAE
mlflow.log_metric("mae", mae)

# Посчитать MSE (среднюю квадратичную ошибку)
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse:.2f}')

# Зарегистрировать метрику MSE
mlflow.log_metric("mse", mse)

# Посчитать RMSE (корень из средней квадратичной ошибки)
rmse = np.sqrt(mse)
print(f'Root Mean Squared Error: {rmse:.2f}')

# Зарегистрировать метрику RMSE
mlflow.log_metric("rmse", rmse)

# Посчитать R-квадрат (коэффициент детерминации)
r2 = r2_score(y_test, y_pred)
print(f'R-squared: {r2:.2f}')

# Зарегистрировать метрику R-квадрат
mlflow.log_metric("r2", r2)

# Завершить отслеживание с mlflow
mlflow.end_run()
