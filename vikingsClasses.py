
# Soldier

class Soldier:
    
    def __init__(self, health, strength):
        
        self.health = health
        self.strength = strength
    
    def attack(self):
        
        return self.strength

    def receiveDamage(self,damage):
        
        self.health -= damage

        
        
# Viking


class Viking(Soldier):
    
    def __init__(self, name, health, strength):
                       
        Soldier.__init__(self, health, strength)
        
        self.name = name
    
    def receiveDamage(self,damage):
        
        self.health -= damage
        
        if self.health > 0: return self.name+' has received '+str(damage)+' points of damage'
        else: return self.name+' has died in act of combat'
        
    def battleCry(_):
        
        return 'Odin Owns You All!'
            

        
        
# Saxon


class Saxon(Soldier):
    
    def __init__(self, health, strength):
                       
        Soldier.__init__(self, health, strength)
    
    def receiveDamage(self,damage):
        
        self.health -= damage
        
        if self.health > 0: return 'A Saxon has received '+str(damage)+' points of damage'
        else: return 'A Saxon has died in combat'
    

    
# War


class War:

    def __init__(self):
        
        self.vikingArmy = []
        self.saxonArmy = []
    
    def addViking(self,vk):
        
        self.vikingArmy.append(vk)
        
    def addSaxon(self,sx):
        
        self.saxonArmy.append(sx)
    
    def vikingAttack(self):
        
        import random as rd
        
        # Elegimos un saxon aleatorio del ejército y le restamos la fuerza de un viking
        res = rd.choice(self.saxonArmy).receiveDamage(rd.choice(self.vikingArmy).strength)  
        
        for i in self.saxonArmy: # Si hay muertos, los sacamos del ejército
            if i.health <=0:
                self.saxonArmy.remove(i)
        
        return res
    
    def saxonAttack(self):
        
        import random as rd
        
        res = rd.choice(self.vikingArmy).receiveDamage(rd.choice(self.saxonArmy).strength) 
        
        for i in self.vikingArmy:
            if i.health <=0:
                self.vikingArmy.remove(i)
        
        return res
    
    def showStatus(self):
        
        if len(self.saxonArmy) == 0: return 'Vikings have won the war of the century!'
        elif len(self.vikingArmy) == 0: return 'Saxons have fought for their lives and survive another day...'
        else: return 'Vikings and Saxons are still in the thick of battle.'
        
        
        
        
        
        
        
