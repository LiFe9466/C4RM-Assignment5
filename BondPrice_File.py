import numpy as np

def getBondPrice(y, face, couponRate, m, ppy=1):

    periods = np.arange(1, m * ppy + 1)

    cashflows = np.ones(m * ppy) * face * couponRate / ppy
    cashflows[-1] = cashflows[-1] + face

    pv = cashflows / (1 + y / ppy) ** periods

    return(np.sum(pv))