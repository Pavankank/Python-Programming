mylist=[]
while True:
    print("1. Add element\n2. Delete element\n3. Display elements\n4. Display Current list\n5. Exit")
    option = int(input("Enter your option:"))

    if option==1:
        ele = int(input("Enter element:"))
        mylist.append(ele)
        print(ele,"has been added successfully.")

    if option==2:
        ele = int(input("Which element you want to delete:"))
        if ele in mylist:
            mylist.remove(ele)
            print(ele,"deleted successfully.")
        else:
            print(ele,"not found..")
    if option==3:
        #print(mylist)
        for k in mylist:
            print(k,end=' ')
    
    if option==4:
        print(mylist)

    if option==5:
        print("Thank you!!")
        break
