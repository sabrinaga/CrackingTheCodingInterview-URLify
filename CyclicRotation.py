# CyclicRotation
# Rotate an array to the right by a given number of steps.
# Code in Python 3.6

def rotate(A):
    return ([A[-1]] + A[0:-1])

def solution(A, K):
    
    count = 0
    B = A
    while count != (K):
        B = rotate(B)
        count = count + 1
    return B
