# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 15:30:49 2021

@author: reetb
"""

import os
os.chdir('C:/Users/reetb/Desktop/LouvainInfMax/InitialExpts/Plots')

import matplotlib.pyplot as plt
plt.style.use('ggplot')

import pandas as pd

index = ['10', '15', '20', '25', '50', '75', '100']

th_imm = [2372.81, 3130.61, 4022.35, 4677.31, 8079.83, 11494.4, 14572.4]
th_louvain_imm = [1259.18, 1558.02, 1745.21, 1951.72, 2935.05, 3624.61, 4275.87]

ph_imm = [2331.64, 3245.16, 3988.51, 4770.13, 8231, 11415.2, 14924.9]
ph_louvain_imm = [1714.14, 2097.59, 2467.4, 2735.38, 4213.05, 5553.15, 6528.69]

df = pd.DataFrame({'imm': th_imm,'louvain-imm-seq': th_louvain_imm}, index=index)

ax = df.plot.bar(rot=0)
ax.set_xlabel('No. Seeds')
ax.set_ylabel('Time (in ms)')
ax.set_title('cit-HepTh: n = 27,770, m = 352,807')
plt.savefig('cit-HepTh_Time.png', dpi = 500)


df = pd.DataFrame({'imm': ph_imm,'louvain-imm-seq': ph_louvain_imm}, index=index)

ax = df.plot.bar(rot=0)
ax.set_xlabel('No. Seeds')
ax.set_ylabel('Time (in ms)')
ax.set_title('cit-HepPh: n = 34,546, m = 421,578')
plt.savefig('cit-HepPh_Time.png', dpi = 500)
