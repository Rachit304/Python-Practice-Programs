def digit(Password):
    for i in Password:
        dig = lambda x: True if (i.isdigit()) else False  # chk for digit
        if dig(i):
            return True
            break


def l_Case(Password):
    for i in Password:
        lower = lambda x: True if (i.islower()) else False  # chk for lower case
        if lower(i):
            return True
            break


def u_Case(Password):
    for i in Password:
        upper = lambda x: True if (i.isupper()) else False  # check for upper case
        if upper(i):
            return True
            break


def special_Case(Password):
    special_str = "!@#$%^&* "
    for i in Password:
        special_char = lambda x: True if (i in special_str) else False  # check for special case
        if special_char(i):
            return True
            break


print("Welcome to the World of Social Media....")
print("\n")
username = input("\t\tUsername : ")
password = input("\t\tPassword : ")

length = lambda passwd: len(passwd) > 8

if length(password) and digit(password) and l_Case(password) and u_Case(password) and special_Case(password):
    print("Password Appropriate")
    print("U are now eligible to register")
if not length(password):
    print("Weak Password: Must have at least 8 letters")
if not digit(password):
    print("Weak Password: Must Contain at least one digit")
if not l_Case(password):
    print("Weak Password: Must Contain at least one lower case letter")
if not u_Case(password):
    print("Weak Password: Must Contain at least one uppercase letter")
if not special_Case(password):
    print("Weak Password: Must Contain at least one special character")
