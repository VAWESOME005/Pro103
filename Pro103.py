import pandas as pd
import plotly.express as px

df = pd.read_csv("projectData.csv")
fig = px.scatter(df, x = "date", y = "country", size = "cases", size_max = 30,
color = 'country')
fig.show()

