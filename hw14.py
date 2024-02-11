class AccessLevel:
    def __init__(self,name = None,level = None):
        self.name = name
        self.level = level
    
    def __eq__(self, other):
        return self.level == other.level
    def __lt__(self, other):
        return self.level < other.level
    def __gt__(self, other):
        return self.level > other.level

class AccessObject:
    def __init__(self,name,content,access_level):
        self.name = name
        self.content = content
        self.access_level = access_level

class User:
    def __init__(self,login = "Guest", mandatum = None):
        self.login = login
        self.__mandatum = mandatum

    @property
    def mandatum(self):
        return self.__mandatum.name
    
    @mandatum.setter
    def mandatum(self):
        if self.__mandatum.name != None and self.__mandatum.level != None:
            return self.__mandatum.name
        else: 
            return None
        
    def get_access(self,access_object):
        self.access_object = access_object
        if self.__mandatum.level >= access_object.access_level.level:
            print(access_object.content)
        else:
            print(f"Access to {access_object.name} denied")


    def greet(self):
        print(f"Hi, my login is {self.login}")

if __name__ == '__main__':
    unclassified = AccessLevel("Unclassified", 1)
    secret = AccessLevel("Secret", 2)
    top_secret = AccessLevel("Top Secret", 3)

    alice = User("Alice", top_secret)
    bob = User("Bob", unclassified)

    password_database = AccessObject(
        "Password Database",
        "Alice - C00peR, Bob - uNc1e",
        secret
    )

    alice.greet()
    alice.get_access(password_database)

    bob.greet()
    bob.get_access(password_database)
    


