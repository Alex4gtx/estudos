import pandas as pd

vendas = {'data': ['10/02/2022', '12/02/2022'], 'valor': [200, 300], 'produto': ['feijão', 'arroz'], 'qtde': [30, 50]}

vendas_df = pd.DataFrame(vendas)

print(vendas_df)