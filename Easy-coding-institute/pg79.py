# mylist = [4,5,6,7,8,9]

# x = lambda a : max(a)

# print()

# # for k in mylist:
# #     x = lambda k : k+
# # print(x(3))

def findmax(n):
    m = 0
    for k in n:
        if m < k:
            m = k
    return m
x = lambda a : findmax(a)
print(x([2,56,34,64,1,234]))