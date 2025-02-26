import pandas as pd

# Load a messy dataset
data = {
    'Name': ['Alice', 'Bob', None, 'David', 'Eve'],
    'Age': [25, None, 22, 35, None],
    'Score': [85, 90, None, 88, 79],
    'Join_Date': ['2023-01-15', '15/01/2023', None, '2023-01-17', 'January 18, 2023']
}
df = pd.DataFrame(data)

# Step 1: Handle missing values
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Score'].fillna(0, inplace=True)
df.dropna(subset=['Name'], inplace=True)

# Step 2: Standardize date formats
df['Join_Date'] = pd.to_datetime(df['Join_Date'], errors='coerce')

# Step 3: Remove duplicates
df.drop_duplicates(inplace=True)

print("Cleaned Dataset:")
print(df)