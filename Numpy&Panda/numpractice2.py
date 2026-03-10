import numpy as np
import pandas as pd

# 1️ Create a 5x5 identity matrix and replace diagonal
def qn1():
    mat = np.eye(5)
    np.fill_diagonal(mat, [10, 20, 30, 40, 50])
    print("Q1:\n", mat)


# 2️ Outer sum using broadcasting
def qn2():
    a = np.array([1,2,3])
    b = np.array([[10],[20]])
    outer_sum = a + b
    print("Q2:\n", outer_sum)


# 3️ Clip 100 random numbers outside 2 std
def qn3():
    arr = np.random.randn(100)
    mean = arr.mean()
    std = arr.std()
    clipped = np.clip(arr, mean - 2*std, mean + 2*std)
    print("Q3 (first 10):\n", clipped[:10])


# 4️ Sort 2D array by second column
def qn4():
    arr = np.random.randint(1, 50, (5,3))
    sorted_arr = arr[np.argsort(arr[:,1])]
    print("Q4:\n", arr)
    print("Sorted by 2nd column:\n", sorted_arr)


# 5️ Structured NumPy array for employees
def qn5():
    dtype = [('name','U10'),('age','i4'),('salary','f4')]
    arr = np.array([("Alice",30,50000),("Bob",25,60000)], dtype=dtype)
    print("Q5:\n", arr)


# 6️ Upper triangular of 4x4 matrix
def qn6():
    mat = np.arange(16).reshape(4,4)
    upper = np.triu(mat)
    print("Q6:\n", upper)


# 7️ Stack 1D arrays vertically & horizontally
def qn7():
    a = np.arange(1,6)
    b = np.arange(6,11)
    c = np.arange(11,16)
    vstacked = np.vstack([a,b,c])
    hstacked = np.hstack([a,b,c])
    print("Q7 Vertical shape:", vstacked.shape)
    print(vstacked)
    print("Q7 Horizontal shape:", hstacked.shape)
    print(hstacked)


# 8️ Cumulative sum row-wise and column-wise
def qn8():
    arr = np.arange(1,10).reshape(3,3)
    row_cumsum = np.cumsum(arr, axis=1)
    col_cumsum = np.cumsum(arr, axis=0)
    print("Q8 Row-wise cumsum:\n", row_cumsum)
    print("Q8 Column-wise cumsum:\n", col_cumsum)


# 9️ Rows where row sum exceeds 100
def qn9():
    arr = np.random.randint(10,50,(5,5))
    rows = arr[np.sum(arr, axis=1) > 100]
    print("Q9:\n", arr)
    print("Rows with sum > 100:\n", rows)


# 10 Inverse and determinant of 3x3 matrix
def qn10():
    mat = np.array([[2,1,1],[1,3,2],[1,0,0]])
    inv = np.linalg.inv(mat)
    det = np.linalg.det(mat)
    print("Q10 Inverse:\n", inv)
    print("Q10 Determinant:", det)

qn1()
qn2()
qn3()
qn4()
qn5()
qn6()
qn7()
qn8()
qn9()
qn10()