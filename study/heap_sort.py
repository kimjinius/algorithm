# heap 라이브러리 사용 시, min heap 방식으로 구현 되어 있기 때문에
# 우선순위가 낮은  데이터부터 pop
# 모든 원소를 넣었다가 꺼내면 정렬 가능
import heapq

def heapsort(iterable) :
    h = []
    result = []

    for value in iterable :
        heapq.heappush(h, value)

    for i in range(len(h)) :
        result.append(heapq.heappop(h))
    return result

result = heapsort([1,3,5,7,9,2,4,6,8,10])
print(result)
