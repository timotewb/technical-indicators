def doubleExponentialMovingAverageNaN(periodDEMA, data):
    
    #--- Double Exponential Moving Average
    # data: array, time series data e.g. daily close prices
    # periodDEMA: integer, number of periods form time series array to include in calculation
    
    #--- import libraries
    import numpy as np
    
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
    
    p = periodDEMA                               # period value
    s = data[firstNonNan:p+firstNonNan].sum()/p  # the first simple moving average
    k = 2/(p+1)                                  # weighting factor
    d = (2 * p) - 1                              # start of the DEMA

    out = np.zeros(len(data))
    out_ee = np.zeros(len(data))
    out_d = np.zeros(len(data))

    for i in range(len(data)):
        
        if i < firstNonNan+p-1:
            out[i] = np.nan
            out_ee[i] = np.nan
            out_d[i] = np.nan
            
        elif i > lastNonNan:
            out[i] = np.nan
            out_ee[i] = np.nan
            out_d[i] = np.nan
            
        #--- where data item is the p'th item use the SMA
        elif i == p-1+firstNonNan:
            out[i] = s
            out_ee[i] = s
            out_d[i] = s
            
        elif i > p-1+firstNonNan:
            #--- calculate EMA
            out[i] = (k * data[i]) + (1 - k) * out[i-1]
            #--- calcualte ema of ema
            out_ee[i] = (k * out[i]) + (1 - k) * out_ee[i-1]
            #--- calculate dema
            out_d[i] = 2 * out[i] - out_ee[i]
            
    return out_d
