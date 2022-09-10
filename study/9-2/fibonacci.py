## template

n = int(input())

arr = [0, 1]

if n==0 :
  print(0)
else : 
  for i in range(n-1):
    arr.append(arr[0]+arr[1])
    del arr[0]
  
  print(arr[1])
