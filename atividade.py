import pandas as pd
import matplotlib.pyplot as pit

tabela = pd.DataFrame({
    'Idade': [19, 44, 3, 18, 13],
    'Nome': ['Kananda', 'Katarina', 'Maria', 'Kauã', 'Kalil']
    })

pit.hist(tabela['Idade'])
