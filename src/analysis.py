import pandas as pd


def load_data(csv_path: str) -> pd.DataFrame:
    """
    Load the health study CSV dataset into a DataFrame.

    Parameters
    ----------
    csv_path:
        Relative path to the CSV file (e.g., "../data/health_study_dataset.csv").

    Returns
    -------
    pd.DataFrame
        DataFrame containing the health study dataset.
    """
    df = pd.read_csv(csv_path)
    return df


def summary_stats(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    """
    Compute basic descriptive statistics for selected columns.

    Parameters
    ----------
    df:
        Input DataFrame.
    columns:
        List of column names to summarize.

    Returns
    -------
    pd.DataFrame
        DataFrame with mean, median, min, and max for each column.
    """
    stats = {}

    for col in columns:
        stats[col] = {
            "mean": df[col].mean(),
            "median": df[col].median(),
            "min": df[col].min(),
            "max": df[col].max(),
        }

    return pd.DataFrame(stats)
