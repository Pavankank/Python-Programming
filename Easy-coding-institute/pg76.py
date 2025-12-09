def total(start, end):
    if start > end:
        return 0
    else:
        return start + total(start+1, end)

print(total(1,5))