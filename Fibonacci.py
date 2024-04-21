#Print Fibonacci Series

n = 10
a, b = 0, 1
fib_series = []
for i in range(n):
    fib_series.append(a)
    a, b = b, a + b
print("Fibonacci Series:", fib_series)