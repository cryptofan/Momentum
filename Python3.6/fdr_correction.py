def fdr_correction(pvals, alpha=0.05):
    '''
    P-value correction for multiple comparison with False Discovery Rate (FDR),
    using Benjamini/Hochberg for independent or positively correlated tests.
    
    INPUT:
    ----------
    pvals:      set of p-values of the individual tests; should be given as an array
    alpha:      error rate; should be given as float 
    
    OUTPUT:
    -------
    reject : array, bool
        True if a hypothesis is rejected, False if not
    pval_corrected : array
        pvalues adjusted for multiple hypothesis testing to limit FDR
    Notes
    -----
    Reference:
    Genovese CR, Lazar NA, Nichols T.
    Thresholding of statistical maps in functional neuroimaging using the false
    discovery rate. Neuroimage. 2002 Apr;15(4):870-8.
    '''
    pvals = np.asarray(pvals)
    shape_init = pvals.shape
    pvals = pvals.ravel()

    pvals_sortind = np.argsort(pvals)
    pvals_sorted = pvals[pvals_sortind]
    sortrevind = pvals_sortind.argsort()

    ecdffactor = _ecdf(pvals_sorted)
    
    reject = pvals_sorted < (ecdffactor * alpha)
    if reject.any():
        rejectmax = max(np.nonzero(reject)[0])
    else:
        rejectmax = 0
    reject[:rejectmax] = True

    pvals_corrected_raw = pvals_sorted / ecdffactor
    pvals_corrected = np.minimum.accumulate(pvals_corrected_raw[::-1])[::-1]
    pvals_corrected[pvals_corrected > 1.0] = 1.0
    pvals_corrected = pvals_corrected[sortrevind].reshape(shape_init)
    reject = reject[sortrevind].reshape(shape_init)
    return reject, pvals_corrected