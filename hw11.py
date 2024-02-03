users = {'Alice':'C00peR',
         'Bob': 'uNc1e',
         'Carl': 'ClariNet'}

def check_password(name_user = "Intruder"):
    i = 3
    
    while i > 0:
        question = input('Enter your password, please : ')
        i = i - 1
        if question in users.values():
            login = [key for key, value in users.items() if value == question]
            name_user = login[0]
            check_auth_code(name = name_user)
            break
        else:
            if i > 0 : 
                print(f"Sorry, password is invalid. Try again!")
                print(f"{i} attempt(s) left")
            else:
                print(f"Sorry, I don`t know you")

    return name_user

def check_auth_code(name,expected_auth_code = 1111):
    itCorrect = False
    question = input(f'Enter authentication code, please: ')
    if int(question) == expected_auth_code:
        itCorrect = True
        print(f"Welcome, {name}! It's nice to see you again")
    else : 
        print(f"Sorry, I don`t know you")
    return itCorrect

check_password()