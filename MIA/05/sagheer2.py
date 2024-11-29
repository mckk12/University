items, money = map(int, input().split())

prices = list(map(int, input().split()))



def total_cost(k):
    sum = 0
    price_changed = []
    for j in range(items):
        price_changed.append(prices[j] + k*(j+1))
    price_changed.sort()
    
    for j in range(k):
        sum += price_changed[j]
    return sum


low = 0
high = items

while low<=high:
    mid = (low+high)//2
    if total_cost(mid) <= money:
        answer = mid
        low = mid + 1
    else:
        high = mid - 1

print(answer, total_cost(answer))