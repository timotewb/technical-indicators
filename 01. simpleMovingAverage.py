def simpleMovingAverage(periodSMA, data):
    
    #--- Simple Moving Average
    # data: array of percentage change values in decimals
    # periodSMA: integer, number of periods form time series array to include in calculation
    
    #--- import libraries
    import numpy as np
    
    #--- define variables
    n = periodSMA
    
    #--- calculate SMA
    ret = np.cumsum(data, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    ret = ret[n - 1:] / n
    
    #--- return array of number the same length as the input
    return np.append(np.zeros(n-1) + np.nan, ret)
