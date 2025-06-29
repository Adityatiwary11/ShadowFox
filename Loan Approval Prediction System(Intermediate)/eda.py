import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('data/loan_prediction.csv')

print("\n🔍 First 5 rows:\n", df.head())
print("\n📊 Column info:\n")
print(df.info())

# Check for missing values
print("\n❓ Missing values:\n", df.isnull().sum())

# Visualize target
sns.countplot(data=df, x='Loan_Status')
plt.title("Loan Approval Distribution")
plt.show()

# Correlation heatmap for numerical features
num_df = df.select_dtypes(include=['int64', 'float64'])
sns.heatmap(num_df.corr(), annot=True, cmap='coolwarm')
plt.title("Feature Correlation")
plt.show()
