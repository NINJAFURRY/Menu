import numpy as np
import pandas as pd
ff=input("Enter the location of .csv file-->")
data=pd.read_csv(ff)
x=data['YearsExperience']
y=data['Salary']
print(data)
from sklearn.linear_model import LinearRegression
model = LinearRegression()
x=x.values.reshape(-1,1)
model.fit(x,y)

arr=int(input('Enter your exprience-->'))
#print(arr)
v=np.array(arr)
newarr=v.reshape(-1,1)
#print(newarr)

pp=model.predict(newarr)
#print(pp)
b=model.intercept_
print(f"Your Baised of this model is {b}")
c=model.coef_
print(f"Your Weight of this model is {c}")
y = b+(c*newarr)
print(y)
print(f"Estimated salary would be {y}")


