
# Soldier

import random 
class Soldier:
    def __init__(self, health, strength):
        self.health=health
        self.strength=strength
    def attack(self):
        return self.strength
    def receiveDamage(self, damage):
        self.health-=damage
# Viking
      
class Viking(Soldier):
    def __init__(self, name, health, strength):
        Soldier.__init__(self, health, strength)
        self.name=name
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
    def battleCry(self):
        return "Odin Owns You All!"
# Saxon

class Saxon(Soldier):
    def __init__(self,health, strength):
        Soldier.__init__(self, health, strength)
        
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"
# War


class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
    def addViking(self, viking):
        return (self.vikingArmy.append(viking))
    
    def addSaxon(self, saxon):
        return(self.saxonArmy.append(saxon))
    
    def vikingAttack(self):
        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)
        result = saxon.receiveDamage(viking.strength)
        if saxon.health <= 0:
            self.saxonArmy.remove(saxon)
        return result
    
    def saxonAttack(self):
        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)
        result = viking.receiveDamage(saxon.strength)
        if viking.health <= 0:
            self.vikingArmy.remove(viking)
        return result
    def showStatus(self):
        if len(self.vikingArmy)==0:
              return "Saxons have fought for their lives and survive another day..."  
        elif len(self.saxonArmy)==0:  
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy)>=1 or len(self.saxonArmy)>=1:
               return "Vikings and Saxons are still in the thick of battle."
    
