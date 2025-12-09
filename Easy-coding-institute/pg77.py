def total(start,end):
    if start > end:
        return 0
    else:
        return start**2 + total(start+1, end)

print(total(1,5))

def sq(num):
    return num**2

def total(start,end):
    if start > end:
        return 0
    else:
        return sq(start) + total(start+1, end)

print(total(1,5))