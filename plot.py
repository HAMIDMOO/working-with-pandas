import matplotlib.pyplot as plt
import numpy as np

labels= ["physics", "chemistry", "math", "literature", "english", "islam", "sport"]

Grade_reza=[13, 19, 15, 17, 14, 14, 19]
Grade_zahra=[19, 17, 15, 18, 18.5, 17, 18]

x= np.arange(len(labels))

width= 0.35

fig, ax= plt.subplots()

ax.bar(x-width/2, Grade_reza, width, label="Grade_reza")
ax.bar(x+width/2, Grade_zahra, width, label="Grade_zahra")

ax.set_ylabel('Grades')
ax.set_title('Students Grades by Subject')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
plt.show()
