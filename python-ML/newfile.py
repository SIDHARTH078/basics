class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def greet(self):
        print(f"hello,my name is {self.name} and im {self.age}years old.")


person1=person("allice",30)
person2=person("bob",27)
person3=person("sidharth",18)
person2.greet()
 