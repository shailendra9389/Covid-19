import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Correct file path using raw string
df = pd.read_csv(r'C:\Users\sps97\Desktop\python-project\Provisional_COVID-19_death_counts__rates__and_percent_of_total_deaths__by_jurisdiction_of_residence.csv')

# Print first 5 rows
print(df.head())


# Set plot style
# Step 1: Import required libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Step 2: Load the CSV file


# Step 3: Drop the 'footnote' column if it exists
if 'footnote' in df.columns:
    df.drop(columns=['footnote'], inplace=True)

# Step 4: Convert date columns to datetime
df['data_period_start'] = pd.to_datetime(df['data_period_start'])
df['data_period_end'] = pd.to_datetime(df['data_period_end'])
df['data_as_of'] = pd.to_datetime(df['data_as_of'])

# Step 5: Drop rows where key columns are missing
df_cleaned = df.dropna(subset=['COVID_deaths', 'crude_COVID_rate', 'COVID_pct_of_total'])

# Step 6: Fill remaining numeric missing values with median
numeric_cols = df_cleaned.select_dtypes(include=[np.number]).columns
df_cleaned[numeric_cols] = df_cleaned[numeric_cols].fillna(df_cleaned[numeric_cols].median())

# Step 7: Plot histograms for 3 key columns
sns.set(style="whitegrid")
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Histogram for COVID_deaths
sns.histplot(df_cleaned['COVID_deaths'], bins=30, kde=True, ax=axes[0], color='skyblue')
axes[0].set_title('Histogram of COVID-19 Deaths')
axes[0].set_xlabel('COVID-19 Deaths')

# Histogram for COVID_pct_of_total
sns.histplot(df_cleaned['COVID_pct_of_total'], bins=30, kde=True, ax=axes[1], color='salmon')
axes[1].set_title('Histogram of COVID % of Total Deaths')
axes[1].set_xlabel('COVID % of Total Deaths')

# Histogram for crude_COVID_rate
sns.histplot(df_cleaned['crude_COVID_rate'], bins=30, kde=True, ax=axes[2], color='mediumseagreen')
axes[2].set_title('Histogram of Crude COVID Death Rate')
axes[2].set_xlabel('Crude COVID Death Rate')

plt.tight_layout()
plt.show()
# Set the plot style
sns.set(style="whitegrid")

# Create a figure with subplots
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Box plot for COVID_deaths
sns.boxplot(y=df_cleaned['COVID_deaths'], ax=axes[0], color='lightblue')
axes[0].set_title('Box Plot of COVID-19 Deaths')

# Box plot for crude_COVID_rate
sns.boxplot(y=df_cleaned['crude_COVID_rate'], ax=axes[1], color='lightgreen')
axes[1].set_title('Box Plot of Crude COVID Rate')

# Box plot for COVID_pct_of_total
sns.boxplot(y=df_cleaned['COVID_pct_of_total'], ax=axes[2], color='lightcoral')
axes[2].set_title('Box Plot of COVID % of Total Deaths')

plt.tight_layout()
plt.show()
