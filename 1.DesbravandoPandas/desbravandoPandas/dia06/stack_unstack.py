# %%
# https://www.youtube.com/watch?v=x1MWHD9dfqU
import pandas as pd

df = pd.read_csv("../data/bia_consolidado.csv", sep=";")
df
# %%

df = df.set_index(["cod", "nome", "período"])
df
# %%
#UTILIZAÇÃO DO STACK
# 


df_stack = df.stack().reset_index().rename(columns={"level_3":"Tipos de Homicidios", 0:"Qtde"})
df_stack
# %%
# UTILIZAÇÃO DO UNSTACK

df_unstack = (df_stack.set_index(["cod", 'nome', 'período', 'Tipos de Homicidios']).unstack().reset_index())
df_unstack
# %%
homicidios = df_unstack['Qtde'].columns.tolist()
homicidios

identificadores = df_unstack.columns.droplevel(1).tolist()[:3]

df_unstack.columns = identificadores + homicidios
df_unstack

# %%
