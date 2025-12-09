def myfact(n):
    p = 1
    for k in range(1,n+1):
        p = p * k
    return p

print(myfact(5))