import matplotlib.pyplot as plt

x = [2023, 2024, 2025, 2026]
y = [47, 52, 51, 49]
y2 = [23, 154, 143, 79]
y3 = [55, 89, 100, 44]

plt.grid()

plt.plot(x, y, marker=".", markersize = 30, markerfacecolor="pink", markeredgecolor="blue", linestyle="solid", linewidth=4)
plt.plot(x, y2, marker=".", markersize = 30, markerfacecolor="pink", markeredgecolor="blue", linestyle="solid", linewidth=4)
plt.plot(x, y3, marker=".", markersize = 30, markerfacecolor="pink", markeredgecolor="blue", linestyle="solid", linewidth=4)

plt.title("Class Size", fontsize=20, family="Arial", fontweight="bold")
plt.xlabel("Year", fontsize=20, family="Arial")
plt.ylabel("Students", fontsize=20, family="Arial")

plt.tick_params(axis="both", colors = "blue")
plt.xticks(x)
plt.show()