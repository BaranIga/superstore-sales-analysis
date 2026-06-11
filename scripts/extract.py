import pandas as pd

from scripts.logger import logger


def extract_data(path: str) -> pd.DataFrame:
    
    try:
        df = pd.read_csv(
            path,
            encoding="latin1"
        )

        logger.info(
            f"Loaded {len(df)} rows from {path}"
        )

        return df

    except FileNotFoundError:

        logger.error(
            f"File not found: {path}"
        )

        raise

    except Exception as e:

        logger.exception(
            f"Unexpected error while loading file: {e}"
        )

        raise