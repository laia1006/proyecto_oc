from pytrends.request import TrendReq
import pandas as pd

# Añadir delay de 2 segundos entre llamadas
pytrends = TrendReq(hl='es-ES', tz=360, retries=5, backoff_factor=0.5)

artist = "Omar Courtz"

pytrends.build_payload([artist], timeframe='today 12-m')

interest = pytrends.interest_by_region(
    resolution='COUNTRY',
    inc_low_vol=True
)

# Ordenar resultados
print("Países donde Omar Courtz tiene más interés (proxy de escuchas):")
print(interest.sort_values(by=artist, ascending=False).head(20))


#Ahora vamos a hacer un gráfico cone estos resultados:
import matplotlib.pyplot as plt

# Ordenar y quedarnos con el top 10
top_countries = interest.sort_values(by=artist, ascending=False).head(20)

pink = "#ff69b4"

# Crear gráfico de barras
plt.figure(figsize=(12, 7))
plt.barh(top_countries.index, top_countries[artist], color=pink)
plt.xlabel("Interés (Google Trends)")
plt.title(f"Top 20 países donde más se busca '{artist}'")
plt.gca().invert_yaxis()  # Para que el país más alto aparezca arriba
plt.tight_layout()
plt.show()
