import pandas as pd

df = pd.read_csv('csvs_created/All Beauty.csv') # 4266963 rows

df_1 = df[:500000]

# print(df_1)

df_1.to_csv('test.csv')