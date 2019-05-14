def trippleExponentialMovingAverage(periodDEMA, data):
    
    import numpy as np
    
    p = periodDEMA
    s = data[:p].sum()/p      # the first simple moving average
    k = 2/(p+1)               # weighting factor
    d = (2 * p) - 1           # start of the DEMA

    out = np.zeros(len(data))
    out_ee = np.zeros(len(data))
    out_eee = np.zeros(len(data))
    out_d = np.zeros(len(data))

    for i in range(len(data)):
        #--- where data item is the p'th item use the SMA
        if i == p-1:
            out[i] = s
            out_ee[i] = s
            out_eee[i] = s
            out_d[i] = s
        elif i > p-1:
            #--- calculate EMA
            out[i] = (k * data[i]) + (1 - k) * out[i-1]
            #--- calcualte ema of ema
            out_ee[i] = (k * out[i]) + (1 - k) * out_ee[i-1]
            #--- calcualte ema of ema of ema
            out_eee[i] = (k * out_ee[i]) + (1 - k) * out_eee[i-1]
            #--- calculate tema
            out_d[i] = 3 * out[i] - 3 * out_ee[i] + out_eee[i]
        elif i < p-1:
            out[i] = np.nan
            out_ee[i] = np.nan
            out_eee[i] = np.nan
            out_d[i] = np.nan
            
    return out_d
