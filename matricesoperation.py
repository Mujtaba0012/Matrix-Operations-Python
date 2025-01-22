import numpy as np

matrix1 = np.parray([[1,2,3],[4,5,6],[7,8,9]])
matrix2 = np.parray([[9,8,7],[6,5,4],[3,2,1]])

add_result = matrix1 + matrix2

print("Element-wise Addition:\n", add_result)

multiply_result = matrix1 * matrix2

print("Element-wise Multiplication:\n", multiply_result)

dot_result = np.dot(matrix1,matrix2)

print("Element-wise Multiplication:\n", dot_result)

print("\nSum of Matrix 1:", np.sum(matrix1))
print("Mean of Matrix 1:", np.mean(matrix1))