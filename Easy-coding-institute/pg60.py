t = (3,7,8,9,10)

p=list(t) # type conversions – changing from tuple to type
p.append(20)
t=tuple(p)
print(t)