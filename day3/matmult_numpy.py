#!/usr/bin/python

# Program to multiply two matrices using nested loops
import numpy as np

N = 250

# NxN matrix
X = []
for i in range(N):
    X.append([np.random.randint(0,100) for r in range(N)])

# Nx(N+1) matrix
Y = []
for i in range(N):
    Y.append([np.random.randint(0,100) for r in range(N+1)])

result = np.matmul(X, Y)
print(result)
