#coding:utf-8
#This is the class for Diebold-Mariano test

import numpy as np
from scipy.stats import norm

#The inputs are two error lists (or array). The outputs are the confidence that these two models have obvious performance discrepancy
#The lengths of the inputs should match. In addition, the length should be more than 1
def DM_test(a,b):
    a=np.array(a)
    b=np.array(b)
    a=a.astype(np.float64)
    b=b.astype(np.float64)
    if len(a.shape)!=1 or len(b.shape)!=1:
        raise Exception('The inputs must be two 1D lists or arraries')
    elif a.shape[0]!=b.shape[0]:
        raise Exception('The lengths of the two inputs do not match')
    elif a.shape[0]==1:
        raise Exception('The length of the input should be more than 1')

    d=a-b
    d_mean=np.abs(np.mean(d))
    d_std=np.std(d-d_mean)
    if d_std==0:
        DM=1e10
    else:
        DM=d_mean/d_std
    confidence=norm(0,1).cdf(abs(DM))
    return confidence

