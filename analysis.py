import pandas as pd

# df = pd.read_csv('csvs_created/All Beauty 1.csv')
# df = pd.read_csv('raw_file/amazon_reviews_actual_5_5m.csv')
reviews_df = pd.read_csv('csvs_created/Computers.csv')

reviews_df_pivot_table = reviews_df.pivot_table(index='product_id', columns='review_score', values='product_rating_count', aggfunc='mean')
print(reviews_df_pivot_table.head(30))

# reviews_df_pivot_table.to_csv('test.csv')