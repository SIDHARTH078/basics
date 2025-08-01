class Dog:
    def __init__(self,name,breed,owner):
        self.name=name
        self.breed=breed
        self.owner=owner
    def bark(self):
        print("whoof whoof")
class owner:
    def __init__(self,name,address,contact):
        self.name=name
        self.address=address
        self.contact=contact
owner1=owner("sidharth","rajappa nagar","8778823302")
dog1=Dog("kick","labrodar",owner1)
print(dog1.owner.name)

owner2=owner("riteish","mettur","235163521621")
dog2=Dog("lucy","husky",owner2)
print(dog2.owner.name)
