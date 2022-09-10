## template

m, n = map(int, input().split())

le = m-n
son = 1
mom = 1

for i in range(le) :
  mom = mom * (i+1)
  son = son * (m-i)

com = int(son/mom)
cnt = 0
for i in range(1, len(str(com))+1):
  if com % 10 == 0 :
    com = com//10
    cnt+=1
print(cnt)
