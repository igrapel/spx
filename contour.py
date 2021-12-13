# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 09:50:16 2021

@author: ilang
"""

import pandas as pd
import matplotlib.pyplot as plt

import numpy as np

import matplotlib.pyplot as plt
import matplotlib.colors as mcol
import matplotlib.cm as cm

from mpl_toolkits import mplot3d
import scipy.interpolate


path_to_csv= "C:\\Users\\ilang\\Desktop\\Projects\\Gamma\\data_cleaned.csv"
df= pd.read_csv(path_to_csv)

print(df)
print("Min", min(df['month_return']))
print("Max", max(df['month_return']))
returns = df['month_return']

print("Minimum Return:")
print(df[df.month_return == df.month_return.min()])
print("Maximum Return:")
print(df[df.month_return == df.month_return.max()])


# Make a user-defined colormap.
cm1 = mcol.LinearSegmentedColormap.from_list("MyCmapName",["r","b"])


#df_subset = df[["gex", "dix", "price"]]

gex = np.array(df[["gex"]])
dix = np.array(df[["dix"]])
price = np.array(df[["month_return"]])

gex_std = np.std(gex)
dix_std = np.std(dix)

print("Gex mean: " + str(np.mean(gex)) + "Gex std: " + str(np.std(gex)))
print("Dix mean: " + str(np.mean(dix)) + "Dix std: " + str(np.std(dix)))
print("Last Month mean: " + str(np.mean(price)) + "Last Month std: " + str(np.std(price)))

x = np.array(df[["dix"]])*100
y = np.array(df[["gex"]])/1000000000
z = np.array(df[["month_return"]])

print("Min", min(z))
print("Max", max(z))

# Set up a regular grid of interpolation points
xi, yi = np.linspace(x.min(), x.max(), 100), np.linspace(y.min(), y.max(), 100)
xi, yi = np.meshgrid(xi, yi)

# Interpolate
rbf = scipy.interpolate.Rbf(x, y, z, function='cubic')
zi = rbf(xi, yi)

fig, ax = plt.subplots()

ax.imshow(zi, vmin=z.min(), vmax=z.max(), origin='lower',
           extent=[x.min(), x.max(), y.min(), y.max()], cmap=cm1)

ax.set_xlabel("DIX")
ax.set_ylabel("GEX")
ax.set_title("E-mini to GEX/DIX")
plt.scatter(x, y, c=z, s=.1, cmap=cm1)
plt.colorbar(label="SPX Dollar Percent Change (last month)")
plt.show()
