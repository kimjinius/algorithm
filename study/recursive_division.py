## template
## template

n = int(input())
cnt = 0
result = [0] * n

def getResult(mySum, index) :
  global cnt
  if mySum == n :
    print(result[0], end="")
    for i in range(1, index):
      print("+"+ str(result[i]), end="")
    print()
    cnt+=1
  else :
    if index==0:
      myNumber = n-1
    else : 
      myNumber = n - mySum
    
    for i in reversed(range(1,myNumber+1)):
      result[index] = i
      if index > 0 and result[index-1]<result[index]:
        continue
      getResult(mySum+i, index+1)
      
getResult(0,0)
print(cnt)
