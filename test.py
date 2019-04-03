import exotic_algorithms as exa
import numpy as np
import time


# Takes sorting function as input and prints its execution time
def time_it(func):
    start = time.time()
    func()
    end = time.time()
    print('Finished in {} seconds.'.format(end - start))


# Generates a random list of integers
randlist = np.random.randint(0, 100, 5).tolist()
print('Unsorted list:', randlist)

# Passes bogo sort function to time_it function
print('\nBogo sort...')
bogosort = lambda: exa.bogosort(randlist)
time_it(bogosort)

# Passes sleep sort function to time_it function
print('\nSleep sort...')
sleepsort = lambda: exa.sleepsort(randlist)
time_it(sleepsort)

