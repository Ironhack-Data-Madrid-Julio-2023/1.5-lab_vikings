
import random
import subprocess
import os
from datetime import datetime

t1 = datetime.now()

ntests = 30
errorcount = 0

randomoptions = ['1','2','3','a','odin',1,2,3,'Odin','patata','hjdgjdsgb',853,'',' ','fhjdg dff',[453,4646]]
safeoptions = ['1','2']

with open('file.py', 'r') as file:
    contenido_file = file.read()


for i in range(ntests):

    test = [random.choice(randomoptions),
            random.choice(randomoptions),
            random.choice(randomoptions),
            random.choice(randomoptions),
            random.choice(randomoptions),
            random.choice(randomoptions),
            random.choice(randomoptions),
            random.choice(safeoptions),
            random.choice(safeoptions)]
    
    exec(contenido_file)

if errorcount == 0:

    os.system('cls||clear')
    ttotal = datetime.now()-t1
    print('Total time ----- '+str(ttotal.total_seconds())+' s\n')
    print('All Ok. '+str(ntests)+' tests passed.')

else:

    os.system('cls||clear')
    ttotal = time.now()-t1
    print('Total time ----- '+str(ttotal.total_seconds())+' s\n')
    print(str(errorcount)+' of '+str(ntests)+' tests failed...')
