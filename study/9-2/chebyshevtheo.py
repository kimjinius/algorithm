## template

while True :
  a = int(input())
  if a == 0 :
    break
  else :
    cnt = 0
    for i in range(a+1, a*2+1):
      flag = 0
      if i == 1 :
        pass
      else:
        for j in range(2, i):
          if i%j == 0 :
            flag =1
            break
        if flag == 0 :
          cnt+=1
    print(cnt)
