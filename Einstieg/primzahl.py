def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if (n%i) == 0:
            return False
    return True

for i in range (1,20):
    if is_prime(i):
        print(i,end=" ")