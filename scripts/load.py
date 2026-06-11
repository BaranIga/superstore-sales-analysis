import os
import pandas as pd

from scripts.logger import logger


def save_data(
    df: pd.DataFrame,
    output_path: str
) -> None:

    try:

        os.makedirs(
            os.path.dirname(output_path),
            exist_ok=True
        )

        df.to_csv(
            output_path,
            index=False
        )

        logger.info(
            f"Saved data to {output_path}"
        )

    except Exception as e:

        logger.exception(
            f"Error saving file {output_path}: {e}"
        )

        raise