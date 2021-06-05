# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 15:34:44 2021

@author: reetb
"""

import os
os.chdir('C:\\Users\\reetb\\Desktop\\Louvain-InfMax\\InitialExpts\\Input')
import networkx as nx


filename = 'Cit-HepTh.txt'

G = nx.read_edgelist(filename, nodetype = int)

d = nx.to_dict_of_lists(G)

graphfile = open(filename + '.graph', 'w')

graphfile.write(str(len(d)) + ' ' + str(len(G.edges())) + '\n')

for i in range(1, len(d) + 1):
    print(i)
    for j in range(len(d[i])):
        if (j == 0):
            graphfile.write(str(d[i][j]))
        else:
            graphfile.write(' ' + str(d[i][j]))
            
    graphfile.write('\n')