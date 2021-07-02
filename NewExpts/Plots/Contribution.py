# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 17:28:44 2021

@author: reetb
"""

import os
os.chdir('C:/Users/reetb/Desktop/Louvain-InfMax/InitialExpts/Plots')

from collections import Counter
import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt
plt.style.use('ggplot')


def read_integers(filename):
    with open(filename) as f:
        return [int(x) for x in f]
    
filename = '../METIS/cnr-2000.mtx_64'
comm = read_integers(filename)
comm_size = Counter(comm)

#for i in range(len(comm_size)):
#    comm_size[i] = comm_size[i] / len(comm)

seedSetSize = ['10', '15', '20', '25', '50', '75', '100']

contribution = pd.DataFrame(columns=seedSetSize)

for i in seedSetSize:
    seedfile = '../Louvain-Imm/Seq/Metis/Cit-HepPh/Cit-HepPh_64_' + i + '.json'
    
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

ax.plot(l, marker='o', alpha=0.5)
ax.set_xlabel('Partition ID')
ax.set_ylabel('Partition Size (#nodes)')
ax.set_title('CNR: n = 325K, m = 3.2M, mod = 0.93')
plt.savefig('CNR_PartitionNodeSize.png', dpi = 500)

#ax.set_title('cit-HepTh: n = 27,770, m = 352,807')
#plt.savefig('cit-HepTh_PartitionNodeSize.png', dpi = 500)


#################################################################################################

partition_size = [0] * len(comm_size) 

edgelist = '../../ripples/cnr-2000.mtx'

df = pd.read_csv(edgelist, sep = ' ', header = None)

for i in range(len(df)):
    source = df[0][i] - 1
    destination = df[1][i] - 1
    
    partition_size[comm[source]] += 1
    partition_size[comm[destination]] += 1
    
fig,ax = plt.subplots()

ax.plot(partition_size, marker='o', alpha=0.5)
ax.set_xlabel('Partition ID')
ax.set_ylabel('Partition Size (#edges)')
ax.set_title('CNR: n = 325K, m = 3.2M, mod = 0.93')
plt.savefig('CNR_PartitionEdgeSize.png', dpi = 500)
#ax.set_title('cit-HepTh: n = 27,770, m = 352,807')
#plt.savefig('cit-HepTh_PartitionEdgeSize.png', dpi = 500)
    
    
    

    
    