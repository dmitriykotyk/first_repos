users = {'Alice':'C00peR',
         'Bob': 'uNc1e',
         'Carl': 'ClariNet'}

question = input("Dawai: ")

if question in users.values():
    print("yes")
    login = [key for key, value in users.items() if value == question]
    print(login[0])
else:
    print('no')