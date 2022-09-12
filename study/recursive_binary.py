## template

number = int(input())

a = []

def binary(n):
  if n ==0 :
    return
  elif n==1 :
    a.append(1)
    return 
  else :
    a.append(n % 2)
    binary(n//2)

binary(number)    
for i in reversed(range(len(a))):
  print(a[i], end="")
