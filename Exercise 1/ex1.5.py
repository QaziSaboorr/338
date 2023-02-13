import timeit
import matplotlib.pyplot as plt
def fib(n, memo={}):
    if n == 0 or n == 1:
        return n
    if n in memo:
        return memo[n]
    else:
        memo[n] = fib(n-1, memo) + fib(n-2, memo)
        return memo[n]


def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)

fibnormal = []
fibmemo = [] 
for x in range(1,35):
    fibnormal.append(timeit.repeat(lambda: func(x),number=1,repeat=1))
    fibmemo.append(timeit.repeat(lambda: fib(x),number=1,repeat=1))

numbers = list(range(1,35))

plt.plot(numbers,fibnormal, label='Normal fib')
plt.plot(numbers,fibmemo, label='Memoization fib')
plt.xlabel('fibonacci number')
plt.ylabel('Time function took (s)')
plt.title('Plot of time taken for two differnet fibonaucci functions to calculate')
plt.legend()
plt.show()

