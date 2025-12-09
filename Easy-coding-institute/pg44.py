basket = ['mango','guava','apple','kiwi','mango','apple','avacado','mango','orange']

myfruit = input("Enter fruit name to find the count of it in the basket:")

print(myfruit,"=",basket.count(myfruit),"\n")

print("These are the single fruits:")
for k in basket:
    if basket.count(k) < 2:
        print(k)

print()
unique = set(basket)
print("Count of each fruit in the basket:")
for k in unique:
    print(k,"=",basket.count(k))

print()
print("Count of each fruit in the basket:")
mybasket =[]
for k in basket:
    if k not in mybasket:
        mybasket.append(k)

for p in mybasket:
    print(p,"=", basket.count(p))