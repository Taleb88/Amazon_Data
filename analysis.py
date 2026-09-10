import pandas as pd

df = pd.read_csv('csvs_created/All Beauty.csv') # 4266963 rows

df_1 = df[:1000000]

# print(df_1)