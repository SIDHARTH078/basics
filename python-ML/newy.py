import random
class marvelmovie:
    def __init__(self,name,director,rating):
        self.name=name
        self.director=director
        self.rating=rating
        self.health=10
    
    def convert_rating(self,rating):
        rating_map={
            "excellent":5,
            "very good":4,
            "good":3,
            "average":2,
            "poor":1
        }
        return rating_map.get(rating.lower(),0)

    def attack(self):
        base_critic=random.randint(1,10)
        return max(base_critic,2)
    
class dcmovie:
    def __init__(self,name,director,rating):
        self.name=name
        self.director=director
        self.rating=rating
        self.marvelmovie=None
        self.health=10
    def attack(self):
        base_critic=random.randint(1,10)
        return max(base_critic,2)
    def critic_war(self):
        print(f"fight between {self.marvelmovie.name} and {self.name}")
        while self.marvelmovie.health>0 and self.health>0:
            print(f"{self.marvelmovie.name} VS {self.name}")
            break
        damage_to_marvel=self.marvelmovie.attack()
        self.health-=damage_to_marvel
        print(f"{self.director} beats {self.marvelmovie.director} by {damage_to_marvel} damage")
        print(f"{self.name}'s health {self.health}")

        if self.marvelmovie.health<=0:
            print(f"{self.marvelmovie.name} is defeated {self.name} wins")

        damage_to_dc=self.attack()
        self.marvelmovie.health-=damage_to_dc
        print(f"{self.marvelmovie.director} beats {self.director} by {damage_to_dc} damage")
        print(f"{self.marvelmovie.name}'s health {self.marvelmovie.health}")

        if self.health>=0:
            print(f"{self.name} is defeated {self.marvelmovie.name} wins")
    
movie1=marvelmovie("ironman","jon faverue","good")
movie2=dcmovie("batman","matt reeves","excellent")
movie3=marvelmovie("gotg","james gunn","very good")
movie4=dcmovie("superman","james gunn","excellent")
movie4.marvelmovie=movie3
movie4.critic_war()



