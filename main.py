import pandas as pd

df = pd.read_csv('raw_file/amazon_reviews_actual_5_5m.csv')

print(df.head(10))

df_cols = list(df.columns)
index = 0

print("\ncolumns:\n")
for column_name in df_cols:
    try:
        print(index, column_name)
        index = index + 1
    except Exception as e:
        print(f"error - cannot grab {type(e)}")

print('review_id unique values: ', df['review_id'].unique())
print('product_id unique values: ', df['product_id'].unique())
print('parent_product_id unique values: ', df['parent_product_id'].unique())
print('product_name unique values: ', df['product_name'].unique())
print('brand_or_store unique values: ', df['brand_or_store'].unique())
print('main_category unique values: ', df['main_category'].unique())
print('price_usd unique values: ', df['price_usd'].unique())
print('product_average_rating unique values: ', df['product_average_rating'].unique())
print('product_rating_count unique values: ', df['product_rating_count'].unique())
print('review_score unique values: ', df['review_score'].unique())
print('review_title unique values: ', df['review_title'].unique())
print('review_text unique values: ', df['review_text'].unique())
print('reviewer_id unique values: ', df['reviewer_id'].unique())
print('review_datetime_utc unique values: ', df['review_datetime_utc'].unique())
print('review_timestamp_ms unique values: ', df['review_timestamp_ms'].unique())
print('helpful_votes unique values: ', df['helpful_votes'].unique())
print('verified_purchase unique values: ', df['verified_purchase'].unique())
print('review_has_images unique values: ', df['review_has_images'].unique())
print('review_image_count unique values: ', df['review_image_count'].unique())
print('product_features unique values: ', df['product_features'].unique())
print('product_description unique values: ', df['product_description'].unique())
print('product_categories unique values: ', df['product_categories'].unique())
print('dataset_category unique values: ', df['dataset_category'].unique())
print('data_source unique values: ', df['data_source'].unique())
print('source_is_actual unique values: ', df['source_is_actual'].unique())

# create + save multiple csvs