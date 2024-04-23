import numpy as np
import pandas as pd
from web_scrapper import obtener_datos_web

resultados = obtener_datos_web()
array = np.reshape(resultados, (20, 3))

dataset = pd.DataFrame({"País": array[:,0], "Visitas totales (millones)": array[:,1], "Trafico total (%)": array[:,2]})
dataset.to_csv("data/ranking-paises-ia.csv", index=False)