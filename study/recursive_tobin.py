## template
n, k = map(int, input().split())

result = [0]*k

def getResult(x):
  if x>=k :
    flag = 0
    for i in range(k):
      for j in range(k):
        if i != j and result[i] == result[j] :
          flag = 1
          break
      if flag==1 :
        break
    if flag ==0:
      result1 = [0] * n
      for i in range(k):
        result1[result[i]] = 1
      for i in range(n):
        print(result1[i], end="")
      print()
  else :
    for i in range(n):
      result[x] = i
      if x > 0 and result[x-1] > result[x]:
        continue
      getResult(x+1)

getResult(0)
