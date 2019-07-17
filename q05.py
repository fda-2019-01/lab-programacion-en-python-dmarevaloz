##
## Imprima el valor maximo y minimo por cada letra de la columa 1.
##
## A,9,1
## B,9,1
## C,9,0
## D,7,1
## E,9,1
##
mail=open('data.csv','r').readlines()
mail=[row.split('\t') for row in mail]
a=dict()
b=dict()
for row in mail: 
  if row[0] not in a.keys():
    a[row[0]]=0
  if int(row[1])>=a[row[0]]:
    a[row[0]]=int(row[1])
    
  if row[0] not in b.keys():
    b[row[0]]=max(int(x[1]) for x in mail)
  if int(row[1])<=b[row[0]]:
    b[row[0]]=int(row[1])
for i in sorted(b.keys()):
  print(i,',',a[i],',',b[i],sep='')
