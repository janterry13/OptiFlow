import numpy as np
import pandas as pd
import datetime as dt
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import norm

#######################################
# Define constants for cost functions #
#######################################
#Cost_storage
C = 5
K1 = 1
#Penalization_cost
D = 35
K2 = 5
#Density function
SIGMA = 100
#f_loss
step = 1
#solve_qt
step_s = 10


#Function Cost storage based on units
def cost_storage(qt, st):
  n = qt - st
  if(n <= 0): return 0
  return C*n + K1


#Penalization cost function
def penalization_cost(qt, st):
  n = st - qt
  if(n <= 0): return 0
  return D*n + K2


def f_density(x, mu):  
    aux = norm.pdf(x, mu, SIGMA)
    return aux


#Loss function
def f_loss(qt,st):
    loss = 0

    #first integral
    rng = np.arange(st, qt+step, step)
    for i in rng:
        loss += cost_storage(i,st)*f_density(i,qt)
    
    #second integral
    rng2 = np.arange(0, st+step, step)
    for i in rng2:
        loss += penalization_cost(i,st)*f_density(i,qt)
    
    return loss


#Solve qt
def solve_qt_it(st,it):
    if(st == it): return st
    
    rng = np.arange(st, it, step_s)
    min_loss = np.inf
    min_qt = 0
    for i in rng:
        aux_loss = f_loss(i,st)
        if(aux_loss < min_loss):
            min_loss = aux_loss
            min_qt = i

    return min_qt


#Solve q_t
def general_solution(v_it, v_st):
    v_qt = []
    for i in range(0, len(v_it)):
        v_qt.append(solve_qt_it(v_st[i], v_it[i]))
    
    return v_qt