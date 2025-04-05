import pandas as pd

# Correct file path using raw string
df = pd.read_csv(r'C:\Users\sps97\Desktop\python-project\Provisional_COVID-19_death_counts__rates__and_percent_of_total_deaths__by_jurisdiction_of_residence.csv')

# Print first 5 rows
print(df.head())
