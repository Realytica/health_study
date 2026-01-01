import matplotlib.pyplot as plt
import pandas as pd


def plot_bp_hist(df: pd.DataFrame) -> None:
    """
    Plot a histogram of systolic blood pressure.

    Parameters
    ----------
    df:
        Input DataFrame containing a 'systolic_bp' column.
    """
    plt.figure(figsize=(8, 5))
    plt.hist(df["systolic_bp"], bins=20)
    plt.axvline(df["systolic_bp"].mean(), color = "red", linestyle = "--")
    plt.xlabel("Systolic Blood Pressure (mmHg)")
    plt.ylabel("Count")
    plt.title("Distribution of Systolic Blood Pressure")
    plt.show()


def plot_weight_box_by_sex(df: pd.DataFrame) -> None:
    """
    Plot a boxplot of weight stratified by sex.

    Parameters
    ----------
    df:
        Input DataFrame containing 'sex' and 'weight' columns.
    """
    weights_female = df[df["sex"] == "F"]["weight"]
    weights_male = df[df["sex"] == "M"]["weight"]

    plt.figure(figsize=(8, 5))
    plt.boxplot(
        [weights_female, weights_male],
        tick_labels=["Female", "Male"],
    )
    plt.ylabel("Weight (kg)")
    plt.title("Weight Distribution by Sex")
    plt.show()


def plot_smoker_proportions(df: pd.DataFrame) -> None:
    """
    Plot a bar chart of smoker proportions.

    Parameters
    ----------
    df:
        Input DataFrame containing a 'smoker' column (e.g., Yes/No).
    """
    smoker_prop = df["smoker"].value_counts(normalize=True)

    plt.figure(figsize=(6, 4))
    plt.bar(smoker_prop.index.astype(str), smoker_prop.values)
    plt.ylabel("Proportion")
    plt.title("Proportion of Smokers")
    plt.ylim(0, 1)
    plt.show()
