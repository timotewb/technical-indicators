def exponentialMovingAverage(periodEMA, data):
    
    #--- Exponential Moving Average
    # data: array, time series data e.g. daily close prices
    # periodEMA: integer, number of periods form time series array to include in calculation
    
    #--- import libraries
    import numpy as np
    
    #--- define variables
    p = periodEMA               # period value form self
    s = data[:p].sum()/p        # the first simple moving average
    m = 2/(p+1)                 # weighting factor

    #--- define output array
    out = np.zeros(len(data))

    #--- calculate EMA
    for i in range(len(data)):
        #--- where data item is the p'th item, use the SMA
        if i == p-1:
            out[i] = s
        elif i > p-1:
            #--- the EMA calculation
            out[i] = ((data[i] - out[i-1]) * m) + out[i-1]
            #--- mathematically equivalent
            #    out[i] = m * data[i] + (1-m) * out[i-1]
        elif i < p-1:
            out[i] = np.nan

    return out
