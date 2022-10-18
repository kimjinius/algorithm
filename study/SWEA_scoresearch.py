score = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

t = int(input())

for test in range(t):
    n, k = map(int, input().split())
    data = []
    
    for _ in range(n):
        a, b, c = map(int, input().split())
        sum_value = (a * 0.35) + (b * 0.45) + (c * 0.2)
        data.append(sum_value)

    k_score = data[k-1]
    data.sort(reverse=True)

    value = n // 10
    result = data.index(k_score) // value

    print("#%d %s" % (test+1, score[result]))
