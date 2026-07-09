import matplotlib.pyplot as plt
import numpy as np

categories = ["Freshmen", "Sophomores", "Juniors", "Seniors"]
values = np.array([1590, 1210, 1145, 1013])
colors = ["pink", "purple", "lavender", "blue"]
plt.pie(values, labels = categories, autopct="%1.1f", colors=colors, explode = [0, 0, 0, 0.1], shadow = True)
plt.title("AASTU Student Distribution")

plt.show()