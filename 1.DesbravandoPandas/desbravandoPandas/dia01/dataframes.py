# %%
import pandas as pd
# %%

data = {
    "nome":["teo", "nah", "lara", "maria"],
    "sobrenome": ["calvo", "ataide", "calvo", "calvo"],
    "idade": [31, 32, 31, 2]
}

#%%
data["idade"][0]

# %%
df = pd.DataFrame(data)
df
#%%
df["idade"].iloc[0]

# %%
df['sobrenome'].iloc[0]

# %%
# o nome das colunas se torna indice da serie
df.iloc[0]

# %%
df['idade']

# %%

df.index=[3,2,1,0]
df
# %%
df["idade"][0]

# %%
df.index

# %%
df.columns

# %%
# o metodo é info mt importante p ter informações mais completas
# o "memory_usage='deep'" é para uma informação mais exata do uso de memoria
df.info(memory_usage='deep')

# %%
# dtypes é um atributo que informa o tipo de objeto de cada elemento
df.dtypes

#%%
# metodo que é utilizado para resumir algumas informações estatisticas
df.describe()

# %%

df['peso'] = [80, 53, 65, 14]

sumario = df.describe()

sumario['peso']['mean']

# %%
# o comando head informa as 2 primeiras linhas do df
df.head(2)

# %%
# o tail informa as duas ultimas linhas do df
df.tail(2)
# %%
