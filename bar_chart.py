import pandas as pd
import matplotlib.pyplot as plt 

plt.style.use('ggplot')

df = pd.DataFrame({
    "Locations" : [
    "Twitter",
    "Facebook",
    "LinkedIn",
    "Indeed",
    "Instagram"
],
    "Responses" : [3,11,16,13,2],
})

df = df.sort_values("Responses")
bar_colours = ["red" if x==df["Responses"].max() else "blue" for x in df["Responses"]]

plt.bar("Locations", "Responses", data = df, color=bar_colours)
plt.title("Return from Job Posting by Locations")
plt.xlabel("Advert Location")
plt.ylabel("Applications Received")
plt.show()

# bar_colours = []

# for x in df["Responses"]:
#     if x == df["Responses"].max():
#         bar_colours.append("red")
#     else:
#         bar_colours.append("blue")