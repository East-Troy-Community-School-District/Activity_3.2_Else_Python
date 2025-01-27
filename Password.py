'''
Password
Pawelski
1/27/2025

Instructions:
1.  Before running the program, predict what it will
    do. Check your prediction by running the program
    and entering a variety of values.
2.  Add a breakpoint to the program on line . Run the
    program in debugging mode. Try entering the password.
    Does the if or else execute? Re-run the program and
    try entering something other than the password. Does
    the if or else execute?
3.  Modify the program so that it checks for the password
    "qwertyuiop123456789@".
'''

name = input("Enter your password >> ")
if name == "password":    # Modify this line of code!
    print("Access granted!")
else:
    print("Access denied!")