# import matplotlib.pyplot as plt
# import mplcursors

# # Sample data
# categories = ['A', 'B', 'C', 'D']
# values = [10, 20, 15, 30]

# fig, ax = plt.subplots()
# bars = ax.bar(categories, values)

# # Add cursor for interactivity
# mplcursors.cursor(bars, hover=True)

# plt.show()

# import plotly.express as px

# # Sample data
# data = {'Category': ['A', 'B', 'C', 'D'], 'Value': [10, 20, 15, 30]}
# fig = px.bar(data, x='Category', y='Value', text='Value')

# fig.update_traces(texttemplate='%{text}', textposition='outside')
# fig.show()