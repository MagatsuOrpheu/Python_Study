"""
C = int(input()) 
for i in range (C): 
  
  nivel = int(input())
  if 100 <= nivel <= 100000:
    if nivel <= 8000:
      print('Inseto!')
    else:
      print('Mais de 8000!')
"""

"""
n = int(input())  

i = 0
while i < n:
    A, B = input().split()

    if len(A) < len(B):
        print("nao encaixa")
    else:
        if A[-len(B):] == B:
            print("encaixa")
        else:
            print("nao encaixa")

    i += 1
"""

# T = int(input())
# i = 0

# while i < T:
  
#     colector = input().split()
#     x, y = int(colector[0]), int(colector[1])
#     print(x % y)

"""

desafio do refrigerante DIO
t = int(input())
i = 0

for i in range(t):
  refri_comprados, garrafas_vazias = input().split()
  refri_comprados, garrafas_vazias = int(refri_comprados), int(garrafas_vazias)
  if garrafas_vazias > refri_comprados:
    print(refri_comprados)
  else:
    print((refri_comprados % garrafas_vazias) + (refri_comprados // garrafas_vazias))
  i = 1 + i
"""

a = input() 
b = input() 
c = input() 

# if a == 'vertebrado' and b == 'ave':

#   if c == 'carnivoro':
#     print('aguia')
#   else:
#     print('pomba')


# elif a == 'vertebrado' and b == 'mamifero':
  
#   if c == 'onivoro':
#     print('homem')
#   else:
#     print('vaca')
    

# elif a == 'invertebrado' and b == 'inseto':
  
#   if c == 'hematofago':
#     print('pulga')
#   else:
#     print('lagarta')

# else:
  
#   if c == 'hematofago':
#     print('sanguessuga')
#   else:
#     print('minhoca')




a = input() 
b = input() 
c = input() 

if a == 'vertebrado' and b == 'ave':

  if c == 'carnivoro':
    print('aguia')
  else:
    print('pomba')


elif a == 'vertebrado' and b == 'mamifero':
  
  if c == 'onivoro':
    print('homem')
  else:
    print('vaca')
    

elif a == 'invertebrado' and b == 'inseto':
  
  if c == 'hematofago':
    print('pulga')
  else:
    print('lagarta')

else:
  
  if c == 'hematofago':
    print('sanguessuga')
  else:
    print('minhoca')

