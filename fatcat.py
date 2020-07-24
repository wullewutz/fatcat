import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('fatcat.dat', index_col=0, parse_dates=True, sep=' ')

# first month
fig_1m, axes_1m = plt.subplots(nrows=2, ncols=1)
axes_1m[0].set_title('Weight')
axes_1m[0].set_ylabel('g')
df['2019-06-09':'2019-07-08'].plot(ax=axes_1m[0], marker='o', lw=2.0)
axes_1m[0].set_xlabel('')
axes_1m[0].grid(True, axis='y')
axes_1m[1].set_title('Weight increase')
axes_1m[1].set_ylabel('g/day')
df['2019-06-09':'2019-07-08'].diff().plot(ax=axes_1m[1], marker='o', lw=2.0)
axes_1m[1].set_xlabel('')
axes_1m[1].grid(True, axis='y')
fig_1m.suptitle("First month", fontsize = 20, fontweight='bold')

# first three months
fig_3m, axes_3m = plt.subplots(nrows=2, ncols=1)
axes_3m[0].set_title('Weight')
axes_3m[0].set_ylabel('g')
df['2019-06-09':'2019-09-02'].plot(ax=axes_3m[0], marker='o', lw=2.0)
axes_3m[0].set_xlabel('')
axes_3m[0].grid(True, axis='y')
axes_3m[1].set_title('Weight increase')
axes_3m[1].set_ylabel('g/day')
df['2019-06-09':'2019-09-02'].diff().plot(ax=axes_3m[1], marker='o', lw=2.0)
axes_3m[1].set_xlabel('')
axes_3m[1].grid(True, axis='y')
fig_3m.suptitle("First three months", fontsize = 20, fontweight='bold')

# all time weight only
fig_all, axes_all = plt.subplots(nrows=1, ncols=1)
axes_all.set_title('Weight')
axes_all.set_ylabel('g')
df.plot(ax=axes_all, marker='o', lw=2.0)
axes_all.set_xlabel('')
axes_all.grid(True, axis='y')
fig_all.suptitle("All time", fontsize = 20, fontweight='bold')

plt.show()
