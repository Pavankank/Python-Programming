basket1 = {"apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "kiwi"}
basket2 = {"kiwi", "lemon", "mango", "nectarine", "orange", "papaya", "cherry", "grape"}

print(f"Unique fruits of basket1 that are not there in basket2: {basket1 - basket2}")

print()

print(f"Common fruits in both the baskets: {basket1.intersection(basket2)}")

print()

print(f"All fruits from both the baskets: {basket1.union(basket2)}")


