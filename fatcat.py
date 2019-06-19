import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('fatcat.dat', index_col=0, sep=' ')
fig, axes = plt.subplots(nrows=3, ncols=1)

axes[0].set_title('Gewicht absolut')
axes[0].set_ylabel('g')
df.plot(ax=axes[0], marker='o', lw=3.0)
axes[0].set_xlabel('')

axes[1].set_title('Gewichtszuwachs')
axes[1].set_ylabel('g/Tag')
df.diff().plot.bar(ax=axes[1])
axes[1].set_xlabel('')

axes[2].set_title('Milchleistung')
axes[2].set_ylabel('g/Tag')
df.diff().plot.area(ax=axes[2], stacked=True)
fig.suptitle('Kalis Kätzlich', fontsize = 20)
plt.show()
