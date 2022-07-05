#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#%%
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.colors as colors

mpl.rc('text', usetex=True)
mpl.rc('font', family='serif')
mpl.rc('font', size=10)

#%%
# file with data from the experiment
# Note: header=6 is for NetLogo data

exp1_desc = 'v3w-exp1x'
exp2_desc = 'v3w-exp2x'
exp_desc = 'v3w_exp1x2x'

data1 = pd.read_csv(exp1_desc + '.csv', header=6)
data2 = pd.read_csv(exp2_desc + '.csv', header=6) 

#%%
# select variables for the analysis 
# this depends on the experiment

# variables
# 1st is different for each plot
# 2nd and 3rd vars provide axes for plots
# 4th variable is visualized
# variant 1
# v = ['mobility-prob', 'patch-infection-weight', 'patch-contamination-prob','mean-infected']
# variant 2
v = ['patch-infection-prob', 'mobility-prob', 'patch-contamination-prob','mean-infected']
vl = [r'$w_3$', r'$\mu$', r'$p^{\mathrm{patch}}$']

# selection for plotting

# selected values of the 1st variable
# mrs = [0.1, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.6, 0.75, 0.9, 1]
#var0s = [0.1, 0.2, 0.3, 0.4, 0.5, 0.55, 0.6, 0.7, 0.75]
var0s = [0.15, 0.30, 0.45, 0.75]


# all vaues for 2nd dna 3rd variable
var1s = data1[v[1]].unique()
var2s = data1[v[2]].unique()


df1 = pd.DataFrame(columns=v)
df2 = pd.DataFrame(columns=v)

#%% 
# calculate mean for the presented variable

for v0 in var0s:
    for v1 in var1s:
        for v2 in var2s:
            df1.loc[len(df1.index)] = [
                v0,
                v1,
                v2,
                data1[ (data1[v[0]] == v0) & (data1[v[1]] == v1) & (data1[v[2]] == v2) ] ['%infected'].mean()
            ]

            df2.loc[len(df2.index)] = [
                v0,
                v1,
                v2,
                data2[ (data2[v[0]] == v0) & (data2[v[1]] == v1) & (data2[v[2]] == v2) ] ['%infected'].mean()
            ]
       

#%%

fig = mpl.figure.Figure(figsize=(6,3.5))
levels = [1,10,20,30,40,50,60,70]

for i,v0 in enumerate(var0s):
    axs = fig.add_subplot(241+i);
    plot_data = df1[df1[v[0]] == v0][[v[1], v[2], v[3]]].to_numpy()
    
        
    axs.contour(
        plot_data.T[0].reshape(len(var1s), len(var1s)), 
        plot_data.T[1].reshape(len(var2s), len(var2s)), 
        plot_data.T[2].reshape(21,21),
        levels = levels,
        colors = 'k',linestyles='dotted'
        
    )
    
    im=axs.contourf(
        plot_data.T[0].reshape(len(var1s), len(var1s)), 
        plot_data.T[1].reshape(len(var2s), len(var2s)),  
        plot_data.T[2].reshape(21,21),
        levels = levels,
        cmap = 'Oranges',
        norm=colors.Normalize(vmin=0, vmax=70),        
    )
        
    axs.grid(True,linestyle=':', linewidth=0.5, c='k')
    
    axs.set_title("abcd"[i]+") "+vl[0]+'='+str(v0))
    axs.set_xticks(np.arange(0,1.01,0.2))
    
    axs.set_xticks([0,0.25,0.5,0.75,1.0])
    axs.set_xticklabels([])
  
    axs.set_yticks([0,0.25,0.5,0.75,1.0])
    axs.set_yticklabels([0,0.25,0.5,0.75,1.0])
    

     
    if i not in [0]:
        axs.set_yticklabels([])
    if i == 0:
        axs.set_ylabel(vl[2])

# lower panels (from experiment exp2x)
for i,v0 in enumerate(var0s):
    axs = fig.add_subplot(245+i);
    plot_data = df2[df2[v[0]] == v0][[v[1], v[2], v[3]]].to_numpy()
    
        
    axs.contour(
        plot_data.T[0].reshape(len(var1s), len(var1s)), 
        plot_data.T[1].reshape(len(var2s), len(var2s)), 
        plot_data.T[2].reshape(21,21),
        levels = levels,
        colors = 'k',linestyles='dotted'
        
    )
    
    im=axs.contourf(
        plot_data.T[0].reshape(len(var1s), len(var1s)), 
        plot_data.T[1].reshape(len(var2s), len(var2s)),  
        plot_data.T[2].reshape(21,21),
        levels = levels,
        cmap = 'Oranges',
        norm=colors.Normalize(vmin=0, vmax=70),        
    )
        
    axs.grid(True,linestyle=':', linewidth=0.5, c='k')
    
    axs.set_title("efgh"[i]+") "+vl[0]+'='+str(v0))
    
    axs.set_xticks([0,0.25,0.5,0.75,1.0])
    axs.set_xticklabels([0,0.25,0.5,0.75,1.0])
  
    axs.set_yticks([0,0.25,0.5,0.75,1.0])
    axs.set_yticklabels([0,0.25,0.5,0.75,1.0])
    
    #if i not in [0,3,6]:
    #    axs.set_yticklabels([])
        
    axs.set_xlabel(vl[1])
    if i not in [0]:
        axs.set_yticklabels([])
    
    if i == 0:
        axs.set_ylabel(vl[2])
        

# fig.colorbar(p)


# fig.subplots_adjust(right=0.8)
cbar_ax = fig.add_axes([0.125, 1.035, 0.8, 0.025])
cbar = fig.colorbar(im, cax=cbar_ax, orientation="horizontal")
cbar.set_ticklabels([str(l)+"\%" for l in levels])

fig.tight_layout()
display(fig)

#%%
fig.savefig("plot_"+ exp_desc +".pdf", format="pdf", bbox_inches = 'tight')