mylist=[20000,25000,45000,50000,38000]
total=0
for k in mylist:
    if k < 50000:
        total = total + k
print(total)