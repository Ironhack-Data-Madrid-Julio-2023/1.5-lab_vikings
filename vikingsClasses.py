
# Soldier

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
    
    def __init__ (self, name, health, strength):
        
        self.name=name
        self.health=health
        self.strength=strength
        
    def attack(self):
        
        return self.strength
    
    def receiveDamage(self,damage):
        
        self.damage=damage
        self.health=self.health-damage
        if self.health>0:
            return f"{self.name} has received {self.damage} points of damage"
        elif self.health<=0:
            return f"{self.name} has died in act of combat"
            
    def battleCry(self):
        x= "Odin Owns You All!"
        return x 
          

# Saxon

class Saxon(Soldier):
    
        def __init__ (self, health, strength):
        
            self.health=health
            self.strength=strength
            
        def attack(self):
        
            return self.strength
        
        def receiveDamage(self,damage):
        
            self.damage=damage
            self.health=self.health-damage
            
            if self.health>0:
                return f"A Saxon has received {self.damage} points of damage"
            
            elif self.health<=0:
                return "A Saxon has died in combat"

            

# War

class War:
    
    def __init__(self):
        
        self.vikingArmy=[]    
        self.saxonArmy=[]
        
    def addViking(self,Viking):
        
        self.vikingArmy.append(Viking)
        
    def addSaxon(self,Saxon):
        
        self.saxonArmy.append(Saxon)
        
    def vikingAttack(self):
        
        saxon = self.saxonArmy[0]  
        viking = self.vikingArmy[0]  
        
        battle = saxon.receiveDamage(viking.strength)  
        if battle == "A Saxon has died in combat":
            self.saxonArmy = self.saxonArmy[1:]  
        
        return battle
    
    
    def saxonAttack(self):
        
        saxon = self.saxonArmy[0]  
        viking = self.vikingArmy[0]  
        
        battle = viking.receiveDamage(saxon.strength)  
        if battle == f"{viking.name} has died in act of combat":
            self.vikingArmy = self.vikingArmy[1:]  
        
        return battle
    
    def showStatus(self):
        
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
        

        

        

