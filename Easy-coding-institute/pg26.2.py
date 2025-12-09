n=int(input("Enter a number to see if it is a palindrome or not:"))
a=n
rev=0

while n!=0:
    last=n%10
    rev=rev*10+last
    n=n//10

if rev==a:
    print(a,"is a palindrome number.")
else:
    print(a,"is not a palindrome number.")

