import pandas as pd
from sklearn.preprocessing import LabelEncoder

def preprocess_data(file_path):
    df = pd.read_csv(file_path)

    # Drop rows with missing target value
    df.dropna(subset=['Loan_Status'], inplace=True)

    # Fill missing values with mode for categorical and median for numerical
    for col in df.columns:
        if df[col].dtype == 'object':
           df[col] = df[col].fillna(df[col].mode()[0])

        else:
           df[col] = df[col].fillna(df[col].median())


    # Encode categorical variables
    le = LabelEncoder()
    for col in df.select_dtypes(include='object').columns:
        df[col] = le.fit_transform(df[col])

    return df
