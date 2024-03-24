# %%
import pandas as pd

# %%
df = pd.read_csv("../data/customers.csv", sep=';')
df

# %%
# no sort_values, esta da seguinte forma. points -> FALSE (ordem decrescente) & name -> TRUE (ordem alfabetica)
# pq 2 criterios? para ter opção de desempate.
df = (df.sort_values( by=["Points", "Name"],
                      ascending=[False, True] )
        .rename(columns={"Name":"Nome", "Points":"Pontos"}))

df
# %%
