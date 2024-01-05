# Скрипт для загрузки датасета

import pandas as pd
import dvc.api

# Загрузить датасет из удаленного хранилища с помощью dvc
with dvc.api.open(
    path="data/insurance.csv",
    repo="https://github.com/Ashen-Elish/Mlops_practice_3.git",
    mode="r",
    remote="s3://bucket/path"
) as fd:
    df = pd.read_csv(fd)

# Сохранить датасет в локальный файл
df.to_csv("data/insurance.csv", index=False)
