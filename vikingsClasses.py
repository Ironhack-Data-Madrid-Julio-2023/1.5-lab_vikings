
# Soldier


class Soldier:
    
    def __init__(self, health, strength):
        
        self.health = health
        self.strength = strength
    
    def attack(self):
        
        return self.strength
    
    def receiveDamage(self, damage):
        
        self.health -= damage
       
        
# Viking


class Viking(Soldier):
    
    def __init__(self, name, health, strenght):
        
        self.name = name
        
        Soldier.__init__(self, health, strenght)
        
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
    
    def __init__(self, health, strenght):
        
        Soldier.__init__(self, health, strenght)
        
    def receiveDamage(self, damage):
        
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"
# War
import random

class War:
    
    def __init__(self):
        
        self.vikingArmy = []
        self.saxonArmy = []
        
    def addViking(self, viking):
        
        self.vikingArmy.append(viking)
        
    def addSaxon(self, saxon):
        
        self.saxonArmy.append(saxon)
        
    def vikingAttack(self):
        
        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)
        result_of_calling = saxon.receiveDamage(viking.strength)
        
        if saxon.health <= 0:
            self.saxonArmy.remove(saxon)
        
        return result_of_calling
        
        
    def saxonAttack(self):
        
        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)
        result_of_calling = viking.receiveDamage(saxon.strength)
        
        if viking.health <= 0:
            self.vikingArmy.remove(viking)
        
        return result_of_calling 
    
    def showStatus(self):
        
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."    
    
    
    
