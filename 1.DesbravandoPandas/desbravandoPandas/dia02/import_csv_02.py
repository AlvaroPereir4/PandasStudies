# %%
import pandas as pd

df = pd.read_csv("../data/products.csv",
                 sep=";", #sepração dos dados
                 names=["Id", "Name", "Description"] # nomeação das colunas
                 )

df

# %%

df = df.rename(columns={"Name":"Nome",
                        "Description":"Descricao"})

df
# %%

df.rename(columns={"Name": "Nome",
                   "Description": "Descricao"},
                   inplace=True)

df
# %%
