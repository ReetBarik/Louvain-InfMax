# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 17:28:44 2021

@author: reetb
"""

import os
os.chdir('C:/Users/reetb/Desktop/LouvainInfMax/InitialExpts/Plots')

from collections import Counter
import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt
plt.style.use('ggplot')


def read_integers(filename):
    with open(filename) as f:
        return [int(x) for x in f]
    
filename = '../Grappolo/ClusterAssignments/Cit-HepPh.txt_clustInfo'
comm = read_integers(filename)
comm_size = Counter(comm)

#for i in range(len(comm_size)):
#    comm_size[i] = comm_size[i] / len(comm)

seedSetSize = ['10', '15', '20', '25', '50', '75', '100']

contribution = pd.DataFrame(columns=seedSetSize)

for i in seedSetSize:
    seedfile = '../Louvain-Imm/Seq/Cit-HepPh_' + i + '.json'
    
    with open(seedfile) as json_file:
        data = json.load(json_file)

    seeds = list(data[0]['Seeds'])
    
    contr = [0] * len(comm_size)
    
    for s in seeds:
        contr[comm[s - 1]] += 1
        
    contribution[i] = contr
    
l = []
    
for i in range(len(comm_size)):
    l.append(comm_size[i])
    
fig,ax = plt.subplots()

ax.plot(l)
ax.set_xlabel('Community ID')
ax.set_ylabel('Community Size')
ax.set_title('cit-HepPh: n = 34,546, m = 421,578')
plt.savefig('cit-HepPh_CommunitySize.png', dpi = 500)

    
    

    
    