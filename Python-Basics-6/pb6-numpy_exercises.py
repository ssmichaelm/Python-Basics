# Michael Moreland - Smoothstack, Python Basics 6; 11/17/2021

# 1. Import np
import numpy as np
print("\nPart 1: Numpy imported")

# 2. Create an array of 10 zeros
print("\nPart2: Create an array of 10 zeroes")
n = np.zeros(10)
print(n)

# 3. Create an array of 10 ones
print("\nPart 3: Create an array of 10 ones")
n = np.ones(10)
print(n)

# 4. Create an array of 10 fives
print("\nPart 4: Create an array of 10 fives")
n = np.full((1,10), 5)
print(n)

# 5. Create an array of integers from 10 to 50
print("\nPart 5: Create an array of integers from 10 to 50")
n = np.arange(10, 51)
print(n)

# 6. Create an array of even integers from 10 to 50
print("\nPart 6: Create an array of even integers from 10 to 50")
n = np.arange(10, 51, 2)
print(n)

# 7. Create a 3x3 matrix with values ranging from 0 to 8
print("\nPart 7: Create a 3x3 matrix with values ranging from 0 to 8")
n = np.matrix([[0,1,2], [3,4,5], [6,7,8]])
print(n)

# 8. Create a 3x3 identity matrix
print("\nPart 8: Create a 3x3 identity matrix")
n = np.eye(3)
print(n)

# 9. Use numpy to randomly generate a number between 0 and 1
print("\nPart 9: Use numpy to randomly generate a number between 0 and 1")
n = np.random.randint(0,2,1)
print(n)
