import warnings
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_csv("data/ranking-paises-ia.csv")
X = dataset['Visitas totales (millones)']
Y = dataset['País']

warnings.filterwarnings("ignore", "is_categorical_dtype")
warnings.filterwarnings("ignore", "use_inf_as_na")

plt.style.use('ggplot')
fig = plt.figure('Paises lideres de la ia', figsize=(10, 6))
fig.suptitle('Ranking de paises con más usuarios de inteligencia artificial', fontsize=14, fontweight='bold')
plt.xlabel('Visitas totales (millones)')
plt.ylabel('Paises')
sns.barplot(x=X, y=Y, orient='h')
fig.tight_layout()
plt.show()