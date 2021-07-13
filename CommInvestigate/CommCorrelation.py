# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 16:21:32 2021

@author: reetb
"""

import os
os.chdir('C:/Users/reetb/Desktop/Louvain-InfMax/CommInvestigate')

import pandas as pd
import matplotlib.pyplot as plt

filenames = ['BerkStan.txt', 'cnr-2000.txt', 'dblp.txt', 'Google.txt', 'HepPh.txt', 'Slashdot0811.txt', 'soc-Epinions1.txt']


for f in filenames:
    file = f + '.csv'
    
    df = pd.read_csv(file)
    
    
    fig, ax = plt.subplots()
    
    ax.scatter(df["seed"], df["comm"]) 
    
    ax.set_xlabel('Seed')
    ax.set_ylabel('Community')
    ax.set_title('Correlation:' + str(df["seed"].corr(df["seed"])))
    plt.savefig(f + '_comm_seed_Correlation.png', dpi = 500)