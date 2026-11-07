# email validation program
import re
emailCondition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
userEmail = input("Enter your email address: ")

if re.match(emailCondition, userEmail):
    print("Email address valid")
else:
    print("Email address invalid")