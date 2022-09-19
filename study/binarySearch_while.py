## template

n = int(input())
a = list(map(int, input().split()))
m = int(input())

def binarySearch(arr, myStart, myEnd, value):
  if arr[myStart] > value : return -1
  elif arr[myStart] == value : return myStart
  
  if arr[myEnd] < value : return -1
  elif arr[myEnd] == value : return myEnd
  
  
  start = myStart
  end = myEnd
  
  while start+1 < end : 
    mid = int((start + end) / 2)
    
    if arr[mid] == value : return mid
    elif arr[mid] > value : end = mid
    else : start = mid
    
  return -1
  
  
  

idx = binarySearch(a, 0, n-1, m)

if idx==-1 :
  print("NO")
else :
  print(idx)
