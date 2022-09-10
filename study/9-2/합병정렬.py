## template

import sys
sys.setrecursionlimit(10**7)

n = int(input())
numbers = list(map(int, input().split()))

def merging(arr, s1, e1, s2, e2):
  temp = []
  p = s1
  q = s2
  
  while p <= e1 and q<=e2 :
    if arr[p] <= arr[q]:
      temp.append(arr[p])
      p+=1
    else :
      temp.append(arr[q])
      q+=1
  
  if p>e1:
    temp.extend(arr[q:e2+1])
  else :
    temp.extend(arr[p:e1+1])
  
  for i in range(s1, e2+1):
    arr[i] = temp[i-s1]
    
def mergeSort(arr, start, end):
  if start >= end :
    return
  
  else :
    mid = (start + end)//2
    mergeSort(arr, start, mid)
    mergeSort(arr, mid+1, end)
    
    merging(arr, start, mid, mid+1, end)
    
mergeSort(numbers, 0, n-1)

for i in range(n):
  print(numbers[i], end=" ")
