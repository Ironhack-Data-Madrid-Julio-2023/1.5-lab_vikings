
# Soldier


class Soldier:
    
    def __init__(self, health, strength): #tiene dos atributos, health y strength, que se inicializan 
                                          # en el método __init__()cuando se crea una instancia de la clase:
        self.health = health
        self.strength = strength
        
        
    def attack(self): # Devuelve la fuerza del soldado cuando se le llama.
        
        return self.strength
       
    def receiveDamage(self, damage): # Recibe un atributo damage que reduce la salud del soldado.
        
        self.health -= damage # Reduce la salud de soldado.
    
    pass


# Viking


class Viking(Soldier): # Es una "hija" subclase de soldier
    
    def __init__(self, name, health, strength): # Hereda los atributos y metodos de Soldier utilizando el método __int_ Soldier.
        Soldier.__init__(self, health, strength) 
                                           
        self.name = name
        
    def attack(self): # Devuelve la fuerza del vikingo cuando se le llama.
        
        return self.strength
    
       
    def receiveDamage(self, damage): 
        
        self.health -= damage # Reduce la salud del vikingo
            
   
        if self.health > 0: # Si la salud es mayor que 0
        
            return f"{self.name} has received {damage} points of damage" # " El vikingo1 ha recibido 10 puntos de daño"
        
        else:
            return f"{self.name} has died in act of combat" # "El vikingo1 ha muerto en combate"
        
    def battleCry(self):
        
        return "Odin Owns You All!" # Cadena de grito de batalla de los vikingos.
            
        
    pass

# Saxon


class Saxon(Soldier): # Es una "hija" de Soldier
    
    def __init__ (self, health, strength): # Ha diferencia de vikingo el Sajon no tiene nombre.
        
        Soldier.__init__(self, health, strength) 
                                           
        
    def receiveDamage(self, damage): # Atributo daño igual que en vikingo
        
        self.health -= damage # Reduce la saludo del sajon.
        
        if self.health > 0: # Si la salud es mayor que 0:
            
            return f"A Saxon has received {damage} points of damage" # " El sajon ha recibido 10 puntos de daño. 
                                                                    # No llamamos name a saxon por que no tiene atributo name.
        else:
            return f"A Saxon has died in combat"
    
    pass

# War
import random

class War:  # Aqui se define la guerra. 
    
    def __init__(self): # Se llama al constructor __init__ inicializa las dos listar vacias.
        self.vikingArmy = [] # lista de ejercito, se inicia como contador vacio.
        self.saxonArmy = [] 
        
    def addViking(self, viking): # Se utiliza para añadir vikingos a la guerra.
        self.vikingArmy.append(viking) # agrega vikingos a la lista vacia.
    
    def addSaxon(self, saxon): # Se utiliza para añadir sajones a la guerra.
        self.saxonArmy.append(saxon) # agrega sajones a la lista vacia.
    
              
    def vikingAttack(self): # El metodo realiza un ataque vikingo
        
        viking = random.choice(self.vikingArmy) # la funcion random.choice() para llamar a un vikingo aleatorio de la lista.
        saxon = random.choice(self.saxonArmy)
        
        result = saxon.receiveDamage(viking.strength) # se almacena en resultado llamando al daño del sajon pasando por la
                                                       # fuerza del vikingo
        if saxon.health<= 0: # Si el sazon muere
            self.saxonArmy.remove(saxon) # se elimina de saxonArmy utilizando remove.
            
        return result
    
    def saxonAttack(self): # el metodo realiza el ataque de un sajon
        
        
        viking = random.choice(self.vikingArmy) # se crean la funcion rando.choice para llamar a los V y S aleatoriamente.
        saxon = random.choice(self.saxonArmy)
        
        result = viking.receiveDamage(saxon.strength) # Se almacena el resultado llamando al daño del viking, paasando por
                                                        # la fuerza del Sajon.
        if viking.health <= 0: # si el vikingo muere.
            self.vikingArmy.remove(viking) # Se elimina del VikingArmy.
            
        return result
    
     
     
    def showStatus(self): # Verifica el estado actual de la guerra.
       
        if len(self.saxonArmy) == 0: # Si la longitud de lista"saxonArmy" es igual a 0, ya no quedan Sajones.
 
            return "Vikings have won the war of the century!"
        
        elif len(self.vikingArmy) == 0: # Si la longitud de lista"vikingArmy es igual a 0, los sajones sobreviven.
            
            return "Saxons have fought for their lives and survive another day..."
        
        else:
            return "Vikings and Saxons are still in the thick of battle."
          
       
        
    
    

    pass
