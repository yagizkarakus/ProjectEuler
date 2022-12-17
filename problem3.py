# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?
n = 600851475143

largest_primeFactor = 0
while n % 2 == 0:
    if largest_primeFactor < 2:
        largest_primeFactor = 2
    n = n/2

for i in range(3, int(n**(1/2))+1, 2):
    while n % i == 0:
        if largest_primeFactor < i:
            largest_primeFactor = i
        n = n/i
if n>2:
    if largest_primeFactor < n:
        largest_primeFactor = n

print(largest_primeFactor)