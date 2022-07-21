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

exp_desc = 'exp1-mobility-patch_cont-patch_infect'

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
v = ['patch-infection-prob', 'mobility-prob', 'patch-contamination-prob', 'mean-infected']
vl = [r'$\nu_{3}$', 'mobility', 'patch contamination probability']

# selection for plotting

# selected values of the 1st variable
var0s = [0.05, 0.10, 0.15, 0.25, 0.30, 0.45, 0.55, 0.65, 0.75]

# all values for 2nd dna 3rd variable
var1s = data[v[1]].unique()
var2s = data[v[2]].unique()

df = pd.DataFrame(columns=v)

# %%
# calculate mean for the presented variable

for v0 in var0s:
    for v1 in var1s:
        for v2 in var2s:
            df.loc[len(df.index)] = [
                v0,
                v1,
                v2,
                data[(data[v[0]] == v0) & (data[v[1]] == v1) & (data[v[2]] == v2)]['%infected'].mean()
            ]

# %%

fig = mpl.figure.Figure(figsize=(6, 5.5))
levels = [1, 10, 20, 30, 40, 50, 60, 70, 80]

for i, v0 in enumerate(var0s):
    axs = fig.add_subplot(331 + i);
    plot_data = df[df[v[0]] == v0][[v[1], v[2], v[3]]].to_numpy()

    axs.contour(
        plot_data.T[0].reshape(len(var1s), len(var1s)),
        plot_data.T[1].reshape(len(var2s), len(var2s)),
        plot_data.T[2].reshape(21, 21),
        levels=levels,
        colors='k', linestyles='dotted'
    )

    im = axs.contourf(
        plot_data.T[0].reshape(len(var1s), len(var1s)),
        plot_data.T[1].reshape(len(var2s), len(var2s)),
        plot_data.T[2].reshape(21, 21),
        levels=levels,
        cmap = 'Oranges',
        norm = colors.Normalize(vmin=0, vmax=70),
    )

    axs.set_title('abcdefghi'[i] + ') ' + vl[0] + '=' + str(v0))
    axs.set_xticks(np.arange(0, 1.01, 0.2))

    axs.grid(True, linestyle=':', linewidth=0.5, c='k')

    if i not in [6, 7, 8]:
        axs.set_xticklabels([])

    if i not in [0, 3, 6]:
        axs.set_yticklabels([])

    if i == 7:
        axs.set_xlabel(vl[1])
    if i == 3:
        axs.set_ylabel(vl[2])

cbar_ax = fig.add_axes([0.125, 1.02, 0.8, 0.02])
cbar = fig.colorbar(im, cax=cbar_ax, orientation="horizontal")
cbar.set_ticklabels([str(l) + "\%" for l in levels])

fig.tight_layout()
display(fig)

# %%
fig.savefig("plot_" + exp_desc + ".pdf", format="pdf", bbox_inches='tight')
