import numpy as np
from scipy.special import factorial
import math

def calc_rank_ensemble_pvalue(ranks, max_rank):
    def n_choose_k(n, k):
        return factorial(n, exact=True) / (factorial(k, exact=True) * factorial(n - k, exact=True))
    def is_odd_or_even(n):
        return 1 if n % 2 == 1 else -1
    n_ind = max_rank
    n_samples = len(ranks)
    total_ways = 0
    max_n_hits = min(ranks)
    for n_hits in range(1, max_n_hits+1):
        #print(n_hits)
        ways = n_choose_k(n_ind, n_hits) #number of sets of n_hit individuals
        #print("number of sets of n_hit individuals: " + str(n_choose_k(n_ind, n_hits)))
        for i in range(n_samples):
            ways *= n_choose_k(ranks[i], n_hits) * factorial(n_hits, exact=True) #number of ways to select nhits out of r ranks
            #this isn't right * n_hits!
            #print("number of ways to arrange the hits, " + str(n_choose_k(ranks[i], n_hits)))
            ways *= factorial(n_ind - n_hits, exact=True) #number of ways to arrange the rest
            #print("number of ways to arrange the rest, " + str(factorial(n_ind - n_hits, exact=True)))
            #print(str(ranks[i]) + ", " + str(ways))

        total_ways += is_odd_or_even(n_hits) * ways
        #print(total_ways)
    #print(factorial(n_ind, exact=True)**n_samples)
    pval = math.log(total_ways) - math.log(factorial(n_ind, exact=True)**n_samples)
    return pval
