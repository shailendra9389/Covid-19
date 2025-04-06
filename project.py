import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\sps97\Desktop\python-project\Provisional_COVID-19_death_counts__rates__and_percent_of_total_deaths__by_jurisdiction_of_residence.csv')

if 'footnote' in df.columns:
    df.drop(columns=['footnote'], inplace=True)

df['data_period_start'] = pd.to_datetime(df['data_period_start'])
df['data_period_end'] = pd.to_datetime(df['data_period_end'])
df['data_as_of'] = pd.to_datetime(df['data_as_of'])

df_cleaned = df.dropna(subset=['COVID_deaths', 'crude_COVID_rate', 'COVID_pct_of_total'])

numeric_cols = df_cleaned.select_dtypes(include=[np.number]).columns
df_cleaned[numeric_cols] = df_cleaned[numeric_cols].fillna(df_cleaned[numeric_cols].median())

sns.set(style="whitegrid")
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

sns.histplot(df_cleaned['COVID_deaths'], bins=30, kde=True, ax=axes[0], color='skyblue')
axes[0].set_title('COVID-19 Deaths')

sns.histplot(df_cleaned['COVID_pct_of_total'], bins=30, kde=True, ax=axes[1], color='salmon')
axes[1].set_title('COVID % of Total Deaths')

sns.histplot(df_cleaned['crude_COVID_rate'], bins=30, kde=True, ax=axes[2], color='mediumseagreen')
axes[2].set_title('Crude COVID Death Rate')

plt.tight_layout()
plt.show()

fig, axes = plt.subplots(1, 3, figsize=(18, 5))

sns.boxplot(y=df_cleaned['COVID_deaths'], ax=axes[0], color='lightblue')
axes[0].set_title('COVID-19 Deaths')

sns.boxplot(y=df_cleaned['crude_COVID_rate'], ax=axes[1], color='lightgreen')
axes[1].set_title('Crude COVID Rate')

sns.boxplot(y=df_cleaned['COVID_pct_of_total'], ax=axes[2], color='lightcoral')
axes[2].set_title('COVID % of Total Deaths')

plt.tight_layout()
plt.show()
sns.set(style="whitegrid")
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

sns.scatterplot(data=df_cleaned, x='COVID_deaths', y='crude_COVID_rate', ax=axes[0], color='teal')
axes[0].set_title('Deaths vs Crude Rate')

sns.scatterplot(data=df_cleaned, x='COVID_deaths', y='COVID_pct_of_total', ax=axes[1], color='purple')
axes[1].set_title('Deaths vs % of Total')

sns.scatterplot(data=df_cleaned, x='crude_COVID_rate', y='COVID_pct_of_total', ax=axes[2], color='orange')
axes[2].set_title('Crude Rate vs % of Total')

plt.tight_layout()
plt.show()
