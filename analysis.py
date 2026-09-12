import pandas as pd

# df = pd.read_csv('csvs_created/All Beauty 1.csv')
# df = pd.read_csv('raw_file/amazon_reviews_actual_5_5m.csv')
computer_reviews_df = pd.read_csv('csvs_created/Computers.csv')

computer_reviews_df_pivot_table = computer_reviews_df.pivot_table(index='product_id', columns='review_score', values='product_rating_count', aggfunc='mean')
print(computer_reviews_df_pivot_table.head(30))

computer_reviews_df_pivot_table.to_csv('pivot_tables/computer_reviews_pivot_table.csv')