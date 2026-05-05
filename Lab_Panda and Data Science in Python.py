# Load the dataset in Python
import pandas as pd

df = pd.read_csv("telco_churn.csv")

print(df.head()) # This shows the first 5 rows
print(df.info())  # This tells you:Number of rows, Data types (int, float, object) and Missing values
print(df.describe()) # This gives the summary statistics (Mean, Min/Max, Standard deviation)
print(df.columns) # This gives columns names

#Handle Missing Values

df = df.dropna() #Removes rows with missing values

df.fillna(0) # Replaces missing values with 0

# Basic Data Analysis

print(df['Churn'].value_counts()) #Count churned customers

print(df.groupby('Churn').mean(numeric_only=True)) #Group by churn

# Filtering Data

high_usage = df[df['Total day minutes'] > 250] # customers with high day minutes
print(high_usage)

# Create New Columns

df['Total charge'] = (
    df['Total day charge'] +
    df['Total eve charge'] +
    df['Total night charge'] +
    df['Total intl charge']
)

# Sorting
df_sorted = df.sort_values(by='Total charge', ascending=False)
print(df_sorted.head())

# output to csv
print(df.to_csv("output.csv"))