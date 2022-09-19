## template

n = int(input())
a = list(map(int, input().split()))
m = int(input())

# arr의 start부터 end까지값들 중에서 
# value가 존재한다면 그 위치를 반환하고,
# 아니라면 -1을 반환하는 함수
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


idx = binarySearch(a, 0, n-1, m)

if idx==-1 :
  print("NO")
else :
  print(idx)
