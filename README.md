# average_entropy

This code calculates the expected value of the entropy of a uniformly distributed sample of size N over $\Omega$ bins (or categories). When $N \gg \Omega$, the expected value is often approximated with its asymptotic value, which is the maximal entropy, $\log{\Omega}$. However, for small samples, the exact average entropy may be required. Averaging over all the possible distributions can be problematic, due to the combinatorial explosion in the number of distributions of N (non-distinct) datapoints over $\Omega$ (distinct) bins. Here we propose an algorithm that greatly reduces computing time by iterating over the integer *partitions* of N.

## Usage

### Import module

```python
    from average_entropy import avg_entropy
```

### Calculate expected value of entropy

Example where we are interested in the expected value of the entropy of a random uniformly distributed sample of size 6 over 20 bins.

```python
    e = avg_entropy(6, 20)
	print(e)
```




