import pandas as pd

# df = pd.read_csv('csvs_created/All Beauty 1.csv')
# df = pd.read_csv('raw_file/amazon_reviews_actual_5_5m.csv')
all_beauty_pivot_table = pd.read_csv('pivot_tables/All Beauty_pivot_table.csv')

print(all_beauty_pivot_table[all_beauty_pivot_table['1.0'].notna()])