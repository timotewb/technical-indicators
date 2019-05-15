def triangularMovingAverage(periodSMA, data):
    
    #--- import libraries
    import numpy as np
    
    #--- define variables
    n = periodSMA
        
    #--- calculate SMA
    ret = np.cumsum(data, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    ret = ret[n - 1:] / n
    
    #--- calculate SMA of SMA
    ret_ss = np.cumsum(ret, dtype=float)
    ret_ss[n:] = ret_ss[n:] - ret_ss[:-n]
    ret_ss = ret_ss[n - 1:] / n
    
    #--- return array of number the same length as the input
    return np.append(np.zeros(2*n-2) + np.nan, ret_ss)
