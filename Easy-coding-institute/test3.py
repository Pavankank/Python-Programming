def sum_of_multiples_with_for(n):
    sum = 0
    for i in range(n):
        if i%3 == 0 or i%5 == 0:
            sum = sum + i
            print(i,sum)
    print(f"Sum of the multiples of 3 or 5 below {n}: {sum}")
    
sum_of_multiples_with_for(int(input("Enter a number: ")))