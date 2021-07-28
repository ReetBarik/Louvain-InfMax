# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 15:49:37 2021

@author: reetb
"""

import os
os.chdir('C:/Users/reetb/Desktop/Louvain-InfMax/NewExpts/Plots')

import matplotlib.pyplot as plt
plt.style.use('ggplot')
import statistics
import numpy as np
import json

f = 'BerkStan.txt'

def expectedSpread(filename):
    with open(filename) as json_file:
        data = json.load(json_file)
    l = []
    
    for i in list(data[0]['Simulations']):
        l.append(i[0])
        
    return statistics.mean(l), statistics.stdev(l)

fig,ax = plt.subplots()

partition = [4,16,64]
seedSize = [10,15,20,25,50,75,100]

y1 = []
e1 = []
y2 = []
e2 = []

f_imm = '../Simulator/Imm/' + f + '_imm_'
f_grappolo = '../Simulator/Louvain-Imm/Grappolo/' + f + '_grappolo_'

for s in seedSize:
    filename1 = f_imm + str(s) + '.json'
    filename2 = f_grappolo + str(s) + '.json'
    m,std = expectedSpread(filename1)
    y1.append(m)
    e1.append(std)
    m,std = expectedSpread(filename2)
    y2.append(m)
    e2.append(std)

ax.errorbar(seedSize, y1, e1, marker='^', label='Imm')
#ax.errorbar(seedSize, y2, e2, marker='o', label='Grappolo')

filename = '../Simulator/Louvain-Imm/Metis/' + f + '_metis_'

for p in partition:
    y = []
    e = []
    for s in seedSize:
         exptFile = filename + str(p) + '_' + str(s) + '.json'
         m,std = expectedSpread(exptFile)
         y.append(m)
         e.append(std)
    ax.errorbar(seedSize, y, e, marker='o', label='METIS-' + str(p))

ax.legend()
ax.set_xlabel('No. Seeds')
ax.set_ylabel('Expected influence')
ax.set_title('BerkStan: n = 685K, m = 7.6M, mod = 0.94')
plt.savefig('BerkStan_ExpectedInfluenceAdjusted.png', dpi = 500)





