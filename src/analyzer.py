import pandas as pd

from analysis import summary_stats
from visuals import (
    plot_bp_hist,
    plot_weight_box_by_sex,
    plot_smoker_proportions,
)


class HealthAnalyzer:
    """
    Encapsulates analysis and visualization for the health study dataset.
    """

    def __init__(self, df: pd.DataFrame) -> None:
        """
        Initialize the analyzer with the health study DataFrame.

        Parameters
        ----------
        df:
            DataFrame containing the health study data.
        """
        self.df = df

    def describe(self, columns: list[str]) -> pd.DataFrame:
        """
        Compute descriptive statistics for selected columns.
        """
        return summary_stats(self.df, columns)

    def plot_blood_pressure(self) -> None:
        """
        Plot histogram of systolic blood pressure.
        """
        plot_bp_hist(self.df)

    def plot_weight_by_sex(self) -> None:
        """
        Plot weight distribution stratified by sex.
        """
        plot_weight_box_by_sex(self.df)

    def plot_smoker_share(self) -> None:
        """
        Plot proportion of smokers in the dataset.
        """
        plot_smoker_proportions(self.df)
