## Human health study

## Reproducibility
- Python version: **Python 3.14.1
- A fixed random seed is used in the notebook (`np.random.seed(42)`).

## Setup
Create/activate a virtual environment and install dependencies:

```bash
pip install -r requirements.txt
```

Data quality:
The dataset contains 800 participants and no missing values. Categorical variables (sex, smoker, disease) contain only expected categories, so no cleaning was required.

Descriptive statistics:\
Key health variables (age, height, weight, systolic BP, cholesterol) fall within plausible ranges for an adult population.

Visuals:
- Systolic blood pressure appears approximately unimodal in distribution.
- Weight differs in central tendency and spread by sex.
- Most participants are non-smokers (moderate class imbalance).

Simulation:\
The observed disease prevalence was used as a probability parameter to simulate 1000 individuals; the simulated prevalence was close to the observed value, with expected random variation.

Confidence interval:\
A 95% bootstrap confidence interval was computed for the mean systolic blood pressure, providing a plausible range for the population mean.

Hypothesis test:\
A one-sided Welch two-sample t-test was used to test whether smokers have higher mean systolic blood pressure than non-smokers. The conclusion is based on the p-value compared to α = 0.05. (No causal interpretation is made.)
