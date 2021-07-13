# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 12:01:02 2021

@author: reetb
"""

import os
os.chdir('C:/Users/reetb/Desktop/Louvain-InfMax/CommInvestigate')

import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np
import json

input = 'soc-Epinions1.txt'

def read_integers(filename):
    with open(filename) as f:
        return [int(x) for x in f]
    
comm = read_integers('../NewExpts/Grappolo/ClusterAssignments/' + input + '_clustInfo')
    
comm_size = Counter(comm)

seedfile = 'Seeds/' + input + '_imm_100.json'

with open(seedfile) as json_file:
    data = json.load(json_file)
    
seeds = list(data[0]['Seeds']) 

seed_comm_size = np.zeros(len(comm_size))

for s in seeds:
    c = comm[s]
    seed_comm_size[c] += 1
    
    
global_comm_size = np.zeros(len(comm_size))

for i in range(len(comm_size)):
    global_comm_size[i] += comm_size[i]


seed_comm_size = seed_comm_size / 100

global_comm_size = global_comm_size / len(comm)

df = pd.DataFrame({'seed': seed_comm_size,'comm': global_comm_size})

df.to_csv(input + '.csv', sep = ',', index = False) 

fig, ax = plt.subplots()

ax.plot(seed_comm_size, color = 'red', label = 'Seeds (IMM)')

ax.plot(global_comm_size, color = 'blue', alpha = 0.6, label = 'Communities')

ax.legend()
ax.set_xlabel('No. Communities')
ax.set_ylabel('% Belongingness')
ax.set_title('BerkStan: n = 685K, m = 7.6M, mod = 0.94')

plt.savefig('BerkStan_Comm.png', dpi = 500)












