import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
import dash 

# Cargamos los datos
url = "https://ourworldindata.org/grapher/global-vaccination-coverage.csv?v=1&csvType=full&useColumnShortNames=true"
df = pd.read_csv(url)
print(df.describe())
print(df.head())

# limpiar los datos
df = df.dropna(how='all')
df = df.drop_duplicates()
df = df.reset_index(drop=True)

# graficar los datos
# Gráfico paises


fig = px.choropleth(df, locations='Code', 
    color='coverage__antigen_hepb3',
    hover_name='Entity',
    color_continuous_scale='viridis',
    title='Global vaccination coverage')

fig.show()

fig2 = px.cho