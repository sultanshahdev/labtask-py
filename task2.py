import numpy as np

# 1. Create a 5x5 NumPy array with random integers between 10 and 100
array = np.random.randint(10, 101, size=(5, 5))

print("===== Original Array =====")
print(array)
print()

# 2. Identify all values greater than the mean of the entire array
mean_value = np.mean(array)
greater_than_mean = array[array > mean_value]

print("Mean of the original array:", mean_value)
print("\nValues greater than the mean:")
print(greater_than_mean)
print()

# 3. Replace all values below 50 with 0
modified_array = array.copy()
modified_array[modified_array < 50] = 0

# 4. Print the original mean and the modified array
print("===== Modified Array (Values < 50 replaced with 0) =====")
print(modified_array)
