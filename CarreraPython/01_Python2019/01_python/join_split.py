nombres = ['mateo','marcos','lucas','juan']
print(type(nombres)) # list
print(nombres)
x = '**'.join(nombres) # mateo**marcos**lucas**juan
print(x)
print(type(x)) # str
print(x.split('a')) #['m', 'teo**m', 'rcos**luc', 's**ju', 'n']
print(type(x.split()))