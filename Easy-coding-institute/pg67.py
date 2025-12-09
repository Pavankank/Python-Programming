stocks = {
    "OPPO" : ['K5','K7','K55','K3'],
    "VIVO" : ['T3','T1','T2'],
    "REDMI" : ["NOTE 12","NOTE 13", "NOTE 13 PRO MAX", "NOTE 14", "NOTE 14 PRO"],
    "SAMSUNG"   : ["S6","S7","S9","S13"]
    }

while True:
    print("\n1. Add Model \n2. Get Models \n3. Buy Phone \n4. Display All \n5. Find Company \n6. Exit")
    try:
        option = int(input("Enter your option: "))

        if option == 1:
            company = input("Enter the company name: ")
            model = input("Enter model name: ")
            if company in stocks:
                model_list = stocks.get(company)
                model_list.append(model)
                print("Model added successfully..")
            else:
                newlist=[]
                newlist.append(model)
                stocks.update({company:newlist})
                print("Model added successfully!")

        elif option == 2:
            company = input("Enter the company name to get all the available models: ")
            if company in stocks:
                mylist = stocks.get(company)
                print(f"Available models:")
                for k in mylist:
                    print(k)
            else:
                print("Company not found..")

        elif option == 3:
            company = input("Enter the company name to get models: ")
            model = input("Enter model that you would like to buy: ")
            if company in stocks:
                available = stocks.get(company)
                available.remove(model)
                print("Sold Successfully")
            else:
                print("Sorry, the entered model not available!")
        elif option == 4:
            for record in stocks.items():
                print(f"{record[0]} --> {record[1]}")
        elif option == 5:
            model = input("Enter model to find its company name: ")
            for company, models in stocks.items():
                for k in models:
                    if k == model:
                        print(f"Company Name of {model}: {company}")
            if model not in models:
                print("Model not found!")
        elif option == 6:
            print("Thank you for using our services!!")
            break
        else:
            print("Invalid choice. Please choose again.")
    except ValueError:
        print("Invalid input. Please enter a number.")