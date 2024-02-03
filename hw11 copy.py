users = {'Alice':'C00peR',
         'Bob': 'uNc1e',
         'Carl': 'ClariNet'}
i = 3

while i > 0:
    question = input('Enter your password, please : ')
    i = i - 1
    if question in users.values():
        login = [key for key, value in users.items() if value == question]
        print(f"Welcome, {login[0]}! It's nice to see you again")
    else:
        if i > 0 : 
            print(f"Sorry, password is invalid. Try again!")
            print(f"{i} attempt(s) left")
        else:
            print(f"Sorry, I don`t know you")
