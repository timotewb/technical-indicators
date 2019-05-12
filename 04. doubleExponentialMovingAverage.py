def doubleExponentialMovingAverage(periodDEMA, data):
    
    import numpy as np
    
    p = periodDEMA
    s = data[:p].sum()/p      # the first simple moving average
    m = 2/(p+1)               # weighting factor
    d = (2 * p) - 1           # start of the DEMA

    out = np.zeros(len(data))
    out_d = np.zeros(len(data))

    for i in range(len(data)):
        #--- where data item is the p'th item use the SMA
        if i == p-1:
            out[i] = s
        elif i > p-1:
            out[i] = ((data[i] - out[i-1]) * m) + out[i-1]
        elif i < p-1:
            out[i] = np.nan

        #--- start calculation of DEMA
        if i == d-1:
            out_d[i] = out[(p-1):d].sum()/p
        elif i > d-1:
            #--- now calcuate the DEMA 2xEMA - ema(EMA)
            out_d[i] = (2 * out[i]) - (((out[i] - out_d[i-1]) * m) + out_d[i-1])
        elif i < d-1:
            out_d[i] = np.nan
            
    return out_d
