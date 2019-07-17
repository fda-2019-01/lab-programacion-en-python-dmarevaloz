##
## Por cada clave de la columna 5 (cadena de tres letras), obtenga
## el valor mas pequeño y el valor mas grande asociado a esa clave.
##
## aaa,0,6
## bbb,4,7
## ccc,0,1
## ddd,5,5
## eee,0,0
## fff,4,9
## ggg,3,3
## hhh,6,8
## iii,2,7
## jjj,2,5
##
mail=open('data.csv','r').readlines()
mail=[row.split('\t') for row in mail]
b=[row[4].split(',') for row in mail]
n=','.join([row[4] for row in mail]).split(',')
n=[row.replace('\n','').split(':') for row in n]
from itertools import groupby
from operator import itemgetter
for key, group in groupby (sorted(n, key=itemgetter(0)), itemgetter(0)):
  g=list(group)
  max_g=max(int(x[1]) for x in g)
  min_g=min(int(x[1]) for x in g)
  print(f'{key},{min_g},{max_g}')
