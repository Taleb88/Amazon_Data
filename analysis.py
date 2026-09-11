import pandas as pd

df = pd.read_csv('csvs_created/All Beauty 1.csv')

print(df.head(20))

test = df.head(30)
test.to_csv('test.csv', index=False)