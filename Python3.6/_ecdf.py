def _ecdf(x):
    '''
    No frills empirical cdf used in fdrcorrection.
    '''
    nobs = len(x)
    return np.arange(1, nobs + 1) / float(nobs)