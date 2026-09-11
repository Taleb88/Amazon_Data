import pandas as pd

# df = pd.read_csv('csvs_created/All Beauty 1.csv')
df = pd.read_csv('raw_file/amazon_reviews_actual_5_5m.csv')

# print(df.head(20))

print(df[df['product_id'] == 'B010TWN80W'])