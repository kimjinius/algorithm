## template
import sys 
input = sys.stdin.readline
sys.setrecursionlimit(10000)
n, r = map(int, input().split())
result = [0]*r

def getResult(x):
  if x>=r :
    flag = 0
    for i in range(r):
      for j in range(r):
        if i != j and result[i] == result[j] :
          flag = 1
          break
      if flag==1 :
        break
    if flag == 0 :
      for i in range(r) :
        print(chr(ord("a")+result[i]), end = "")
      print()
  else :
    for i in range(n):
      result[x] = i
      getResult(x+1)

getResult(0)
