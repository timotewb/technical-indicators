def simpleMovingAverageNaN(periodSMA, data):
    
    #--- Simple Moving Average NaN
    # data: array, time series data e.g. daily close prices
    # periodSMA: integer, number of periods form time series array to include in calculation
    
    #--- import libraries
    import numpy as np
    
    #--- define variables
    n = periodSMA
    
    #--- get first non nan index
    for i in range(len(data)):
        
        if np.isnan(data[i]) == False:
            
            firstNonNan = i
            break
    
    #--- get last non nan index            
    for i in reversed(range(len(data))):
        
        if np.isnan(data[i]) == False:
            
            lastNonNan = i
            break
    
    #--- calculate SMA
    ret = np.nancumsum(data, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    ret = ret[n - 1:] / n
    
    #--- return array of number the same length as the input
    ret =  np.append(np.zeros(n-1) + np.nan, ret)
    
    #--- update zeros with nan
    for i in range(len(data)):
        
        if i < firstNonNan+n:
            
            np.put(ret,i,np.nan)
            
        elif i >= lastNonNan:
            
            np.put(ret,i,np.nan)
            
    return ret
