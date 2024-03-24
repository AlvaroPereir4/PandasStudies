# %%
import pandas as pd

# %%

idades = [30, 42, 90, 34]
idades

# %%
# media -> sum: somar len: qtd de elemento dentro da lista
media = sum(idades) / len(idades)

total = 0
for i in idades:
    total += (media - i)**2
# lembrando que **2 = elevar ao quadrado

variancia = total / (len(idades) - 1) 
print(media)
variancia

# %%
# Transformação para séries Pandas
series_idades = pd.Series(idades)
series_idades

# %%
# Métodos da séries pandas
# Média
series_idades.mean()

# %%
# Variância
series_idades.var()
# %%
# Desvio padrão
series_idades.std()

# %%
# Mediana
series_idades.median()

# %%
# 3o Quartil
series_idades.quantile(0.75)

# %%
# Sumarização
series_idades.describe()

# %%
# Dimensão da série
# O shape tem a funcionalidade de informar quantas linhas minha series tem
# e informa em formato de tupla
series_idades.shape

# %%
# Navegando na lisa
idades[0]

# %%
# Navegando na série
series_idades[3]

# %%
# Alterando index da série
series_idades.index = ['t', 'e', 'o', 'c']
series_idades

# %%
# Navegando nos índices novos
series_idades['t']

# %%
# se vc colocar indice numerico, nem se passar numeros padrões ele vai encontrar
# segue abaixo organizado randomicamente

series_idades.index = [40, 10, 30, 20]
series_idades

# %%
series_idades

# %%
# o "iloc" vai garantir que informe os dados nas posições requeridas
series_idades.iloc[2:4]

# %%
series_idades.iloc[0:2]

# %%
# o "loc" vai garantir informação dos dados pelo indice.
series_idades.loc[40]

# %%
# é possivel dar nomes as series
series_idades.name = 'idades'
series_idades

# %%

series_idades = pd.Series(idades, name="idades")
series_idades
# %%
