import pandas as pd
import numpy as np

# Create a Series containing 10 random numbers
s = pd.Series(np.random.rand(10))

print("Original Series:")
print(s)

# Indexing: access the value at index 3
print("\nValue at index 3:")
print(s[3])

# Filtering: select values greater than 0.5
print("\nValues greater than 0.5:")
print(s[s > 0.5])

# Statistical operations
print("\nMean:", s.mean())
print("Median:", s.median())
print("Minimum:", s.min())
print("Maximum:", s.max())