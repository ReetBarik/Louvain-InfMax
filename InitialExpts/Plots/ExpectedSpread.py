# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 15:49:37 2021

@author: reetb
"""

import os
os.chdir('C:/Users/reetb/Desktop/Louvain-InfMax/InitialExpts/Plots')

import matplotlib.pyplot as plt
plt.style.use('ggplot')
import statistics
import numpy as np
import json

def expectedSpread(filename):
    with open(filename) as json_file:
        data = json.load(json_file)
    l = []
    
    for i in list(data[0]['Simulations']):
        l.append(i[0])
        
    return statistics.mean(l), statistics.stdev(l)

th_imm_10 = [13547, 13550, 13666, 13605, 13726]
th_imm_15 = [13831, 14156, 13947, 13904, 13761]
th_imm_20 = [14328, 14285, 14051, 14035, 14193]
th_imm_25 = [14348, 14055, 14551, 14446, 14194]
th_imm_50 = [14905, 15152, 14945, 14666, 14868]
th_imm_75 = [15145, 15419, 15369, 15324, 15197]
th_imm_100 = [15749, 15827, 15602, 15604, 15750]

th_louvain_imm_10 = [12969, 12623, 12851, 12912, 13062]
th_louvain_imm_15 = [13274, 13477, 13172, 13274, 13290]
th_louvain_imm_20 = [13666, 13476, 13625, 13512, 13477]
th_louvain_imm_25 = [13630, 13621, 13851, 13577, 13472]
th_louvain_imm_50 = [13440, 13596, 13600, 13583, 13690]
th_louvain_imm_75 = [13737, 13639, 13845, 13568, 13260]
th_louvain_imm_100 = [13801, 13808, 13577, 13581, 13776]


ph_imm_10 = [17526, 17742, 17749, 17798, 17588]
ph_imm_15 = [17904, 17996, 17886, 18143, 18207]
ph_imm_20 = [18387, 18183, 18377, 18458, 18381]
ph_imm_25 = [18586, 18725, 18446, 18524, 18438]
ph_imm_50 = [19155, 19160, 19422, 19332, 19295]
ph_imm_75 = [19790, 19873, 19730, 19745, 19587]
ph_imm_100 = [20152, 20149, 20108, 20268, 19993]

ph_louvain_imm_10 = [16923, 17210, 17395, 17429, 17122]
ph_louvain_imm_15 = [17504, 17409, 17408, 17682, 17379]
ph_louvain_imm_20 = [17716, 17283, 17466, 17747, 17640]
ph_louvain_imm_25 = [17628, 17340, 17405, 17855, 17658]
ph_louvain_imm_50 = [17470, 17660, 17593, 17583, 17376]
ph_louvain_imm_75 = [17294, 17059, 17603, 17449, 17819]
ph_louvain_imm_100 = [18688, 18604, 18822, 18636, 18397]

choice = 2

y1 = []
e1 = []
y2 = []
e2 = []
filename = ''

if (choice == 1): #1 for Ph 2 for Th
    
    filename = '../Simulator/Louvain-Imm/Seq/Metis/Cit-HepPh/Cit-HepPh_'
    
    y1.append(statistics.mean(ph_imm_10))
    e1.append(statistics.stdev(ph_imm_10))
    
    y1.append(statistics.mean(ph_imm_15))
    e1.append(statistics.stdev(ph_imm_15))
    
    y1.append(statistics.mean(ph_imm_20))
    e1.append(statistics.stdev(ph_imm_20))
    
    y1.append(statistics.mean(ph_imm_25))
    e1.append(statistics.stdev(ph_imm_25))
    
    y1.append(statistics.mean(ph_imm_50))
    e1.append(statistics.stdev(ph_imm_50))
    
    y1.append(statistics.mean(ph_imm_75))
    e1.append(statistics.stdev(ph_imm_75))
    
    y1.append(statistics.mean(ph_imm_100))
    e1.append(statistics.stdev(ph_imm_100))
    
    
    y2.append(statistics.mean(ph_louvain_imm_10))
    e2.append(statistics.stdev(ph_louvain_imm_10))
    
    y2.append(statistics.mean(ph_louvain_imm_15))
    e2.append(statistics.stdev(ph_louvain_imm_15))
    
    y2.append(statistics.mean(ph_louvain_imm_20))
    e2.append(statistics.stdev(ph_louvain_imm_20))
    
    y2.append(statistics.mean(ph_louvain_imm_25))
    e2.append(statistics.stdev(ph_louvain_imm_25))
    
    y2.append(statistics.mean(ph_louvain_imm_50))
    e2.append(statistics.stdev(ph_louvain_imm_50))
    
    y2.append(statistics.mean(ph_louvain_imm_75))
    e2.append(statistics.stdev(ph_louvain_imm_75))
    
    y2.append(statistics.mean(ph_louvain_imm_100))
    e2.append(statistics.stdev(ph_louvain_imm_100))
    
if (choice ==2):
    
    filename = '../Simulator/Louvain-Imm/Seq/Metis/Cit-HepTh/Cit-HepTh_'
    
    y1.append(statistics.mean(th_imm_10))
    e1.append(statistics.stdev(th_imm_10))
    
    y1.append(statistics.mean(th_imm_15))
    e1.append(statistics.stdev(th_imm_15))
    
    y1.append(statistics.mean(th_imm_20))
    e1.append(statistics.stdev(th_imm_20))
    
    y1.append(statistics.mean(th_imm_25))
    e1.append(statistics.stdev(th_imm_25))
    
    y1.append(statistics.mean(th_imm_50))
    e1.append(statistics.stdev(th_imm_50))
    
    y1.append(statistics.mean(th_imm_75))
    e1.append(statistics.stdev(th_imm_75))
    
    y1.append(statistics.mean(th_imm_100))
    e1.append(statistics.stdev(th_imm_100))
    
    y2.append(statistics.mean(th_louvain_imm_10))
    e2.append(statistics.stdev(th_louvain_imm_10))
    
    y2.append(statistics.mean(th_louvain_imm_15))
    e2.append(statistics.stdev(th_louvain_imm_15))
    
    y2.append(statistics.mean(th_louvain_imm_20))
    e2.append(statistics.stdev(th_louvain_imm_20))
    
    y2.append(statistics.mean(th_louvain_imm_25))
    e2.append(statistics.stdev(th_louvain_imm_25))
    
    y2.append(statistics.mean(th_louvain_imm_50))
    e2.append(statistics.stdev(th_louvain_imm_50))
    
    y2.append(statistics.mean(th_louvain_imm_75))
    e2.append(statistics.stdev(th_louvain_imm_75))
    
    y2.append(statistics.mean(th_louvain_imm_100))
    e2.append(statistics.stdev(th_louvain_imm_100))


fig,ax = plt.subplots()

partition = [2,4,8,16,32,64]
seedSize = [10,15,20,25,50,75,100]

ax.errorbar(seedSize, y1, e1, marker='^', label='Imm')
ax.errorbar(seedSize, y2, e2, marker='o', label='Grappolo')

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
if (choice == 1):
    ax.set_title('cit-HepPh: n = 34,546, m = 421,578')
    plt.savefig('cit-HepPh_ExpectedInfluenceMETIS.png', dpi = 500)
if (choice == 2):
    ax.set_title('cit-HepTh: n = 27,770, m = 352,807')
    plt.savefig('cit-HepTh_ExpectedInfluence.png', dpi = 500)




