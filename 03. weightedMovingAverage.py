def weightedMovingAverage(periodWMA, data):

    from numba import jit
    import numpy as np
    
    #--- define jit code
    @jit(target='cpu', nopython=True)
    def calc(p, data):

        #--- based on period value calculate the 'weighting factor' or denominator
        d = p*(p/2+.5)

        #--- generate weights list
        weights = np.zeros(p)
        for i in range(p):
            weights[i] = (i+1)/d

        #--- calculate WMA
        a = np.zeros(p)
        out = np.zeros(len(data))
        for i in range(len(data)):
            if i < p-1:
                out[i] = np.nan
            else:
                for m in range(p):
                    a[(p-1)-m] = data[i-m,]
                out[i] = np.sum(a * weights)
        return out
    
    #--- execute and return jit code
    return calc(periodWMA, data)
