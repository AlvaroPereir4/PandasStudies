# %%
import pandas as pd
import numpy as np

data = {
    "nome":["Téo", "Nah", "Lah", "Mah", "Jo"],
    "idade":[31,32,34,12,np.nan],
    "renda":[np.nan,3245,357,12432,np.nan],
}

df = pd.DataFrame(data)
df
# %%
df["idade"].isna().sum()

# %%
# o comando isna informa em que elementos existe um NotANumber
df.isna().sum()

# %%
df.isna().mean()

# %%
# existe várias maneiras diferentes de se preencher utilizando o comando fillna
# se colocar da seguinte maneira abaixo, ele pega a media dos valores e preenche com os tais

df.fillna({
        "idade": df["idade"].mean(),
        "renda":df["renda"].mean(),
        })

# %%
# o dropna tem a função de remover os NA, somente a função ele remove todas as linhas q possuem NaN

df.dropna(subset=["idade", "renda"], how='any')

# %%
df.dropna(axis=1, thresh=3)