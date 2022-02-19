"""
Function which rotates a NxN matrix by 90 degrees.
Args:
    param1: the matrix to be rotated
Return:
    No return value. Rotates the matrix in place

"""

def rotateImage(matrix):
    n = len(matrix)
    matrix.reverse()
    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
            
if __name__ == '__main__':

    m = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
    rotateImage(m)
    print(m)            
