# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 14:46:23 2021

@author: reetb
"""

import os
os.chdir('C:/Users/reetb/Desktop/Louvain-InfMax/CommInvestigate/SamplingEffort/')

import matplotlib.pyplot as plt

def read_integers(filename):
    with open(filename) as f:
        return [str(x) for x in f]
    
    
filename = 'BerkStan.txt_grappolo_100'

effort = read_integers(filename)

size = {}
theta = {}

for i in range(0, len(effort), 2):
    c = int(effort[i])
    s = str.split(effort[i + 1], ',')
    size[c] = int(s[0])
    theta[c] = int(s[1])
    
size = dict(sorted(size.items(), key=lambda item: item[1]))


y1 = []   # Sorted Size of communities/partitions
y2 = []   # Sampling effort for each community/partitions

for s in size:
    y1.append(size[s])
    y2.append(theta[s])
    
    
fig, ax = plt.subplots()

ax.plot(y1, marker = 'o', alpha = 0.4, markersize = 3, color = 'blue')

ax2 = ax.twinx()

ax2.plot(y2, marker = 'o', alpha = 0.4, markersize = 3, color = 'red')

fig.text(0.3, 0.90, 'Community Size (left y axis)', c = 'blue', ha='center')
fig.text(0.5, 0.96, 'BerkStan: n = 685K, m = 7.6M, mod = 0.94, #comm = ' + str(len(y1)), ha='center')
fig.text(0.5, 0.90, 'vs', ha='center')
fig.text(0.725, 0.90, 'Community Theta (Right y axis)', c = 'red', ha='center')
fig.text(0.5, 0.03, 'Theta IMM = 37541, Theta LouvainIMM = ' + str(sum(y2)), ha='center')
    
plt.savefig(filename + '_CommVTheta.png', dpi = 500)
