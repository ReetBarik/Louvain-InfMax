# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 15:30:49 2021

@author: reetb
"""

import os
os.chdir('C:/Users/reetb/Desktop/Louvain-InfMax/NewExpts/Plots')

import matplotlib.pyplot as plt
plt.style.use('ggplot')

import pandas as pd

index = ['10', '15', '20', '25', '50', '75', '100']

th_imm = [21583.9, 28431.9, 34128.2, 40851.9, 68779.6, 94326.7, 120949]
th_grappolo = [172172, 229694, 263800, 291804, 465332, 563120, 670075]
th_metis_4 = [27677, 32239.7, 41193.1, 45251.9, 67066.9, 86603.3, 109224]
th_metis_16 = [7941.29, 7966.33, 10201.9, 10075.3, 13542.3, 15679.6, 18982.1]
th_metis_64 = [7616.64, 7574.11, 7925.11, 7496.6, 7731.6, 7571.6, 7950.87]


ph_imm = [1512.1, 1940.98, 2348.83, 2747.24, 4301.17, 5866.68, 7476.85]
ph_grappolo = [4696.57, 5503.51, 6582.36, 6730.96, 17637, 20451.1, 27688.7]
ph_metis_4 = [4905.42, 6258.67, 7520.98, 8707.05, 13883.6, 18654.2, 23271.5]
ph_metis_16 = [1854.48, 2384, 2854.88, 3440.56, 5911.17, 8393.6, 10914.7]
ph_metis_64 = [10324.2, 13436.5, 19202.2, 19728.4, 37939.2, 60402.1, 87918.4]

df = pd.DataFrame({'imm': th_imm, 'metis-4': th_metis_4, 'metis-16': th_metis_16, 'metis-64': th_metis_64}, index=index)
df = df / 1000

ax = df.plot.bar(rot=0)
ax.set_xlabel('No. Seeds')
ax.set_ylabel('Time (in s)')
ax.set_title('BerkStan: n = 685K, m = 7.6M, mod = 0.94')
plt.savefig('BerkStan_TimeAdjusted.png', dpi = 500)


df = pd.DataFrame({'imm': ph_imm,'grappolo': ph_grappolo, 'metis-4': ph_metis_4, 'metis-16': ph_metis_16, 'metis-64': ph_metis_64}, index=index)
df = df / 1000

ax = df.plot.bar(rot=0)
ax.set_xlabel('No. Seeds')
ax.set_ylabel('Time (in s)')
ax.set_title('cit-HepPh: n = 34K, m = 421K, mod = 0.72')
plt.savefig('HepPh_Time.png', dpi = 500)
