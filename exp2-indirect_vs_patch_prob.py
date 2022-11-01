#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# %%
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.colors as colors

mpl.rc('text', usetex=True)
mpl.rc('font', family='serif')
mpl.rc('font', size=10)

# %%
# file with data from the experiment
# Note: header=6 is for NetLogo data

exp_desc = 'exp2-indirect_vs_patch_prob'

data = pd.read_csv(exp_desc + '.csv', header=6)

# %%
# select variables for the analysis 
# this depends on the experiment

# variables
# 1st is different for each plot
# 2nd and 3rd vars provide axes for plots
# 4th variable is visualized
# variant 1
# v = ['mobility-prob', 'patch-infection-weight', 'patch-contamination-prob','mean-infected']
# variant 2
v = ['indirect-infection-prob', 'patch-infection-prob', 'mobility-prob', 'patch-contamination-prob', 'mean-infected']
vl = [r'$\nu_{2}$', r'$\nu_{3}$', 'mobility', 'patch contamination probability']

# selection for plotting

# vars 0 and 1 are used to index plots
var0s = [0.3, 0.6, 0.9]
var1s = [0.3, 0.6, 0.9]

# variable 2nd and 3rd are used to inded plot data
var2s = data[v[2]].unique()
var3s = data[v[3]].unique()

df = pd.DataFrame(columns=v)

# %%
# calculate mean for the presented variable

for v0 in var0s:
    for v1 in var1s:
        for v2 in var2s:
          for v3 in var3s:
            df.loc[len(df.index)] = [
                v0,
                v1,
                v2,
                v3,
                data[(data[v[0]] == v0) & (data[v[1]] == v1) & (data[v[2]] == v2) & (data[v[3]] == v3) ]['%infected'].mean()
            ]

# %%

fig = mpl.figure.Figure(figsize=(6, 5.5))
levels = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90]

for i, v0 in enumerate(var0s):
  
  for j, v1 in enumerate(var1s):
    axs = fig.add_subplot(331 + i + 3*j);
    plot_data = df[ (df[v[0]] == v0) & (df[v[1]] == v1) ][[v[2], v[3], v[4]]].to_numpy()


    # first two elements of plot_data correspond to the values of 2nd and 3rd variable
    axs.contour(
        plot_data.T[0].reshape(len(var2s), len(var2s)), 
        plot_data.T[1].reshape(len(var3s), len(var3s)),
        plot_data.T[2].reshape(21, 21),
        levels=levels,
        colors='k', linestyles='dotted', linewidths=0.5
    )

    im = axs.contourf(
        plot_data.T[0].reshape(len(var2s), len(var2s)),
        plot_data.T[1].reshape(len(var3s), len(var3s)),
        plot_data.T[2].reshape(21, 21),
        levels=levels,
        cmap = 'hot_r',
        norm = colors.Normalize(vmin=0, vmax=levels[-1]),
    )

    axs.set_title('abcdefghi'[i+3*j] + ') ' + vl[0] + '=' + str(v0) +', ' + vl[1] + '=' + str(v1))
    axs.set_xticks(np.arange(0, 1.01, 0.2))

    axs.grid(True, linestyle=':', linewidth=0.5, c='k')

    if j not in [2]:
        axs.set_xticklabels([])

    if i not in [0]:
        axs.set_yticklabels([])

    if i == 1 and j == 2:
        axs.set_xlabel(vl[2])
    if i == 0 and j == 1:
        axs.set_ylabel(vl[3])

cbar_ax = fig.add_axes([0.125, 1.02, 0.8, 0.02])
cbar = fig.colorbar(im, cax=cbar_ax, orientation="horizontal")
cbar.set_ticklabels([str(l) + "\%" for l in levels])

fig.tight_layout()
display(fig)


# %%
fName = "plot_" + exp_desc + "_all.pdf"
print("INFO] Saving " + fName)
fig.savefig('plots/'+fName, format="pdf", bbox_inches='tight')
