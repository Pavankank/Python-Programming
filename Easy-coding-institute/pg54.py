email=input("Enter email ID to see if it is valid or not: ")

if "@" in email and "." in email:
    part1 = email.split("@")
    part2 = part1[0].split(".")
    part3 = part1[1].split(".")
    if len(part1) == 2 and len(part2) > 1 and len(part3) == 2:
        if part2[0].isalnum() and part2[1].isalnum() and part3[0] in ['gmail','yahoo','rediff','yandex'] and part3[1] in ['com','org','net']:
            print(f"Email ID '{email}' entered is valid!")
        else:
            print(f"Email ID '{email}' entered is invalid!")
    elif len(part1) == 2 and len(part2) == 1 and len(part3) == 2:
        if part2[0].isalnum() and part3[0] in ['gmail','yahoo','rediff','yandex'] and part3[1] in ['com','org','net']:
            print(f"Email ID '{email}' entered is valid!")
        else:
            print(f"Email ID '{email}' entered is invalid!")
    else:
        print(f"Email ID '{email}' entered is invalid!")
else:
    print(f"Email ID '{email}' entered is invalid!")