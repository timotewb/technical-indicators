def kaufmanAdaptiveMovingAverage(periodKAMA, fastEMA_KAMA, slowestEMA_KAMA, data):
    
    #--- import libraries
    import numpy as np
    import math
    
    #--- define variables
    n = periodKAMA
    f = fastEMA_KAMA
    s = slowestEMA_KAMA
    dataLength = len(data)
    
    change = np.zeros(len(data))
    prev_cur = np.zeros(len(data))
    volatility = np.zeros(len(data))
    
    #--- efficiency ratio
    er = np.zeros(len(data))
    #--- smoothing constant
    sc = np.zeros(len(data))
    #--- kama
    kama = np.zeros(len(data))
        
    #--- calculate efficiency ratio
    for i in range(1, dataLength):
        if i == n:
            prev_cur[i] = math.sqrt((data[i] - data[i-1]) ** 2)
            
            change[i] = math.sqrt((data[i-1] - data[i-n]) ** 2)
            
            #--- first kama value is the sma
            kama[i] = sum(data[i:i+n])/n
            
            volatility[i] = np.nan
            er[i] = np.nan
            sc[i] = np.nan
            
        elif 1 < i < n:
            prev_cur[i] = math.sqrt((data[i] - data[i-1]) ** 2)
            
            change[i] = np.nan
            volatility[i] = np.nan
            er[i] = np.nan
            sc[i] = np.nan
            kama[i] = np.nan
            
        elif i > n:            
            prev_cur[i] = math.sqrt((data[i] - data[i-1]) ** 2)
            
            change[i] = math.sqrt((data[i] - data[i-n]) ** 2)
            
            volatility[i] = sum(prev_cur[i-n+1:i+1])
            
            er[i] = change[i] / volatility[i]
            
            sc[i] = (er[i] * ((2/(f+1)) - (2/(s+1))) + (2/(s+1))) **2
            
            kama[i] = kama[i-1] + sc[i] * (data[i] - kama[i-1])

        else:
            prev_cur[i] = np.nan
            change[i] = np.nan
            volatility[i] = np.nan
            er[i] = np.nan
            sc[i] = np.nan
            kama[i] = np.nan

    return kama
