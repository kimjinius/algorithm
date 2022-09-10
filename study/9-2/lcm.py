## template

a, b = map(int, input().split())

if a > b :
  temp = a 
  a = b 
  b = temp

def gcd(num1, num2):
  if num2 == 0 :
    return num1
  else :
    return gcd(num2, num1%num2)
    
g = gcd(b, a)
print(int(a*b/g))
