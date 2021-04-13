"""It is way better to try this code
out on Google Colab or Notebook"""

import seaborn as sns
import matplotlib.pyplot as plt

vuelos = sns.load_dataset("flights")
vuelos = vuelos.pivot("month", "year", "passengers")
ax = sns.heatmap(vuelos)
plt.show()