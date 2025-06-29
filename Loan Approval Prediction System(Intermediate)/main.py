import joblib
import numpy as np

# Load trained model
model = joblib.load('models/loan_model.pkl')

# Example input [replace these values with real user input]
# Format: [Gender, Married, Dependents, Education, Self_Employed, ApplicantIncome,
#          CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History, Property_Area]

sample = np.array([[1, 1, 0, 1, 0, 5000, 2000, 150, 360, 1, 2]])  # shape = (1, 11)

result = model.predict(sample)
print("\n🎯 Prediction:", "✅ Loan Approved" if result[0] == 1 else "❌ Loan Rejected")
