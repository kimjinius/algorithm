## template

n = int(input())
cnt = 0

for i in range(n):
  flag = 0
  a = int(input())
  if a == 1 :
    pass
  else:
    for j in range(2, a):
      if a%j == 0 :
        flag =1
        break
    if flag == 0 :
      cnt+=1
print(cnt)
