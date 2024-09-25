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

# By using memo structure, we cut down on recrusive calls and going down recursive subtrees


def gridTraveler(n, m):
  if n == 1 and m == 1:
    return 1
  if n == 0 or m == 0:
    return 0 
  
  moveDown = gridTraveler(n-1, m)
  moveRight = gridTraveler(n, m-1)
  return moveDown + moveRight
  
# again this will be slow for a large grid 
# use memo
memo = {}
def gridTraveler(n, m, memo):
  key = n + ',' + m
  if key in memo:
    return memo[key]
  if n == 1 and m == 1:
    return 1
  if n == 0 or m == 0:
    return 0 
  
  moveDown = gridTraveler(n-1, m, memo)
  moveRight = gridTraveler(n, m-1, memo)
  memo[key] = moveDown + moveRight
  return moveDown + moveRight

# With memoization we cut down O(2^n+m) to O(n*m) time
# tree nodes could have m*n combinations
# O(n+m) Space

##############################################################################
# Memoization Recipe -> DP in general
"""
  1. Make it work
    * visualize the problem as a tree
    * implement the tree using recursion (leaves of tree are base case for hint)
    * test it

  2. Make it efficient
    * add a memo object
    * add a base case to return memo values
    * store return values into the memo
  
"""
############################################################################

'''
  canSum function (Naive)
  write a funciton canSum(targetSum, numbers) that takes in a target Sum and an array of numbers as args

  the function should return a boolean whether or not it is possible to generate the target sum 
  you can use an element as many times as you want
  assume all input numbers are nonnengative
  example: canSum(7, [5,4,3,7]) -> true
  Larger target sums are harder than smaller targets
  We should encode args into our function, into the nodes of our drawing

'''
def canSum(targetSum, numbers):
  if targetSum == 0:
    return True
  elif targetSum < 0:  # if targetSum is negative nothing in numbers can be subtract to get a solution
    return False

  #for every element in numbers we need to branch to simulate subtracting targetSum with that value
  for num in numbers:
    if canSum(targetSum - num, numbers): # returns boolean
      return True # early return true if subproblem returns True
  
  return False

# Time Complexity: two inputs: m is size of targetSum, n is length of numbers
# max height of tree case: if you subtract 1 from m, m times
# branching factor: n
# O(n^m)
# Space Complexity: call stack contains at most m recursive calls
############################################################################


'''
  canSum function (optimized)
  use memoization to store calculations to query when seen again

'''
memo = {}
def canSum(targetSum, numbers, memo):
  # if targetSum is in memo return memo[targetSum]
  if targetSum in memo:
    return memo[targetSum]
  if targetSum == 0:
    return True
  elif targetSum < 0:  # if targetSum is negative nothing in numbers can be subtract to get a solution
    return False

  #for every element in numbers we need to branch to simulate subtracting targetSum with that value
  for num in numbers:
    if canSum(targetSum - num, numbers): # returns boolean
      memo[targetSum] = True
      return True # early return true if subproblem returns True
  memo[targetSum] = False
  return False

'''
  Again we say m = target sum n = array length
  Memoized: O(m*n) time, O(m) space
  why? m levels by at most n calculations. after that it O(1) access from memo
  That is also why the space complexity is O(m) - the memo will only have at most m mappings
'''
##################################################################
# i need to return an array at each recursive call
def howSum(targetSum, numbers):
  if targetSum == 0:
    return []
  elif targetSum < 0:
    return None
  
  for num in numbers:
    remainderResult = howSum(targetSum - num, numbers)
    if remainderResult is not None:
      return [remainderResult] + [num]

  return None    

'''
  m = target sum, n = length of numbers
  # of recursive calls we make plus copying of array for every call: O(n^m * m) Time
  Space: stack space O(m) + O(m) for array that is passed up the call stack: O(m)
  
'''
memo = {}
def howSumMemo(targetSum, numbers, memo):
  if targetSum in memo:
    return memo[targetSum]
  if targetSum == 0:
    return []
  elif targetSum < 0:
    return None
  
  for num in numbers:
    remainderResult = howSumMemo(targetSum - num, numbers, memo)
    if remainderResult is not None:
      memo[targetSum] = [remainderResult] + [num]
      return memo[targetSum]

  memo[targetSum] = None
  return None   
# time: O(n*m) recursive calls (* m) for copying the array -> O(n* m^2)
# space: O(m*m) for memo + O(m) for stack size -> O(m^2)

