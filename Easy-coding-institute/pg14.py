x=int(input("Enter the x value:"))
y=int(input("Enter the y value:"))

if x>0 and y>0:
	print(x,",",y," values are in Quad 1")
elif x<0 and y>0:
	print(x,",",y," values are in Quad 2")
elif x<0 and y<0:
	print(x,",",y," values are in Quad 3")
elif x>0 and y<0:
	print(x,",",y," values are in Quad 4")
elif x==0 and y>0:
	print(x,",",y," values are on positive y axis")
elif x==0 and y<0:
	print(x,",",y," values are on negative y axis")
elif y==0 and x>0:
	print(x,",",y," values are on positive x axis")
elif y==0 and x<0:
	print(x,",",y," values are on negative x axis")
else:
	print(x,",",y," values are at origin")
