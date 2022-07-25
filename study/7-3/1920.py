from sys import stdin, stdout
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

def binary_search(data, search):
    if len(data)==1:
        if data[0] == search:
            return True
        else:
            return False
    medium = len(data)//2
    if search == data[medium]:
        return True
    if search > data[medium]:
        return binary_search(data[medium:], search)
    else :
        return binary_search(data[:medium], search)
        
a.sort()
for i in range(m):
    if binary_search(a, b[i]):
        print("1")
    else:
        print("0")
