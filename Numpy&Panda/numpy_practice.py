import numpy as np

#Create a NumPy array containing numbers from 10 to 50 with step 5.
def qn1():
  arr = np.arange(10, 51, 5)
  print("qn1:\n", arr)

#Create a 3x3 matrix with random integers between 1 and 100.
def qn2():
  matrix = np.random.randint(1, 101, (3, 3))
  print("qn2:\n", matrix)

#Find the mean, median, and standard deviation of an array.
def qn3(): 
    arr = np.array([100, 206, 308, 407, 555])
    mean = np.mean(arr)
    median = np.median(arr)
    std = np.std(arr)
    print("qn3: \n")
    print("Mean:", mean)
    print("Median:", median)
    print("Standard Deviation:", std)

#Reshape a 1D array of 12 elements into a 3x4 matrix.
def qn4():    
    arr = np.arange(1, 13)
    reshaped = arr.reshape(3,4)
    print("qn4:\n", reshaped)

#Extract all even numbers from an array.
def qn5(): 
    arr = np.array([100, 206, 308, 407, 555])
    even= arr[arr % 2 == 0]
    print("qn5: \n", even)

#Replace all values greater than 50 with 0.
def qn6():
    arr = np.array([10, 26, 308, 407, 555])
    arr[arr > 50] = 0
    print("qn6: \n", arr)

#Perform element-wise multiplication of two arrays.
def qn7():
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    result = a * b
    print("qn7: \n", result)

#Compute the dot product of two matrices.
def qn8():
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    dot_product = a @ b
    print("qn8: \n",dot_product )

#Find the index of the maximum and minimum values in an array.
def qn9():
    arr = np.array([100, 206, 308, 407, 555])
    max_index = np.argmax(arr)
    min_index = np.argmin(arr)
    print("qn9: \n")
    print("Max:", max_index)
    print("Min:", min_index)

#Normalize an array so values are between 0 and 1.
def qn10():
    arr = np.array([100, 206, 308, 407, 555])
    normalized = (arr - arr.min()) / (arr.max() - arr.min())
    print("qn10: \n", normalized )

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