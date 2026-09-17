import pandas as pd
df = pd.read_csv("C:\\Users\\pohiy\\Desktop\\data.csv")

print("Shape:", df.shape)
print("\nColumn names:", df.columns.tolist())
print("\nData types:\n", df.dtypes)
print("\nFirst 5 rows:\n", df.head())

print("Missing values per column:\n", df.isnull().sum())
df = df.dropna()

# Example: Sirf wo rows jahan Calories 300 se zyada hain
filtered_df = df[df['Calories'] > 300]
print(filtered_df)

# Example: Calories per minute ka naya column
df['Calories_per_min'] = df['Calories'] / df['Duration']
print(df.head())

df.to_csv("cleaned_data.csv", index=False)
print("Cleaned file saved!")