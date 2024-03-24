# %%

import pandas as pd
df = pd.read_excel("../data/transactions.xlsx")

# %%

df_last = (df.sort_values("DtTransaction", ascending=False)
             .drop_duplicates(subset=['IdCustomer'], keep='first'))
# subset=identificador de qual é a coluna
# keep é a condição do que vai continuar

# o comando .nunique testa quantos valores tem em uma series que são unicos

df_last['IdCustomer'].nunique()

# %%

condicao = df['IdCustomer'] == '5f8fcbe0-6014-43f8-8b83-38cf2f4887b3'
df[condicao]

# %%

df_last[df_last['IdCustomer'] == '5f8fcbe0-6014-43f8-8b83-38cf2f4887b3']