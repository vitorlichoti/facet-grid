import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# KAST = KAST (Kill Assist Survival Traded) significa os fundamentos principais no jogo: matar, sobreviver, dar assistência ou trocar a kill. 

matplotlib.use("TkAgg")

sns.set(style="ticks", color_codes=True)

cs_stats = pd.read_csv('csgo_stats.csv')

graphic_one = sns.FacetGrid(cs_stats, col="country")

g = graphic_one.map(sns.distplot, "kast")

plt.show()
