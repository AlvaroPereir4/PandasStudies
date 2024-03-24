# %%

import pandas as pd

# %%
#.read_csv - é um metodo do pandas
df_customers = pd.read_csv("../data/customers.csv", sep=";")
df_customers

#%%
# o comando shape quando for sobre um csv, ele informa 2 valores. as linhas e colunas.
df_customers.shape
# %%
df_customers.info(memory_usage='deep')

# %%
# É bem importante, o describe, para ter a informação do type dos elementos
df_customers["Points"].describe()

# %%
# forma direta de fazer uma diação de valor em todos os elementos.
df_customers['Points'] > 1000
 
# %%
# modelo exemplar de um filtro em pandas.
condicao = df_customers["Points"] > 1000
df_customers[condicao]

# %%
condicao = df_customers["Points"] == df_customers["Points"].max()
df_customers[condicao]

# %%
# padrão comum de filtro
condicao = df_customers["Points"] == df_customers["Points"].max()
df_maior = df_customers[condicao]
df_maior["Name"].iloc[0]


# %%
# Qnd vc usa o ".copy" vc cria um novo objeto, pode ser tanto do filtro quanto
# do data frame principal.
# Isso é perfeito para manter o dataframe original integro e sem alterações.
condicao = (df_customers["Points"] >= 1000) & (df_customers["Points"] <= 2000)
df_1000_2000 = df_customers[condicao].copy()


# %%
df_1000_2000["Points"] = df_1000_2000["Points"] + 1000
df_1000_2000
# %%
df_customers

# %%
# como selecionar colunas
df_customers[["UUID", "Name"]]

# %%
# .columns, ele seleciona as colunas **mas não é tipo LISTA
# .tolist é um metodo q ele cria uma lista dos elementos selecionados.
# .sort() - 
colunas = df_customers.columns.tolist()
colunas.sort()

df_customers = df_customers[colunas]
df_customers

# %%
# INFORMAÇÃO
# Quando renomeamos, o sistema cria um novo Dataframe com as alterações.
# O Dataframe principal continua do mesmo jeito.

df_customers = df_customers.rename(columns={"Name": "Nome",
                                            "Points": "Pontos"})

df_customers

# %%
# É uma outra forma de alterar 
# Mas utilizando o INPLACE, 
df_customers.rename(columns={"UUID":"Id"}, inplace=True)
df_customers