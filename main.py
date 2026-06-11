from scripts.extract import extract_data
from scripts.transform import clean_data, engineer_features
from scripts.load import save_data
from scripts.load_sqlite import save_to_sqlite
from scripts.analysis  import (
    sales_by_region,
    profit_by_category,
    top_products,
    monthly_sales,
    avg_delivery_time
)
from scripts.logger import logger


RAW_PATH = "data/raw/sales.csv"
CLEAN_PATH = "data/cleaned/sales_cleaned.csv"
DB_PATH = "data/sales.db"


def main():

    try:

        df = extract_data(RAW_PATH)

        df = clean_data(df)

        df = engineer_features(df)

        save_data(
            df,
            CLEAN_PATH
        )

        save_to_sqlite(
            df,
            DB_PATH,
            "sales"
        )

        save_data(
            sales_by_region(DB_PATH),
            "data/analysis/sales_by_region.csv"
        )

        save_data(
            profit_by_category(DB_PATH),
            "data/analysis/profit_by_category.csv"
        )

        save_data(
            top_products(DB_PATH),
            "data/analysis/top_products.csv"
        )

        save_data(
            monthly_sales(DB_PATH),
            "data/analysis/monthly_sales.csv"
        )

        save_data(
            avg_delivery_time(DB_PATH),
            "data/analysis/avg_delivery_time.csv"
        )

        logger.info(
            "Pipeline completed successfully"
        )

    except Exception as e:

        logger.exception(
            f"Pipeline failed: {e}"
        )

        raise

if __name__ == "__main__":
    main()