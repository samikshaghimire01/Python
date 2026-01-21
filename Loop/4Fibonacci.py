# Write a program to print the fibonacci series upto nth term.
n = int(input("Enter the number of terms: "))

fibonacci = []
a, b = 0, 1

for i in range(n):
    fibonacci.append(a)
    a, b = b, a + b

print(fibonacci)

