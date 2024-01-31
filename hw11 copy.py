User_1 = 'Alice'
p_1 = 'C00peR'

User_2 = 'Bob'
p_2 = 'uNc1e'

User_3 = 'Carl'
p_3 = 'ClariNet'

i = 3

while i > 0:
    question = input('Enter your password, please : ')
    i = i - 1
    if question == p_1:
        print(f"Welcome, {User_1}! It's nice to see you again")
        break
    elif question == p_2:
        print(f"Welcome, {User_2}! It's nice to see you again")
        break
    elif question == p_3:
        print(f"Welcome, {User_3}! It's nice to see you again")
        break
    else:
        if i > 0 : 
            print(f"Sorry, password is invalid. Try again!")
            print(f"{i} attempt(s) left")
        else:
            print(f"Sorry, I don`t know you")
