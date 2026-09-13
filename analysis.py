import pandas as pd

df = pd.read_csv('csvs_created/All Beauty 1.csv')
# df = pd.read_csv('raw_file/amazon_reviews_actual_5_5m.csv')
# all_beauty_pivot_table = pd.read_csv('pivot_tables/All Beauty_reviews_pivot_table.csv')

print(df.head(20))

df = df.head(20)
df.to_csv('test.csv')