import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('fatcat.dat', index_col=0, sep=' ')
df.Karli.plot(color='g', marker='o', lw=3.0, label='Karli')
df.Tatze.plot(color='r', marker='o', lw=3.0, label='Tatze')
df.Tiger.plot(color='y', marker='o', lw=3.0, label='Tiger')
df.Schwarze.plot(color='b', marker='o', lw=3.0, label='Schwarze')
plt.ylabel('Gewicht / g')
plt.title('Kalis Kätzlich')
plt.legend()
plt.show()
