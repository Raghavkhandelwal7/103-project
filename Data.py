import pandas as pd
import plotly.express as px

df=pd.read_csv("data.csv")
fig=px.scatter(df,x="cases",y="date",size="cases",color="country",size_max=10)
fig.show()