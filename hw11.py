
User_1 = 'Alice'
p_1 = 'C00peR'

User_2 = 'Bob'
p_2 = 'uNc1e'

User_3 = 'Carl'
p_3 = 'ClariNet'



def check_password(name_user = "Intruder"):
    i = 3
    
    while i > 0:
        question = input('Enter your password, please : ')
        i = i - 1
        if question == p_1:
            name_user = User_1
            check_auth_code(name = name_user)
            break
        elif question == p_2:
            name_user = User_2
            check_auth_code(name = name_user)
            break
        elif question == p_3:
            name_user = User_3
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