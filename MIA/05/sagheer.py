items, money = map(int, input().split())

prices = list(map(int, input().split()))
prices.sort()
max_k = items + 1

total_cost = money + 1

while total_cost > money:
    max_k-=1
    sum = 0
    for j in range(max_k):
        sum += max_k * (j+1) + prices[j]
    total_cost = sum   


print(max_k, total_cost)