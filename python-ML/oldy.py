#fight club for superheroes
import random
class hero: 
    def __init__(self,hname,powers,weakness):
        self.hname=hname
        self.powers=powers
        self.weakness=weakness
        self.villain=None
        self.health=100
    def attack(self):
        base_damage=random.randint(10,20)
        if self.villain.antipowers==self.powers:
            print(f"{self.hname}'s power is weak against {self.villain.vname}'s anti power!")
            base_damage-=5
        return max(base_damage,5)
        
class villain:
    def __init__(self,vname,antipowers):
        self.vname=vname
        self.antipowers=antipowers
        self.hero=None
        self.health=100
    def attack(self):
        base_damage=random.randint(10,20)
        if self.antipowers==self.hero.weakness:
            print(f"{self.vname} hits a weak spot")
            base_damage+=10
        return base_damage
        
    def fight(self):
        print(f"🦸🏻⚔️🦹🏻Battle:{self.hero.hname} vs {self.vname} begins!\n")
        round=1
        while self.hero.health>0 and self.health>0:
            print(f"\n---Round{round}---")
            round+=1
            break

        damage_to_villain=self.hero.attack()
        self.health-=damage_to_villain
        print(f"{self.hero.hname} attacks {self.vname} for {damage_to_villain} damage")
        print(f"{self.vname}'s health:{self.health}")

        if self.health<=0:
            print(f"\n😀{self.vname} is defeated! {self.hero.hname} wins!")
         
        
        damage_to_hero=self.attack()
        self.hero.health-=damage_to_hero
        print(f"{self.vname} attacks {self.hero.hname} for {damage_to_hero} damage")
        print(f"{self.hero.hname}'s health:{self.health}")

        if self.health<=0:
            print(f"\n🙄{self.hero.hname} is defeated! {self.vname} wins!")
         

        round+=1
        
hero1=hero("superman","superhuman strength","kryptonite")
villain1=villain("lexluthor","kryptonite")
hero2=hero("batman","intelligence","blackmail")
villain2=villain("joker","blackmail")

hero2.villain=villain2
villain2.hero=hero2 
villain2.fight()