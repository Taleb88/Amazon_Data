from pyspark import pipelines as dp

from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    DoubleType,
    LongType,
    BooleanType
)

from pyspark.sql.functions import (
    col,
    trim,
    to_timestamp
)


# ============================================================
# AMAZON ALL BEAUTY ETL PIPELINE
# ============================================================

# Source CSV located in Unity Catalog Volume
file_path = "/Volumes/amazon_data/default/all_beauty_five/All Beauty 5.csv"


# ============================================================
# DEFINE CSV SCHEMA
# ============================================================

schema = StructType([

    StructField(
        "review_id",
        StringType(),
        True
    ),

    StructField(
        "product_id",
        StringType(),
        True
    ),

    StructField(
        "parent_product_id",
        StringType(),
        True
    ),

    StructField(
        "product_name",
        StringType(),
        True
    ),

    StructField(
        "brand_or_store",
        StringType(),
        True
    ),

    StructField(
        "main_category",
        StringType(),
        True
    ),

    StructField(
        "price_usd",
        DoubleType(),
        True
    ),

    StructField(
        "product_average_rating",
        DoubleType(),
        True
    ),

    StructField(
        "product_rating_count",
        LongType(),
        True
    ),

    StructField(
        "review_score",
        DoubleType(),
        True
    ),

    StructField(
        "review_title",
        StringType(),
        True
    ),

    StructField(
        "review_text",
        StringType(),
        True
    ),

    StructField(
        "reviewer_id",
        StringType(),
        True
    ),

    StructField(
        "review_datetime_utc",
        StringType(),
        True
    ),

    StructField(
        "review_timestamp_ms",
        LongType(),
        True
    ),

    StructField(
        "helpful_votes",
        LongType(),
        True
    ),

    StructField(
        "verified_purchase",
        BooleanType(),
        True
    ),

    StructField(
        "review_has_images",
        BooleanType(),
        True
    ),

    StructField(
        "review_image_count",
        LongType(),
        True
    ),

    StructField(
        "product_features",
        StringType(),
        True
    ),

    StructField(
        "product_description",
        StringType(),
        True
    ),

    StructField(
        "product_categories",
        StringType(),
        True
    ),

    StructField(
        "dataset_category",
        StringType(),
        True
    ),

    StructField(
        "data_source",
        StringType(),
        True
    ),

    StructField(
        "source_is_actual",
        BooleanType(),
        True
    )

])


# ============================================================
# PIPELINE TABLE
# ============================================================

@dp.table(
    name="all_beauty_five",
    comment="""
    Amazon All Beauty review data.
    Extracted from Unity Catalog Volume,
    transformed using PySpark,
    and loaded into a Delta table.
    """
)
def all_beauty_five():

    # ========================================================
    # EXTRACT
    # Read CSV directly from Unity Catalog Volume
    # ========================================================

    df = (
        spark.read
            .format("csv")
            .option(
                "header",
                True
            )
            .option(
                "multiLine",
                True
            )
            .option(
                "quote",
                '"'
            )
            .option(
                "escape",
                '"'
            )
            .schema(
                schema
            )
            .load(
                file_path
            )
    )


    # ========================================================
    # SELECT COLUMNS
    # ========================================================

    columns = [

        "review_id",
        "product_id",
        "parent_product_id",
        "product_name",
        "brand_or_store",
        "main_category",
        "price_usd",
        "product_average_rating",
        "product_rating_count",
        "review_score",
        "review_title",
        "review_text",
        "reviewer_id",
        "review_datetime_utc",
        "review_timestamp_ms",
        "helpful_votes",
        "verified_purchase",
        "review_has_images",
        "review_image_count",
        "product_features",
        "product_description",
        "product_categories",
        "dataset_category",
        "data_source",
        "source_is_actual"

    ]

    df = df.select(
        columns
    )


    # ========================================================
    # TRANSFORM
    # ========================================================

    df = (

        df

        # ----------------------------------------------------
        # Trim review ID
        # ----------------------------------------------------

        .withColumn(
            "review_id",
            trim(
                col("review_id")
            )
        )


        # ----------------------------------------------------
        # Trim product ID
        # ----------------------------------------------------

        .withColumn(
            "product_id",
            trim(
                col("product_id")
            )
        )


        # ----------------------------------------------------
        # Trim parent product ID
        # ----------------------------------------------------

        .withColumn(
            "parent_product_id",
            trim(
                col("parent_product_id")
            )
        )


        # ----------------------------------------------------
        # Trim product name
        # ----------------------------------------------------

        .withColumn(
            "product_name",
            trim(
                col("product_name")
            )
        )


        # ----------------------------------------------------
        # Trim brand/store
        # ----------------------------------------------------

        .withColumn(
            "brand_or_store",
            trim(
                col("brand_or_store")
            )
        )


        # ----------------------------------------------------
        # Trim main category
        # ----------------------------------------------------

        .withColumn(
            "main_category",
            trim(
                col("main_category")
            )
        )


        # ----------------------------------------------------
        # Trim reviewer ID
        # ----------------------------------------------------

        .withColumn(
            "reviewer_id",
            trim(
                col("reviewer_id")
            )
        )


        # ----------------------------------------------------
        # Trim dataset category
        # ----------------------------------------------------

        .withColumn(
            "dataset_category",
            trim(
                col("dataset_category")
            )
        )


        # ----------------------------------------------------
        # Trim data source
        # ----------------------------------------------------

        .withColumn(
            "data_source",
            trim(
                col("data_source")
            )
        )


        # ----------------------------------------------------
        # Convert review date string to timestamp
        # ----------------------------------------------------

        .withColumn(
            "review_datetime_utc",
            to_timestamp(
                col("review_datetime_utc")
            )
        )


        # ----------------------------------------------------
        # Remove duplicate reviews based on review_id
        # ----------------------------------------------------

        .dropDuplicates(
            [
                "review_id"
            ]
        )

    )


    # ========================================================
    # LOAD
    #
    # Returning the DataFrame tells Databricks to load the
    # transformed data into the pipeline-managed table:
    #
    # amazon_data.default.all_beauty_one
    #
    # assuming the pipeline catalog is:
    # amazon_data
    #
    # and the pipeline schema is:
    # default
    # ========================================================

    return df