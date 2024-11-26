
#* ---------- Matplotlib ----------------------------

#? we import the pyplot module from matplotlib, and refer to it as plt in our code.
#? This is a common alias, most things will say "as plt"
import matplotlib.pyplot as plt

#? optional - matplotlib can have stylesheets applied to it to add formatting to a plot all in one go. The most used is ggplot, though there are many others:
#? https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html 

plt.style.use('ggplot')

#? Our aim is to visualise some of the information we took from the staff overflow developer survey. 
#? As these are changes over time, a line graph would be a good plot to produce. 

#? We can store the different axis information in any kind of collection - for now we'll use a list. 

#? The years we are tracking - these will make up our x-axis
years = [2018, 2019, 2020, 2021, 2022, 2023]

#? The languages we are tracking. We can plot all of these on the same graph to help compare them. 
python_position = [7, 4, 4, 3, 4, 3]
javascript_position = [1, 1, 1, 1, 1, 1]
sql_position = [4, 3, 3, 4, 3, 4]
typescript_position = [12, 10, 9, 7, 5, 5]

#? When we create a plot, Matplotlib generates a "figure" object. 
#? A figure acts as the container for all elements of the plot (axes, labels, titles, etc.). 
#? By default, all plots are added to the current active figure unless a new figure is explicitly created.

#? Some of these plots have been customised - we've added labels to them to help with creating a legend, and some plots have linestyles on them
#? This can help identify the lines when colour can't be relied on. 

plt.plot(years, python_position, label = "Python")
plt.plot(years, javascript_position, label = "JavaScript", linestyle = "dashed")
plt.plot(years, sql_position, label = "SQL", linestyle = "dotted")
plt.plot(years, typescript_position, label = "TypeScript", linestyle="dashdot")


#? We can use these methods to add features to the active figure. They are well named and readable!

plt.title("Python Rankings in Stack Overflow Survey")
plt.xlabel("Year")
plt.ylabel("Position in Survey")

#? Unusually, because of the theme of our plot, we need to flip our y axis so the largest number is at the bottom. This will show languages moving up or down the rankings in the orientation we expect!
plt.ylim(bottom=13, top = 0)

#? Because we have many observations on one plot, a legend can help identify the different lines used on the plot. Without it, we wouldn't know which line was which!
plt.legend()

#? The last thing you do is plt.show() - this instructs matplotlib to follow your instructions and draw the chart, and then show you the result. After it has done this, it wipes the chart! 
plt.show()
