import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
pp=input('Enter your file path .csv format')
data=pd.read_csv(pp)
print(data)
x=data['YearsExperience']
y=data['Salary']
plt.scatter(x,y,alpha=0.5)
plt.plot(x,y,marker="o")
plt.title('Graph of Salary prediction')
plt.show()
