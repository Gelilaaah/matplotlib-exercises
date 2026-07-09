import matplotlib.pyplot as plt
import numpy as np

x= [0, 1, 1, 2, 2, 3, 4, 5, 5, 6, 7, 8]
y=[45, 51, 49, 68, 65, 77, 81, 89, 88, 90, 93, 96]

x1= [0, 1, 1, 2, 2, 3, 4, 5, 5, 6, 7, 8]
y1=[35, 51, 50, 66, 69, 74, 86, 90, 92, 88, 91, 93]

plt.scatter(x, y, color="blue", label="Class A")
plt.scatter(x1, y1, color="pink", label = "Class B")
plt.xlabel("hours studied")
plt.ylabel("grades")

plt.title("Corelation between grades and study hours")
plt.legend()
plt.show()