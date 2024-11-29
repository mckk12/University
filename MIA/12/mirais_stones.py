n = int(input())
vs = list(map(int, input().split()))
m = int(input())
us = sorted(vs)

cumulative_sum = [0] * (n + 1)
for i in range(1, n + 1):
    cumulative_sum[i] = cumulative_sum[i - 1] + vs[i - 1]

u_cumulative_sum = [0] * (n + 1)
for i in range(1, n + 1):
    u_cumulative_sum[i] = u_cumulative_sum[i - 1] + us[i - 1]

for _ in range(m):
    type, l, r = map(int, input().split())
    if type == 1:
        print(cumulative_sum[r] - cumulative_sum[l - 1])
    else:
        print(u_cumulative_sum[r] - u_cumulative_sum[l - 1])
