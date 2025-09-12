import pandas as pd

df = pd.read_csv('dados.csv')

df_filtrado = df.loc[df['column_name'] > 100]

print(df_filtrado.head())