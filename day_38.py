import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# load data set
data = pd.read_csv("experience_salary.csv")

x = data[["YearsExperience"]]
y = data[["Salary"]]

model = LinearRegression()
model.fit(x, y)

data ["PredictedSalary"] = model.predict(x)

print("Model Coefficient (slope)", round(model.coef_[0][0], 2))
print("Model Intercept (slope)", round(model.intercept_[0], 2))

plt.scatter(x, y, color="blue", label="Actual Data")
plt.plot(x, data["PredictedSalary"], color="red", label="Regression line")
plt.xlabel("Years of experience")
plt.ylabel("Salary")
plt.title("Salary vs Experience")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()