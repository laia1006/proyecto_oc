import pandas as pd
import matplotlib.pyplot as plt

file_path = "/Users/laiazamora/Desktop/carpeta/proyecto_oc/omar_courtz_dataset.csv"
df = pd.read_csv(file_path)

pink = "#ff69b4"

# Popularity bar chart
plt.figure(figsize=(10,6))
plt.bar(df['track_name'], df['popularity'], color=pink)
plt.xticks(rotation=90)
plt.title('Popularidad por Canción')
plt.xlabel('Canción')
plt.ylabel('Popularidad')
plt.tight_layout()
plt.show()

# Danceability vs Energy scatter
plt.figure(figsize=(8,6))
plt.scatter(df['danceability'], df['energy'], color=pink)
plt.title('Danceability vs Energy')
plt.xlabel('Danceability')
plt.ylabel('Energy')
plt.tight_layout()
plt.show()

# Tempo histogram
plt.figure(figsize=(8,6))
plt.hist(df['tempo'], color=pink)
plt.title('Distribución del Tempo')
plt.xlabel('Tempo')
plt.ylabel('Frecuencia')
plt.tight_layout()
plt.show()
