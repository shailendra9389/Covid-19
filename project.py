# import pandas as pd
# import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt

# # Load the data from csv file
# df = pd.read_csv(r'C:\Users\sps97\Desktop\python-project\Provisional_COVID-19_death_counts__rates__and_percent_of_total_deaths__by_jurisdiction_of_residence.csv')

# # Basic EDA summary
# print("----- HEAD (First 5 Rows) -----")
# print(df.head())

# print("\n----- INFO -----")
# print(df.info())

# print("\n----- DESCRIBE (Numerical Stats) -----")
# print(df.describe())

# # Drop unnecessary column nad rows

# if 'footnote' in df.columns:
#     df.drop(columns=['footnote'], inplace=True)

# # Convert date columns to datetime
# df['data_period_start'] = pd.to_datetime(df['data_period_start'])
# df['data_period_end'] = pd.to_datetime(df['data_period_end'])
# df['data_as_of'] = pd.to_datetime(df['data_as_of'])

# # Drop rows with missing key values
# df_cleaned = df.dropna(subset=['COVID_deaths', 'crude_COVID_rate', 'COVID_pct_of_total'])

# # Fill numeric NaNs with median values fro each column
# # this is common practice for handling missing data
# numeric_cols = df_cleaned.select_dtypes(include=[np.number]).columns
# df_cleaned[numeric_cols] = df_cleaned[numeric_cols].fillna(df_cleaned[numeric_cols].median())

# # Histograms code
# sns.set(style="whitegrid")
# fig, axes = plt.subplots(1, 3, figsize=(18, 5))
# sns.histplot(df_cleaned['COVID_deaths'], bins=30, kde=True, ax=axes[0], color='skyblue')
# axes[0].set_title('COVID-19 Deaths')

# sns.histplot(df_cleaned['COVID_pct_of_total'], bins=30, kde=True, ax=axes[1], color='salmon')
# axes[1].set_title('COVID % of Total Deaths')

# sns.histplot(df_cleaned['crude_COVID_rate'], bins=30, kde=True, ax=axes[2], color='mediumseagreen')
# axes[2].set_title('Crude COVID Death Rate')

# plt.tight_layout()
# plt.show()

# # Boxplots code 
# fig, axes = plt.subplots(1, 3, figsize=(18, 5))
# sns.boxplot(y=df_cleaned['COVID_deaths'], ax=axes[0], color='lightblue')
# axes[0].set_title('COVID-19 Deaths')

# sns.boxplot(y=df_cleaned['crude_COVID_rate'], ax=axes[1], color='lightgreen')
# axes[1].set_title('Crude COVID Rate') #this is a box plot

# sns.boxplot(y=df_cleaned['COVID_pct_of_total'], ax=axes[2], color='lightcoral')
# axes[2].set_title('COVID % of Total Deaths')  # title

# plt.tight_layout()
# plt.show()

# # Scatter plots
# fig, axes = plt.subplots(1, 3, figsize=(18, 5))
# sns.scatterplot(data=df_cleaned, x='COVID_deaths', y='crude_COVID_rate', ax=axes[0], color='teal')
# axes[0].set_title('Deaths vs Crude Rate')

# sns.scatterplot(data=df_cleaned, x='COVID_deaths', y='COVID_pct_of_total', ax=axes[1], color='purple')
# axes[1].set_title('Deaths vs % of Total')

# sns.scatterplot(data=df_cleaned, x='crude_COVID_rate', y='COVID_pct_of_total', ax=axes[2], color='orange')
# axes[2].set_title('Crude Rate vs % of Total')

# plt.tight_layout()
# plt.show()

# # Correlation heatmap
# correlation = df_cleaned[['COVID_deaths', 'crude_COVID_rate', 'COVID_pct_of_total']].corr()
# plt.figure(figsize=(8, 6))
# sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt=".2f", square=True)
# plt.title("Correlation Heatmap")
# plt.show()

# # Pairplot
# sns.pairplot(df_cleaned[["COVID_deaths", "crude_COVID_rate", "COVID_pct_of_total"]],
#              kind="scatter", plot_kws={"s": 50, "color": "orange"})
# plt.suptitle("Pairplot of COVID-19 Metrics", y=1.02)
# plt.show()





import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv(r'C:\Users\sps97\Desktop\python-project\Provisional_COVID-19_death_counts__rates__and_percent_of_total_deaths__by_jurisdiction_of_residence.csv')

# Standardize column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Show head, info, and describe
print("🔹 HEAD (first 5 rows):")
print(df.head())
print("\n🔹 INFO:")
print(df.info())
print("\n🔹 DESCRIBE:")
print(df.describe(include='all'))

# Use only the first 500 rows
df = df.head(500)

# Drop 'footnote' column if it exists
if 'footnote' in df.columns:
    df.drop(columns=['footnote'], inplace=True)

# Convert date columns to datetime format
for col in ['data_period_start', 'data_period_end', 'data_as_of']:
    if col in df.columns:
        df[col] = pd.to_datetime(df[col], errors='coerce')

# Drop rows with missing critical values
required_cols = ['covid_deaths', 'crude_covid_rate', 'covid_pct_of_total']
df_cleaned = df.dropna(subset=[col for col in required_cols if col in df.columns])

# Ensure numeric conversion
for col in required_cols:
    df_cleaned[col] = pd.to_numeric(df_cleaned[col], errors='coerce')

# Fill remaining numeric NaNs with median
numeric_cols = df_cleaned.select_dtypes(include='number').columns
df_cleaned[numeric_cols] = df_cleaned[numeric_cols].fillna(df_cleaned[numeric_cols].median())

# Set seaborn theme
sns.set(style="whitegrid")

# ----------- HISTOGRAMS -----------
fig, axes = plt.subplots(1, 3, figsize=(18, 5))
sns.histplot(df_cleaned['covid_deaths'], bins=20, kde=True, ax=axes[0], color='skyblue')
axes[0].set_title('COVID-19 Deaths')

sns.histplot(df_cleaned['covid_pct_of_total'], bins=20, kde=True, ax=axes[1], color='salmon')
axes[1].set_title('% of Total Deaths')

sns.histplot(df_cleaned['crude_covid_rate'], bins=20, kde=True, ax=axes[2], color='green')
axes[2].set_title('Crude COVID Rate')

plt.tight_layout()
plt.show()

# ----------- BOXPLOTS -----------
fig, axes = plt.subplots(1, 3, figsize=(18, 5))
sns.boxplot(y=df_cleaned['covid_deaths'], ax=axes[0], color='lightblue')
axes[0].set_title('COVID Deaths')

sns.boxplot(y=df_cleaned['crude_covid_rate'], ax=axes[1], color='lightgreen')
axes[1].set_title('Crude Rate')

sns.boxplot(y=df_cleaned['covid_pct_of_total'], ax=axes[2], color='lightcoral')
axes[2].set_title('% of Total')

plt.tight_layout()
plt.show()

# ----------- SCATTER PLOTS -----------
fig, axes = plt.subplots(1, 3, figsize=(18, 5))
sns.scatterplot(x='covid_deaths', y='crude_covid_rate', data=df_cleaned, ax=axes[0], color='blue')
axes[0].set_title('Deaths vs Rate')

sns.scatterplot(x='covid_deaths', y='covid_pct_of_total', data=df_cleaned, ax=axes[1], color='orange')
axes[1].set_title('Deaths vs % of Total')

sns.scatterplot(x='crude_covid_rate', y='covid_pct_of_total', data=df_cleaned, ax=axes[2], color='purple')
axes[2].set_title('Rate vs % of Total')

plt.tight_layout()
plt.show()

# ----------- CORRELATION HEATMAP -----------
corr = df_cleaned[required_cols].corr()

plt.figure(figsize=(6, 5))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.tight_layout()
plt.show()

# ----------- BARPLOT: TOP JURISDICTIONS -----------
if 'jurisdiction' in df_cleaned.columns:
    df_cleaned['jurisdiction'] = df_cleaned['jurisdiction'].astype(str)
    top_juris = df_cleaned.groupby('jurisdiction')['covid_deaths'].sum().sort_values(ascending=False).head(10)

    if not top_juris.empty:
        plt.figure(figsize=(10, 6))
        sns.barplot(x=top_juris.values, y=top_juris.index, palette="Reds_r")
        plt.title('Top 10 Jurisdictions by COVID Deaths')
        plt.xlabel("Total Deaths")
        plt.ylabel("Jurisdiction")
        plt.tight_layout()
        plt.show()
    else:
        print("⚠️ Not enough jurisdiction data to plot top 10.")
else:
    print("⚠️ Column 'jurisdiction' not found in the dataset.")

