import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Caminho do arquivo
url = 'https://raw.githubusercontent.com/lucasvoltera/minicurso-python-secompp/main/dados/pokemon_data.csv'

# Leitura do arquivo CSV
df_pokemon = pd.read_csv(url)


# Filtrar os valores de ataque
ataque_pokemon = df_pokemon['Attack'].dropna()

# Criar o histograma
fig, ax = plt.subplots()
ax.hist(ataque_pokemon, bins=20, edgecolor='black')
ax.set_title('Histograma de ataque dos Pokémons')
ax.set_xlabel('Ataque')
ax.set_ylabel('Frequência')
plt.show()