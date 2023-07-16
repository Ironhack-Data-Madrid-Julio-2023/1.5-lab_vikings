from vikingsClasses import *

import random
import time



def dice():
    for i in range(40):
        lastnum = random.choice(range(1,7))
        print(lastnum,end="\r")
        time.sleep(.05)

    return lastnum


w = War()

print('\nWelcome to the Final Battle of All Times!!!! In the following minutes, a combat will start in which you will fight for your survival. \
    \nAn army of fellow soldiers will fiercely defend you, but first you must choose which side you are on...\n')

print('VIKINGS are proud and dangerous warriors known for their strength and perseverance. Whenever a viking army is left with less than ten soldiers, \
    \nthe remaining ones increment their strength in 100-200%!\
    \n\nSAXONS, however, are bounded by strong alliances among each others. Whenever their armies descend from 10 integrants, they call more allies for help \
    \nincreasing their total to up to 15 soldiers.\
    \n\nEach side has its advantages, but neither of them will follow a stranger. A few questions will need to be answered to determine your fate.')

ready = input('\nAre you ready?!!!\n1: Yes\n2: No\n')

flag = True
while flag:
    try:
        int(ready)
        flag = False
    except:
        ready = input('Oups! It seems you fail to answer as indicated. Try again!')

if ready == '2': print("\n'WRARG!!! YOU SHOULD HAVE THOUGHT ABOUT THAT BEFORE'-- an angry viking shouts. \n")
else: pass


q = ['\nWhich of the following is NOT a viking god?\n1: Frey\n2: Asgard\n3: Thor\n',
'\nAlong with Frey and Thor, what is the name of the remaining main deidy?\n',
'\nWhich is the drink the vikings consume the least?\n1: Ale\n2: Beer\n3: Wine\n',
'\nWhere are the saxons mostly stablished?\n1: England\n2: Germany\n3: Scotland\n',
"\nWhat was the saxons' original religion?\n1: German religion\n2: Christianity\n3: They worshiped diverse religions\n",
'\nHave saxons ever met the Celtic people?\n1: Yes\n2: No\n']

a = [input(e) for e in q]
right_a = ['2','odin','3','2','1','1']

check = [a[i].lower()==right_a[i] for i in range(len(a))]
vscore = sum(check[:3])
sxscore = sum(check[3:])

flag = True

while flag:
        if vscore < sxscore: ch1 = '2'
        elif vscore > sxscore: ch1 = '1'
        else: ch1 = input('\nWOW! It seems you know the same about both cultures. You get to choose then. Which army do you want to lead?:\n1: Vikings\n2: Saxons\n')
        
        if ch1 == '1': 
            print("\nvikingChief: 'WROARG! You will guide us to victory!'\n")
            print("\x1B[3m" + 'You correctly answered ' +str(vscore)+'/3 questions about your people, the Vikings.\
            \nIt will have an influence on their initial health and strength..\n' + "\x1B[0m")
            score = vscore
            flag = False
        elif ch1 == '2': 
            print("\nsaxonsChief: 'We will bring you the glory, my lord.'\n")
            print("\x1B[3m" + 'You correctly answered ' +str(sxscore)+'/3 questions about your people, the Saxons.\
            \nIt will have an influence on their initial health and strength..\n' + "\x1B[0m")
            score = sxscore
            flag = False
        else: 
            print('You must really choose a side now...')


attackrange = {0:30,1:50,2:80,3:100}
healthrange = {0:200,1:250,2:280,3:300}


viking_names = [
    "Ragnar", "Ivar", "Bjorn", "Lagertha", "Erik", "Sigurd", "Freyja", "Harald", "Astrid",
    "Rollo", "Frida", "Leif", "Ingrid", "Olaf", "Sigrun", "Eirik", "Gunnar", "Thora", "Ubbe",
    "Aslaug", "Eivor", "Hilda", "Egil", "Sif", "Hakon", "Thyra", "Njal", "Helga", "Thorstein",
    "Yrsa", "Vidar", "Gudrun", "Gorm", "Gyda", "Haldor", "Ragnhild", "Halfdan", "Thordis",
    "Ivarr", "Gisla", "Knut", "Borghild", "Birger", "Ranveig", "Dag", "Alfhild", "Eyvind",
    "Ylva", "Hjalmar", "Liv"
]

cter=0

if ch1 == '1':

    for i in range(30):
        w.addViking(Viking(viking_names[i],random.choice(range(healthrange[score]-20,healthrange[score]+20)),random.choice(range(attackrange[score]-20,attackrange[score]))))
        w.addSaxon(Saxon(healthrange[2],attackrange[2]))
        
    print('%20s %42s' % ('Your Army',"The enemys' Army"))
    for i in range(30):
        cter+=1
        print('%-12s %-10s %-15s %-12s %-10s %-10s' % (str(w.vikingArmy[i].name),'h: '+str(w.vikingArmy[i].health),'s: '+str(w.vikingArmy[i].strength),'Saxon '+str(cter),'h: '+str(w.saxonArmy[i].health),'s: '+str(w.saxonArmy[i].strength)))

elif ch1 == '2':
    
    for i in range(30):
        w.addViking(Viking(viking_names[i],healthrange[2],attackrange[2]))
        w.addSaxon(Saxon(random.choice(range(healthrange[score]-20,healthrange[score]+20)),random.choice(range(attackrange[score]-20,attackrange[score]))))
    
    print('%20s %42s' % ('Your Army',"The enemys' Army"))
    for i in range(30):
        cter+=1
        print('%-12s %-10s %-15s %-12s %-10s %-10s' % ('Saxon '+str(cter),'h: '+str(w.saxonArmy[i].health),'s: '+str(w.saxonArmy[i].strength),str(w.vikingArmy[i].name),'h: '+str(w.vikingArmy[i].health),'s: '+str(w.vikingArmy[i].strength)))

else:
    pass

battle1=input("\nThe first battle is about to start.\
              \nPress enter to roll a dice, the first attack will be yours if you get a nunber higher than 3.\n")

d1 = dice()

print('\n')
sv, ss = 0, 0

if d1 > 3 and ch1 == '1' or d1 <=3 and ch1 == '2':
    while w.showStatus() == 'Vikings and Saxons are still in the thick of battle.':

        if sv == 0 and len(w.vikingArmy)<10:
            print("\n'AAAAAGH!!! FOR THE POWER OF ODIN!' -- Less than 10 vikings remain alive. Their strength rises in 100-200%!\n")
            time.sleep(4)
            sv+=1
            for j in w.vikingArmy:
                j.strength *= 1 + 0.01*random.choice(range(50,100))
        elif ss == 0 and len(w.saxonArmy)<10:
            print("\n'Dear fellow brothers, we need your help!' -- Less than 10 saxons remain alive. Up to 15 brothers join the fight!\n")
            time.sleep(4)
            ss+=1
            for j in range(random.choice(range(5,15))):
                w.addSaxon(Saxon(random.choice(range(50,100)),random.choice(range(20,60))))
        else:
            pass

        print(w.vikingAttack())
        time.sleep(0.1)
        if w.showStatus() == 'Vikings and Saxons are still in the thick of battle.':
            print(w.saxonAttack())
        else:
            pass
    print('\n')
    print(w.showStatus())
    print('Viking warriors left: '+str(len(w.vikingArmy)),'Saxon soldiers left: '+str(len(w.saxonArmy)))

else:
    while w.showStatus() == 'Vikings and Saxons are still in the thick of battle.':

        if sv == 0 and len(w.vikingArmy)<10:
            print("\n'AAAAAGH!!! FOR THE POWER OF ODIN!' -- Less than 10 vikings remain alive. Their strength rises in up to 300%!\n")
            time.sleep(4)
            sv+=1
            for j in w.vikingArmy:
                j.strength *= 1 + 0.01*random.choice(range(100,200))
        elif ss == 0 and len(w.saxonArmy)<10:
            print("\n'Dear fellow brothers, we need your help!' -- Less than 10 saxons remain alive. Up to 15 brothers join the fight!\n")
            time.sleep(4)
            ss+=1
            for j in range(random.choice(range(5,15))):
                w.addSaxon(Saxon(random.choice(range(50,100)),random.choice(range(20,60))))
        else:
            pass

        print(w.saxonAttack())
        time.sleep(0.1)
        if w.showStatus() == 'Vikings and Saxons are still in the thick of battle.':
            print(w.vikingAttack())
        else:
            pass
    print('\n')
    print(w.showStatus())
    print('Viking warriors left: '+str(len(w.vikingArmy)),'Saxon soldiers left: '+str(len(w.saxonArmy)))

if ch1 == '1' and w.showStatus() == 'Vikings have won the war of the century!' or ch1 == '2' and w.showStatus() == 'Saxons have fought for their lives and survive another day...':
    ent2 = input("\n\n\nYOU WON THE BATTLE! Your remaining army rejoices in its triumph. \
                 \n\nOWEVER, you get overconfident, and the next day a second group of angry enemies appears to add pain to your hangover. \
                 \nPress enter when ready!\n\n")
    vict = 1
    
else:
    ent2 = input("\n\n\nYOU LOST THE BATTLE.. Alone in the woods, you pray for mercy to the gods and wait for your death. \
                 \n\nBUT SUDDENLY, an unnoticed small group of survival warriors from your army gets to you and shout: \
                 \n\n'We will not give up!!!!!!!'\n\
                \nWith a new hope, you thank the universe and prepare yourself for revenge. \
                 \nPress enter when ready!\n\n")
    vict = 0

if ch1 == '1' and vict == 1 or ch1 == '2' and vict ==0:
        
    for i in range(random.choice(range(5,20))):
        w.addSaxon(Saxon(random.choice(range(50,200)),random.choice(range(30,100))))

else:

    for i in range(random.choice(range(5,20))):
        w.addViking(Viking(random.choice(viking_names),random.choice(range(50,200)),random.choice(range(30,100))))

if ch1 == '2':
    print('%20s %42s' % ('Your Army',"The enemys' Army"))

else:
    print('%20s %52s' % ("The enemys' Army",'Your Army'))
vks = len(w.vikingArmy)
sxs = len(w.saxonArmy)

cter = 0
if vks < sxs:
    for i in range(vks):
        cter+=1
        print('%-12s %-25s %-15s %-12s %-10s %-10s' % ('Saxon '+str(cter),'h: '+str(w.saxonArmy[i].health),'s: '+str(w.saxonArmy[i].strength),str(w.vikingArmy[i].name),'h: '+str(w.vikingArmy[i].health),'s: '+str(w.vikingArmy[i].strength)))
    for i in range(vks,sxs):
        cter+=1
        print('%-12s %-25s %-15s %-12s %-10s %-10s' % ('Saxon '+str(cter),'h: '+str(w.saxonArmy[i].health),'s: '+str(w.saxonArmy[i].strength),'','',''))
else:
    for i in range(sxs):
        cter+=1
        print('%-12s %-25s %-15s %-12s %-10s %-10s' % ('Saxon '+str(cter),'h: '+str(w.saxonArmy[i].health),'s: '+str(w.saxonArmy[i].strength),str(w.vikingArmy[i].name),'h: '+str(w.vikingArmy[i].health),'s: '+str(w.vikingArmy[i].strength)))
    for i in range(sxs,vks):
        cter+=1
        print('%-12s %-25s %-15s %-12s %-10s %-10s' % ('','','',str(w.vikingArmy[i].name),'h: '+str(w.vikingArmy[i].health),'s: '+str(w.vikingArmy[i].strength)))

battle1=input("\nThe second battle is about to start.\
              \nPress enter to roll a dice, the first attack will be yours if you get a nunber higher than 3.\n")

d2 = dice()

print('\n')
sv, ss = 0, 0

if d2 > 3 and ch1 == '1' or d2 <=3 and ch1 == '2':
    while w.showStatus() == 'Vikings and Saxons are still in the thick of battle.':

        if sv == 0 and len(w.vikingArmy)<10:
            print("\n'AAAAAGH!!! FOR THE POWER OF ODIN!' -- Less than 10 vikings remain alive. Their strength rises in 100-200%!\n")
            time.sleep(4)
            sv+=1
            for j in w.vikingArmy:
                j.strength *= 1 + 0.01*random.choice(range(50,100))
        elif ss == 0 and len(w.saxonArmy)<10:
            print("\n'Dear fellow brothers, we need your help!' -- Less than 10 saxons remain alive. Up to 15 brothers join the fight!\n")
            time.sleep(4)
            ss+=1
            for j in range(random.choice(range(5,15))):
                w.addSaxon(Saxon(random.choice(range(50,100)),random.choice(range(20,60))))
        else:
            pass

        print(w.vikingAttack())
        time.sleep(0.1)
        if w.showStatus() == 'Vikings and Saxons are still in the thick of battle.':
            print(w.saxonAttack())
        else:
            pass
    print('\n')
    print(w.showStatus())
    print('Viking warriors left: '+str(len(w.vikingArmy)),'   Saxon soldiers left: '+str(len(w.saxonArmy)))

else:
    while w.showStatus() == 'Vikings and Saxons are still in the thick of battle.':

        if sv == 0 and len(w.vikingArmy)<10:
            print("\n'AAAAAGH!!! FOR THE POWER OF ODIN!' -- Less than 10 vikings remain alive. Their strength rises in up to 300%!\n")
            time.sleep(4)
            sv+=1
            for j in w.vikingArmy:
                j.strength *= 1 + 0.01*random.choice(range(100,200))
        elif ss == 0 and len(w.saxonArmy)<10:
            print("\n'Dear fellow brothers, we need your help!' -- Less than 10 saxons remain alive. Up to 15 brothers join the fight!\n")
            time.sleep(4)
            ss+=1
            for j in range(random.choice(range(5,15))):
                w.addSaxon(Saxon(random.choice(range(50,100)),random.choice(range(20,60))))
        else:
            pass

        print(w.saxonAttack())
        time.sleep(0.1)
        if w.showStatus() == 'Vikings and Saxons are still in the thick of battle.':
            print(w.vikingAttack())
        else:
            pass
    print('\n')
    print(w.showStatus())
    print('Viking warriors left: '+str(len(w.vikingArmy)),'   Saxon soldiers left: '+str(len(w.saxonArmy)))

if ch1 == '1' and w.showStatus() == 'Vikings have won the war of the century!' or ch1 == '2' and w.showStatus() == 'Saxons have fought for their lives and survive another day...':
    print("\nYou won the second battle!\n")
    time.sleep(2)
    vict +=1
    
else:
    print("\nYou lost the second battle..\n")
    time.sleep(2)



if vict == 2:
    print("Your people have proven themselves the champions of the Greatest War of All Times, winning both battles fought.\
          \n\nYOU WON THE GAME, NOW GO GET DRUNK TO CELEBRATE!\
          \nTHE WAR HAS ENDED\n")

elif vict == 1:
    print("------- 'TRUCE????'\
          \nThe chief of the other army is willing to make a deal with you, as none of you have been able to win both battles. \
          \nYou look to your exhausted warriors and accept, seal it with ale and beer and start an era of\
          \ncollaboration. \
          \n\nTHE WAR HAS ENDED\n")

elif vict == 0:
    print("You lost both battles. The fields are red with the blood of your soldiers, and your body is a mesh of bones, wounds and pain. \
          \nAs you close your eyes and fall to the ground, a goat approaches and starts eating your hair.\
          \n\nHELL AWAITS YOU, AND YOUR THERE-AWAITING FURIOUS WARRIORS TOO..\
          \n\nGAME OVER\n")