'''
Dynamic Programming Course

examples
- count the number of different ways to move through a 6x9 grid
- given a set of coins, how can we make 27 cents in the least number of coins

- Most difficult part is whiteboarding the solution
- range of questions is diverse which makes DP hard

2 Parts in Dynamic Programming
1. Memoization
2. Tabulation

Write a function fib(n) that takes in a number n and returns the nth number of the Fibonacci sequence

     n: 1, 2, 3, 4, 5, 6, 7
fib(n): 1, 1, 2, 3, 5, 8, 13
'''

def fib(n):
  if n <= 2:
    return 1
  result = fib(n-1) + fib(n-2)
  return result
  
# This function is correct but its slow and inefficient

#Using Memoization

# dict for memo keys will be arg for fib, value will be the return value
memo = {}
def fib(n, memo):
  if n in memo:
    return memo[n]
  if n <= 2:
    return 1
  
  result = fib(n - 1, memo) + fib(n - 2, memo)
  memo[n] = result
  return result

