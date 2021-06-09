# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 15:30:49 2021

@author: reetb
"""

import os
os.chdir('C:/Users/reetb/Desktop/Louvain-InfMax/InitialExpts/Plots')

import matplotlib.pyplot as plt
plt.style.use('ggplot')

import pandas as pd

index = ['10', '15', '20', '25', '50', '75', '100']

th_imm = [2372.81, 3130.61, 4022.35, 4677.31, 8079.83, 11494.4, 14572.4]
th_grappolo = [1259.18, 1558.02, 1745.21, 1951.72, 2935.05, 3624.61, 4275.87]
th_metis_2 = [2604.18, 3309.85, 3992.55, 4560.58, 7297.43, 9784.47, 13052.7]
th_metis_4 = [1891.68, 2374.78, 2805.44, 3265.51, 4933.73, 6539.53, 7640.78]
th_metis_8 = [1421.23, 1814.91, 2084.87, 2317.46, 3569.48, 4587.06, 5468.59]
th_metis_16 = [1186.98, 1483.09, 1742.95, 1949.27, 2893.37, 3561.00, 4415.36]
th_metis_32 = [1057.34, 1266.53, 1422.21, 1610.53, 2176.70, 2593.88, 3005.81]
th_metis_64 = [909.13, 1092.21, 1219.77, 1345.4, 1752.85, 2033.76, 2196.86]


ph_imm = [2331.64, 3245.16, 3988.51, 4770.13, 8231, 11415.2, 14924.9]
ph_grappolo = [1714.14, 2097.59, 2467.4, 2735.38, 4213.05, 5553.15, 6528.69]
ph_metis_2 = [2523.75, 3272.83, 3957.73, 4460.90, 6923.70, 9383.13, 11309.90]
ph_metis_4 = [1938.46, 2512.83, 2981.00, 3422.43, 5354.14, 7043.13, 8498.48]
ph_metis_8 = [1742.68, 2205.23, 2495.51, 2836.44, 4503.25, 5612.65, 6840.08]
ph_metis_16 = [1488.57, 1839.47, 2119.4, 2383.60, 3596.59, 4554.13, 5411.39]
ph_metis_32 = [1318.81, 1615.58, 1862.17, 2060.53, 2960.26, 3680.88, 4222.2]
ph_metis_64 = [1204.62, 1450.11, 1637.70, 1799.02, 2394.21, 2848.67, 3156.47]

df = pd.DataFrame({'imm': th_imm,'grappolo': th_grappolo, 'metis-2': th_metis_2, 'metis-4': th_metis_4, 'metis-8': th_metis_8, 'metis-16': th_metis_16, 'metis-32': th_metis_32, 'metis-64': th_metis_64}, index=index)

ax = df.plot.bar(rot=0)
ax.set_xlabel('No. Seeds')
ax.set_ylabel('Time (in ms)')
ax.set_title('cit-HepTh: n = 27,770, m = 352,807')
plt.savefig('cit-HepTh_TimeNew.png', dpi = 500)


df = pd.DataFrame({'imm': ph_imm,'grappolo': ph_grappolo, 'metis-2': ph_metis_2, 'metis-4': ph_metis_4, 'metis-8': ph_metis_8, 'metis-16': ph_metis_16, 'metis-32': ph_metis_32, 'metis-64': ph_metis_64}, index=index)

ax = df.plot.bar(rot=0)
ax.set_xlabel('No. Seeds')
ax.set_ylabel('Time (in ms)')
ax.set_title('cit-HepPh: n = 34,546, m = 421,578')
plt.savefig('cit-HepPh_TimeNew.png', dpi = 500)
