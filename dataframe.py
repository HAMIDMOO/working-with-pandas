import pandas as pd


data={"ali":[18, 14.25, 14, 17], "mohammad":[12, 15, 13, 15], "reza":[19, 20, 18, 17]}
y = pd.DataFrame(data,index=["fizic", "chemistry", "math", "literature"] )
y.to_excel("grades.xlsx")

