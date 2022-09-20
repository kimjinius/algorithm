## template
n, s = map(int, input().split())

data = list(map(int, input().split()))

start = 1 # start X를 가리킴
end = n  # end O

def check(interval):
  # 구간의 길이 interval만큼 정했을 때, 그합이 S이상인 경우가 있는가?
  sum = 0 
  for i in range(interval) :
    sum += data[i]
  if sum>= s : return True
  for i in range(n-interval):
    sum = sum-data[i] + data[i+interval]
    
    if sum >= s :
      return True
      
  return False

if check(1) :
  print("1")
elif check(n)==False:
  print("-1")
else : 
  while start+1 < end :
    mid = int((start+end)/2)
    
    if check(mid) :
      end = mid
    else :
      start = mid
  print(end)
