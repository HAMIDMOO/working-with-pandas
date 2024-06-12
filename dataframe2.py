import pandas as pd
import numpy as np


data={"ali":[18, 14.25, 14, 17], "mohammad":[12, 15, 13, 15], "reza":[19, 20, 18, 17]}
y = pd.DataFrame(data,index=["fizic", "chemistry", "math", "literature"] )


print("mean: ",y.loc[:, 'ali'].mean())
print("mean: ",y.loc[:, 'mohammad'].mean())
print("mean: ",y.loc[:, 'reza'].mean())
print("---------------------")

print("median: ",y.loc[:, 'ali'].median())
print("median: ",y.loc[:, 'mohammad'].median())
print("median: ",y.loc[:, 'reza'].median())

print("---------------------")

print("mode", y.loc[:, 'ali'].mode())
print("mode",y.loc[:, 'mohammad'].mode())
print("mode",y.loc[:, 'reza'].mode())

print("---------------------")


correlation_matrix= y.corr()
print(correlation_matrix)





