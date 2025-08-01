class user:
    def __init__(self,username,email,password):
        self.username=username
        self.email=email
        self.password=password
 
    def say_hi_to_user(self,user):
        print(f"sending message to {user.username}:hi {user.username},its {self.username}")

user1=user("batsy078","sidharthselvaraj2@gmail.com","hello")
user2=user("sid_harth2007","nightwing78dg@gmail.com","femboy")
user1.say_hi_to_user(user2)
print(user1.email)
