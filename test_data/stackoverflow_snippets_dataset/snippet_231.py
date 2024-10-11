# Extracted from https://stackoverflow.com/questions/3013449/list-comprehension-vs-lambda-filter
[x for x in X if P(x)]

[f(x) for x in X if P(f(x))]

primes_cubed = [x*x*x for x in range(1000) if prime(x)]

prime_cubes = [x*x*x for x in range(1000) if prime(x*x*x)]

prime_cubes = filter(prime, [x*x*x for x in range(1000)])

