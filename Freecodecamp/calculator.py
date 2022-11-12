#!/usr/bin/env python
# coding: utf-8

# In[8]:


# import library
import numpy as np

# input list
mylist = list(map(int,input('Enter 9 number only using split with comma \' , \':').strip().split(',')))
matrix = np.array(mylist).reshape(3,3)
mylist

# mean, var, std, max, min, min, sum calculator
mean = [(matrix.mean(axis=0).tolist()), (matrix.mean(axis=1).tolist()),(matrix.flatten().mean())]
var = [(matrix.var(axis=0).tolist()), (matrix.var(axis=1).tolist()),(matrix.flatten().var())]
std = [(matrix.std(axis=0).tolist()), (matrix.std(axis=1).tolist()), (matrix.flatten().std())]
max = [(matrix.max(axis=0).tolist()), (matrix.max(axis=0).tolist()), (matrix.flatten().max())]
min = [(matrix.min(axis=0).tolist()), (matrix.min(axis=1).tolist(), (matrix.flatten().min()))]
s = [(matrix.sum(axis=0).tolist()), (matrix.sum(axis=1).tolist()), (matrix.flatten().sum())]

# rename
calculations = { 'mean': mean,
 'variance': var,
 'standard-deviation':std,
 'maximum':max,
 'minimum':min,
 'sum':s
}
# output
calculations

