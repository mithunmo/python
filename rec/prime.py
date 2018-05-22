

def prime(n):
    for i in range(2,n):
        if n % i == 0:
            return [i] + prime(n // i)
    return[n]

print(prime(20))