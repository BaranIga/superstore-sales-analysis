import sqlite3
import pandas as pd

from scripts.logger import logger


def save_to_sqlite(
    df: pd.DataFrame,
    db_path: str,
    table_name: str
) -> None:

    try:

        conn = sqlite3.connect(db_path)

        df.to_sql(
            table_name,
            conn,
            if_exists="replace",
            index=False
        )

        conn.close()

        logger.info(
            f"Saved {len(df)} rows to SQLite table '{table_name}'"
        )

    except sqlite3.Error as e:

        logger.exception(
            f"SQLite error: {e}"
        )

        raise