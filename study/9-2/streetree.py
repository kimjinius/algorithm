## template
n = int(input())
arr1 = []
arr2 = []
for i in range(n):
  arr1.append(int(input()))

for i in range(n-1):
  arr2.append(arr1[i+1]-arr1[i])
  
def gcd(num1, num2):
  if num2 == 0 :
    return num1
  else :
    return gcd(num2, num1%num2)

g = gcd(arr2[1], arr2[0])    
for i in range(3, len(arr2)):
  g = gcd(arr2[i], g)
  
print(int((arr1[n-1] - arr1[0])/g)+1-n)
