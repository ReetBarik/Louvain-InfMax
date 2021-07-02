# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 15:30:49 2021

@author: reetb
"""

import os
os.chdir('C:/Users/reetb/Desktop/HiPC_Constance/NewExpts/Plots')

import matplotlib.pyplot as plt
plt.style.use('ggplot')

import pandas as pd

index = ['10', '15', '20', '25', '50', '75', '100']

th_imm = [21583.9, 28431.9, 34128.2, 40851.9, 68779.6, 94326.7, 120949]
th_grappolo = [235610, 261712, 355920, 332818, 530397, 593913, 743392]
th_metis_4 = [61912.6, 79988, 96867.7, 112324, 186357, 256151, 319798]
th_metis_16 = [24336.8, 31039.1, 38126.6, 45069.7, 75724.6, 105496, 129107]
th_metis_64 = [55810.3, 84581.6, 101797, 126085, 204407, 292055, 395949]


ph_imm = [1512.1, 1940.98, 2348.83, 2747.24, 4301.17, 5866.68, 7476.85]
ph_grappolo = [4696.57, 5503.51, 6582.36, 6730.96, 17637, 20451.1, 27688.7]
ph_metis_4 = [4905.42, 6258.67, 7520.98, 8707.05, 13883.6, 18654.2, 23271.5]
ph_metis_16 = [1854.48, 2384, 2854.88, 3440.56, 5911.17, 8393.6, 10914.7]
ph_metis_64 = [10324.2, 13436.5, 19202.2, 19728.4, 37939.2, 60402.1, 87918.4]

df = pd.DataFrame({'imm': th_imm,'grappolo': th_grappolo, 'metis-4': th_metis_4, 'metis-16': th_metis_16, 'metis-64': th_metis_64}, index=index)
df = df / 1000

ax = df.plot.bar(rot=0)
ax.set_xlabel('No. Seeds')
ax.set_ylabel('Time (in s)')
ax.set_title('BerkStan: n = 685K, m = 7.6M, mod = 0.94')
plt.savefig('BerkStan_Time.png', dpi = 500)


df = pd.DataFrame({'imm': ph_imm,'grappolo': ph_grappolo, 'metis-4': ph_metis_4, 'metis-16': ph_metis_16, 'metis-64': ph_metis_64}, index=index)
df = df / 1000

ax = df.plot.bar(rot=0)
ax.set_xlabel('No. Seeds')
ax.set_ylabel('Time (in s)')
ax.set_title('cit-HepPh: n = 34K, m = 421K, mod = 0.72')
plt.savefig('HepPh_Time.png', dpi = 500)
