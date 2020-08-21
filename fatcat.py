import matplotlib.pyplot as plt
import pandas as pd
import os
import shutil

df = pd.read_csv('fatcat.dat', index_col=0, parse_dates=True, sep=' ')

# Increase figure sizes to 10 x 8 inches
fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 10
fig_size[1] = 8
plt.rcParams["figure.figsize"] = fig_size

out_path = 'plots'
if os.path.exists(out_path) and os.path.isdir(out_path):
    shutil.rmtree(out_path)
os.mkdir(out_path)

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
plt.savefig('plots/first_month.png', dpi=300)

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
plt.savefig('plots/first_three_months.png', dpi=300)

# all time weight only
fig_all, axes_all = plt.subplots(nrows=1, ncols=1)
axes_all.set_title('Weight')
axes_all.set_ylabel('g')
df.plot(ax=axes_all, marker='o', lw=2.0)
axes_all.set_xlabel('')
axes_all.grid(True, axis='y')
fig_all.suptitle("All time", fontsize = 20, fontweight='bold')
plt.savefig('plots/all_time.png', dpi=300)

plt.show()
