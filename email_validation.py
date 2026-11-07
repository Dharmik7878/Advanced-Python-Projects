# email validation program
email = input("Enter your email address: ")

k, j, d = 0, 0, 0

if len(email) > 7 :
    if email[0].isalpha():
        if ("@" in email) and (email.count("@") == 1):
            if (email[-4] == ".") or (email[-3] == "."):
                for i in email:
                    if i == i.isspace():
                        k = 1
                    elif i.isalpha():
                        if i == i.upper():
                            j = 1
                    elif i.isdigit():
                        continue
                    elif (i == "_") or (i == ".") or (i == "@") or (i == "-"):
                        continue
                    else:
                        d = 1
                if (k == 1) or (j == 1) or (d == 1):
                    print("Invalid email address 5")
                else:
                    print("Email registration successful!")
            else:
                print("Invalid email address 4")
        else:
            print("Invalid email address 3")
    else:
        print("Invalid email address 2")
else:
    print("Invalid email address 1")

# print("Error no. = 1 = Your mail len is less than 7")
# print("Error no. = 2 = In Your mail first latter is not alpha")
# print("Error no. = 3 = In Your mail @ are more than 1 time")
# print("Error no. = 4 = In Your mail . dot are more than 1 time")
# print("Error no. = 5 = Space ' ', or upper case, or digit is in your mail")