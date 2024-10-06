def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True  # 2 is prime
    if n % 2 == 0:
        return False  # Exclude even numbers greater than 2
    
    # Check odd divisors from 3 to the square root of n
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
            
    return True 

def findFirstPrime(array):
    for i in array:
        if is_prime(i):
            print(i)
            return i
    
    return -1

print('test 1')
findFirstPrime([1,2,4,5,7,9])
print('test 2')
findFirstPrime([2,4,5,7,9])
print('test 3')
findFirstPrime([4,6,8,9, 12, 14, 16, 19])
