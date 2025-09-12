import pandas as pd

df = pd.read_csv('dados.csv')

# Método 1: Remover linhas com NaN
new_df_drop = df.dropna()  # Remove linhas com qualquer NaN


# Método 2: Preencher NaN com um valor específico
algum_valor = 0  # Qualquer valor
new_df_fill = df.fillna(algum_valor)  # Substitui NaN por algum_valor


# Método 3: Preencher NaN com a média, moda ou mediana da coluna
new_df_mean = df.fillna(df.mean())  # Substitui NaN pela média da coluna
new_df_mode = df.fillna(df.mode().iloc[0])  # Substitui NaN pela moda da coluna
new_df_median = df.fillna(df.median())  # Substitui NaN pela mediana da coluna

# Método 4: Interpolar valores
new_df_interpolate = df.interpolate()  # Interpola valores faltantes
