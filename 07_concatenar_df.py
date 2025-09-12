import pandas as pd

df1 = pd.DataFrame({
    "A": [1, 2],
    "B": [3, 4]
})

df2 = pd.DataFrame({
    "A": [5, 6],
    "C": [7, 8]
})


print("\nConcatenando por linhas:\n")
result = pd.concat([df1, df2], axis=0)
print(result)


print("\nConcatenando por colunas:\n")
result2 = pd.concat([df1, df2], axis=1)
print(result2)
