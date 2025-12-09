
def mymax(mylist):
    mx = 0
    for k in mylist:
        if mx < k:
            mx = k

    return mx

m = [5,6,91,30,5,56]
print(mymax(m))

