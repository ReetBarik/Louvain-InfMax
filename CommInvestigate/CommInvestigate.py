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

input = 'BerkStan.txt'

def read_integers(filename):
    with open(filename) as f:
        return [int(x) for x in f]
    
comm = read_integers('../NewExpts/Grappolo/ClusterAssignments/' + input + '_clustInfo')
    
comm_size = Counter(comm)

comm_size = dict(sorted(comm_size.items(), key=lambda item: item[1]))

seedfile = 'Seeds/' + input + '_grappolo_100.json'

with open(seedfile) as json_file:
    data = json.load(json_file)
    
seeds = list(data[0]['Seeds']) 

seed_comm = np.zeros(len(comm_size))

for s in seeds:
    c = comm[s]
    seed_comm[c] += 1
    
    
global_comm_size = []
seed_comm_size = []

for i in comm_size:
    global_comm_size.append(comm_size[i])
    seed_comm_size.append(seed_comm[i])

#seed_comm_size = seed_comm_size / 100
#
#global_comm_size = global_comm_size / len(comm)

df = pd.DataFrame({'seed': seed_comm_size,'comm': global_comm_size})

df.to_csv(input + '.csv', sep = ',', index = False) 

fig, ax = plt.subplots()

ax.plot(global_comm_size, marker = 'o', alpha = 0.4, markersize = 3, color = 'blue')
ax2 = ax.twinx()
ax2.plot(seed_comm_size, marker = 'o', alpha = 0.2, markersize = 2, color = 'red')

#ax.legend()
fig.text(0.3, 0.90, 'Community Size (left y axis)', c = 'blue', ha='center')
fig.text(0.5, 0.96, 'BerkStan: n = 685K, m = 7.6M, mod = 0.94, #comm = ' + str(len(global_comm_size)), ha='center')
fig.text(0.5, 0.90, 'vs', ha='center')
fig.text(0.725, 0.90, '#L-IMM seeds in Comm (Right y axis)', c = 'red', ha='center')
fig.text(0.5, 0.03, 'Communities sorted acc. size', ha='center')

plt.savefig('BerkStan_Comm_Grappolo.png', dpi = 500)












