##
## Genere una lista de tuplas, donde cada tupla contiene en la primera 
## posicion, el valor de la segunda columna; la segunda parte de la 
## tupla es una lista con las letras (ordenadas y sin repetir letra) 
## de la primera  columna que aparecen asociadas a dicho valor de la 
## segunda columna. Esto es:
##
## ('0', ['C'])
## ('1', ['A', 'B', 'D', 'E'])
## ('2', ['A', 'D', 'E'])
## ('3', ['A', 'B', 'D', 'E'])
## ('4', ['B', 'E'])
## ('5', ['B', 'C', 'D', 'E'])
## ('6', ['A', 'B', 'C', 'E'])
## ('7', ['A', 'C', 'D', 'E'])
## ('8', ['A', 'B', 'E'])
## ('9', ['A', 'B', 'C', 'E'])
##
##
mail=open('data.csv','r').readlines()
mail=[row.split('\t') for row in mail]
mail=[[row[1], row[0]] for row in mail]
a=dict()
for row in mail: 
  if row[0] not in a.keys():
    a[row[0]]=[]
  a[row[0]]=a[row[0]]+list(row[1])
for i in sorted(a.keys()):
  b=(i,sorted(set(a[i])))
  print(b)
