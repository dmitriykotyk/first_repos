users = {'Alice':'C00peR',
         'Bob': 'uNc1e',
         'Carl': 'ClariNet'}
question = input('Enter your password, please : ')
if question in users.values():
    login = [key for key, value in users.items() if value == question]
    print(f"Welcome, {login[0]}! It's nice to see you again")
else:
    print(f"Sorry, I don`t know you")