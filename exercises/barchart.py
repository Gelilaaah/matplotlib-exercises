import matplotlib.pyplot as plt
import numpy as np

categories = np.array(["Grains", "Fruits", "Vegetables", "Protein", "Diary", "Sweets"])
values = np.array([4, 3, 2, 5, 3, 1])

plt.barh(categories, values, color = "purple")
plt.title("Daily Consumption")
plt.xlabel("Food")
plt.ylabel("Amount")


plt.show() ## show hulem mecheresha new!!!