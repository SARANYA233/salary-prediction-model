import joblib
model = joblib.load('salary-predict-model.pk1')

exp = float(input("Enter years of experience: "))
output = model.predict([[exp]])
print("Your Salary :: ", output)
