import itertools

population = [5, 10, 15, 20]
sample_distribution = []
sample_distribution_no_repeats = []
sample_size = 2
replacement = True

if replacement:
    sample_distribution = itertools.product(population, repeat=sample_size)
    print("samples with replacement:")
else:
    sample_distribution = itertools.permutations(population, sample_size)
    print("samples without replacement:")
for i in sample_distribution:
    print(i)

print("\nsample probabilities:")

