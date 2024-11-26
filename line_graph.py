
#* ---------- Matplotlib ----------------------------

#? we import the pyplot module from matplotlib, and refer to it as plt in our code.
#? This is a common alias, most things will say "as plt"
import matplotlib.pyplot as plt

plt.style.use('ggplot')

years = [2018, 2019, 2020, 2021, 2022, 2023]

python_position = [7, 4, 4, 3, 4, 3]
javascript_position = [1, 1, 1, 1, 1, 1]
sql_position = [4, 3, 3, 4, 3, 4]
typescript_position = [12, 10, 9, 7, 5, 5]

plt.plot(years, python_position, label = "Python")
plt.plot(years, javascript_position, label = "JavaScript", linestyle = "dashed")
plt.plot(years, sql_position, label = "SQL", linestyle = "dotted")
plt.plot(years, typescript_position, label = "TypeScript", linestyle="dashdot")
plt.title("Python Rankings in Stack Overflow Survey")
plt.xlabel("Year")
plt.ylabel("Position in Survey")
plt.ylim(bottom=13, top = 0)

# plt.legend(["Python", "JavaScript", "SQL", "TypeScript"])
plt.legend()
plt.show()
