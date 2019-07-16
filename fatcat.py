import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('fatcat.dat', index_col=0, sep=' ')
fig, axes = plt.subplots(nrows=2, ncols=1)

axes[0].set_title('Gewicht absolut')
axes[0].set_ylabel('g')
df.plot(ax=axes[0], marker='o', lw=2.0)
axes[0].set_xlabel('')
axes[0].grid(True, axis='y')

axes[1].set_title('Gewichtszuwachs')
axes[1].set_ylabel('g/Tag')
df.diff().plot(ax=axes[1], marker='o', lw=2.0)
axes[1].set_xlabel('')
axes[1].grid(True, axis='y')

fig.suptitle('Kalis Kätzlich', fontsize = 20, fontweight='bold')
plt.show()
