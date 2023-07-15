
# Soldier

import random
class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength
         
    
    def receiveDamage(self, damage):
        self.health = self.health - damage
                
# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        Soldier.__init__(self, health, strength)
        self.name = name
     
    
   
    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return self.name + ' ' + 'has received ' + str(damage) +  ' points of damage'
        
        if self.health <= 0:
            return self.name + ' has died in act of combat'
        
      
    def battleCry(self):
        return "Odin Owns You All!"
                             
# Saxon
class Saxon(Soldier):
    
    def __init__(self,health, strength):
        Soldier.__init__(self, health, strength)
        
    def receiveDamage(self, damage):
        self.health = self.health - damage
        
        if self.health > 0:
            return "A Saxon has received " + str(damage) + " points of damage"
        
        elif self.health <= 0:
            
            return "A Saxon has died in combat"
        
        
         
class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
    
    
    def addViking(self, Viking):
        self.vikingArmy.append(Viking)
    
    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)
     
    
    def vikingAttack(self):
        saxon_random = random.choice(self.saxonArmy)
        viking_random = random.choice(self.vikingArmy)
        r = saxon_random.receiveDamage(viking_random.strength)
        
        if saxon_random.health <= 0: 
            self.saxonArmy.remove(saxon_random)
                                   
        return r
        
        
    def saxonAttack(self):
        viking_random = random.choice(self.vikingArmy)
        saxon_random = random.choice(self.saxonArmy)
        r = viking_random.receiveDamage(saxon_random.strength)
        
        if viking_random.health <= 0:
            self.vikingArmy.remove(viking_random)
            
        return r
        
    def showStatus(self):
        if not self.saxonArmy:
            return "Vikings have won the war of the century!"
        elif not self.vikingArmy:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."

