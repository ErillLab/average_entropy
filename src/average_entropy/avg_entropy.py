
import math
from scipy.stats import multinomial


def entropy(counts):
    '''
    Returns Shannon's Entropy for the `counts` vector.
    '''
    n = sum(counts)
    H = 0
    for c in counts:
        if c != 0:
            H -= (c/n) * math.log(c/n, 2)
    return H

def append_partitions(out_list, n, *rest):
    '''
    Appends all the possible partitions of `n` to a pre-existing list `out_list`.
    Every partition is itself a list.
    '''
    out_list.append([n, *rest])
    min = rest[0] if rest else 1
    max = n // 2
    for i in range(min, max+1):
        append_partitions(out_list, n-i, i, *rest)

def count_distributions(partition, N_bins):
    '''
    Counts how many distributions correspond to a specified partition of the
    total number of elements T, where T is sum(partition).
    `partition` is assumed to be a vector of non-zero counts. The non-zero counts
    in `partition` refer to one of many possible bins. The total number of
    possible bins is `N_bins`.
    
    Example:
        N_bins = 8
        partition = [2,2,1]
        T = 5 (because 2+2+1=5)
        
        This function will return 168, because there are 168 distributions of
        five counts over 8 bins such that two bins contain 2 counts, one bin
        contains 1 count and all the ramaining five bins contain 0 counts.
        
        One of those 168 distributions would be:
            [0,0,2,1,0,2,0,0]
    '''
    # Non-empty bins
    m = len(partition)
    
    # The number of ways to map `m` non-empty bins onto `N_bins` possible bins is:
    # N_bins!/(N_bins-m)!  To avoid factorials (big nubers) I compute the ratio directly
    num = math.prod([i for i in range(N_bins, N_bins-m, -1)])
    
    # Duplicates: avoid counting multiple times the same distribution (some elements
    # are not unique).
    # Example: the third and sixth bins of [0,0,2,1,0,2,0,0] can be swapped
    # Note that the zeros are not included in the lists that represent partitions,
    # so there's no need to account for the multiple zeros.
    den = 1
    for count_val in list(set(partition)):
        if partition.count(count_val) > 1:
            den *= math.factorial(partition.count(count_val))
    return int(num/den)

def prob_of_distribution(distribution, N_bins):
    '''
    Probability of obtaining the exact list of counts as in `distribution`,
    given that bins are equiprobable, and given that there were `N_bins` bins.
    '''
    n_empty_bins = N_bins - len(distribution)
    distribution = distribution + [0]*n_empty_bins  # Add empty bins
    bin_probs = [1/N_bins] * N_bins  # Discrete uniform over the bins
    return multinomial.pmf(distribution, n=sum(distribution), p=bin_probs)
    
def prob_of_partition(partition, N_bins):
    '''
    Returns the probability that T elements will fall into bins in a way that
    partitions T into a set of counts as `partition`. T is sum(partition).
    
    Example:
        N_bins = 8
        partition = [2,2,1]
        T = 5 (because 2+2+1=5)
        
        This function will return ~ 0.1538, which is the probability that, after
        randomly placing 5 elements in 8 bins, two bins will contain two elements,
        one bin will contain one element, and the remaining bins will be empty.
    '''
    return count_distributions(partition, N_bins) * prob_of_distribution(partition, N_bins)

def avg_entropy(n, N_bins):
    '''
    Returns the expected value of Shannon's entropy for a discrete sample of
    size n, where every element is drawn from a uniform over `N_bins` many bins.
    '''
    # All the partitions of n
    partitions = []
    append_partitions(partitions, n)
    # Expected value of Shannon Entropy (H)
    E = 0
    for partition in partitions:
        if len(partition) <= N_bins:
            p = prob_of_partition(partition, N_bins)
            H = entropy(partition + [0]*(N_bins-len(partition)))
            E += p*H
    return float(E)



