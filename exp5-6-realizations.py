#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# %%
import pandas as pd
import numpy as np
import matplotlib as mpl

mpl.rc('text', usetex=True)
mpl.rc('font', family='serif')
mpl.rc('font', size=10)


def mav(x, w=100):
    return np.convolve(x, np.ones(w), 'valid') / w


# %%
# file with data from the experiment
# Note: header=6 is for NetLogo data

exp_1_desc = 'v3w-exp5'
exp_2_desc = 'v3w-exp6'
exp_desc = 'v3w-exp5-6'

df_1 = pd.read_csv(exp_1_desc + '.csv', header=6)
df_2 = pd.read_csv(exp_2_desc + '.csv', header=6)
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
v = ['patch-heal-prob', '[step]', '%infected']
vl = [r'$\lambda_c$', 'step', 'percentage of infected']

# selection for plotting

# selected values of the 1st variable
# mrs = [0.1, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.6, 0.75, 0.9, 1]
# var0s = [0, 0.03, 0.07, 0.1, 0.15, 0.2, 0.3, 0.45, 0.5]
# var0s = [0, 0.02, 0.03, 0.07, 0.12, 0.15]
var0s = [0, 0.02, 0.04, 0.06, 0.08, 0.10, 0.12, 0.14, 0.15]

# %%

fig = mpl.figure.Figure(figsize=(6, 4.5))
# levels = [1,10,20,30,40,50,60,70]
skip = 200
for i, v0 in enumerate(var0s):
    axs = fig.add_subplot(331 + i);
    plot_data_1 = df_1[df_1[v[0]] == v0][[v[1], v[2]]].to_numpy()
    plot_data_2 = df_2[df_2[v[0]] == v0][[v[1], v[2]]].to_numpy()

    axs.plot(mav(plot_data_1.T[1]), color='black', linestyle='--', lw=0.75)
    axs.plot(mav(plot_data_2.T[1]), color='green', linestyle='-', lw=0.75)

    axs.set_ylim([0, 100])
    axs.set_xlim([0, 10000])
    axs.set_xticks([0, 3500, 7000, 10000])
    axs.set_yticks([0, 25, 50, 75, 100])
    axs.set_title(vl[0] + "={:.2f}".format(v0))
    axs.grid(True, linestyle=':', linewidth=0.5, c='k')

    if i not in [6, 7, 8]:
        axs.set_xticklabels([])

    if i not in [0, 3, 6]:
        axs.set_yticklabels([])

    if i == 7:
        axs.set_xlabel(vl[1])
    if i == 3:
        axs.set_ylabel(vl[2])

# %%
fig.tight_layout()
display(fig)

# %%
fig.savefig("plot_" + exp_desc + ".pdf", format="pdf", bbox_inches='tight')
