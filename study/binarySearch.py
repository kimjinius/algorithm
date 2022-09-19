## template

n, q = map(int, input().split())
a = list(map(int, input().split()))
m = list(map(int, input().split()))

def binarySearch(arr, start, end, value):
  if start>end :
    return -1
  elif start==end:
    if arr[start] == value : return start
    else :return -1
  else :
    mid = int((start+end)/2)
    if arr[mid] == value : return mid
    elif arr[mid]>value :
      return binarySearch(arr, start, mid-1, value)
    else : 
      return binarySearch(arr, mid+1, end, value)
  
for i in range(q):
  idx = binarySearch(a, 0, n-1, m[i])
  if idx==-1 :
    print("NO")
  else :
    print("YES")
