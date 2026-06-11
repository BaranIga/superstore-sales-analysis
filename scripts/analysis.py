import sqlite3
import pandas as pd


# sprzedaż według regionu
def sales_by_region(db_path):

    conn = sqlite3.connect(db_path)

    query = """
    SELECT
        region,
        ROUND(SUM(sales), 2) AS total_sales
    FROM sales
    GROUP BY region
    ORDER BY total_sales DESC
    """

    result = pd.read_sql_query(
        query,
        conn
    )

    conn.close()

    return result


# zysk wg kategorii
def profit_by_category(db_path):

    conn = sqlite3.connect(db_path)

    query = """
    SELECT
        category,
        ROUND(SUM(profit), 2) AS total_profit
    FROM sales
    GROUP BY category
    ORDER BY total_profit DESC
    """

    result = pd.read_sql_query(
        query,
        conn
    )

    conn.close()

    return result


# top 10 projektów
def top_products(db_path):

    conn = sqlite3.connect(db_path)

    query = """
    SELECT
        product_name,
        ROUND(SUM(sales), 2) AS total_sales
    FROM sales
    GROUP BY product_name
    ORDER BY total_sales DESC
    LIMIT 10
    """

    result = pd.read_sql_query(
        query,
        conn
    )

    conn.close()

    return result

# sprzedaż miesięczna
def monthly_sales(db_path):

    conn = sqlite3.connect(db_path)

    query = """
    SELECT
        order_year,
        order_month,
        ROUND(SUM(sales), 2) AS total_sales
    FROM sales
    GROUP BY
        order_year,
        order_month
    ORDER BY
        order_year,
        order_month
    """

    result = pd.read_sql_query(
        query,
        conn
    )

    conn.close()

    return result


# średni czas dostawy
def avg_delivery_time(db_path):

    conn = sqlite3.connect(db_path)

    query = """
    SELECT
        ROUND(
            AVG(delivery_days),
            2
        ) AS avg_delivery_days
    FROM sales
    """

    result = pd.read_sql_query(
        query,
        conn
    )

    conn.close()

    return result