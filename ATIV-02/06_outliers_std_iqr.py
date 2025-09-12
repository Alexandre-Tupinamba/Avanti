import pandas as pd

df = pd.DataFrame({'valores': [10, 12, 12, 13, 12, 100, 11, 13, 12, 12, 15]})

# Média e desvio padrão
media = df['valores'].mean()
desvio = df['valores'].std()

# Identificar outliers (limite de 3 desvios)
limite_inferior = media - 3*desvio
limite_superior = media + 3*desvio

outliers = df[(df['valores'] < limite_inferior) | (df['valores'] > limite_superior)]
print("Outliers:\n", outliers)


# IQR 

Q1 = df['valores'].quantile(0.25)
Q3 = df['valores'].quantile(0.75)
IQR = Q3 - Q1

limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

outliers = df[(df['valores'] < limite_inferior) | (df['valores'] > limite_superior)]
print("Outliers:\n", outliers)
