import pandas as pd

def aprobados(notas):
    notas = pd.Series(notas)
    return notas[notas >= 5].sort_values(ascending=False)

notas = {'Dulce':7.5, 'Oscar':9.1, 'gerardo':6, 'Raul': 5, 'Dulce': 9}
print(aprobados(notas))
