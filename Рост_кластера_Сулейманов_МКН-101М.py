# -*- coding: utf-8 -*-
"""Рост кластера.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gODXf0iWwrljO5eiGlDqv1xqm8FlOLf3

Занять в начальный момент времени один из центральных узлов двумерной решетки размерностью 8х8 в качестве зародыша  кластера. На каждом из последующих временных шагов занимать случайным образом один узел решетки, принадлежащий периметру. Написать программу, моделирующую рост кластера в зависимости от «времени». Построить рисунки, отображающие состояние кластера, для 32 последовательных моментов времени. Рассчитать фрактальную размерность полученного кластера.
"""

import numpy as np
import matplotlib.pyplot as plt
from math import log

def fill(cluster, perimeter, cell_x, cell_y, iteration, t):
    n = cluster.shape[0]    
    
    if (iteration > t):        
        return

    plt.figure()
    plt.imshow(cluster)   
         
    print('t = ', iteration, '\n',cluster, '\n')
    #print(len(perimeter))
    
    iteration+=1
    cluster[cell_x,cell_y] = iteration

    if ((cell_x == n-1) or (cell_x == 0) or (cell_y == n-1) or (cell_y == 0)):     
        cluster[cell_x, cell_y] = 99 
        perimeter.append([cell_x, cell_y]) 
    else:                      
        for dir in range(4):            
            if (dir == 0):
                if (cluster[cell_x + 1, cell_y] == 0):                    
                    perimeter.append([cell_x + 1, cell_y])
                    cluster[cell_x + 1, cell_y] = 99                    
            elif (dir == 1):
                if (cluster[cell_x, cell_y + 1] == 0):
                    perimeter.append([cell_x, cell_y + 1])    
                    cluster[cell_x, cell_y + 1] = 99                
            elif (dir == 2):
                if (cluster[cell_x - 1, cell_y] == 0):
                    perimeter.append([cell_x - 1, cell_y])   
                    cluster[cell_x - 1, cell_y] = 99                 
            elif (dir == 3):
                if (cluster[cell_x, cell_y - 1] == 0):
                    perimeter.append([cell_x, cell_y - 1])  
                    cluster[cell_x, cell_y - 1] = 99                  

    next = np.random.randint(len(perimeter))
    next_val = perimeter[next]
    perimeter.remove(perimeter[next])
    fill(cluster, perimeter, next_val[0], next_val[1], iteration, t)

def calc_fract(cluster):
    n = cluster.shape[0]
    l = 1/n
    M = 0
    for i in range(n):
        for j in range(n):
            if (cluster[i,j] > 0) and (cluster[i,j] < 99) :
                M += 1
    d =  log(M)/log(1/l)
    return d

def main():
    seed = [4,4]
    cluster0 = np.zeros((8,8))
    cluster = cluster0.copy()
    perimeter0 = []
    perimeter = perimeter0.copy()

    fill(cluster, perimeter, seed[0], seed[1], 0, 32)

    return cluster, calc_fract(cluster)

result = main()

print('result cluster')
plt.imshow(result[0])

print('фрактальная размерность l =',result[1])

