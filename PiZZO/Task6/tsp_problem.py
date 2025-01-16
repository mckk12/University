from itertools import permutations

def read_input():
    n = int(input().strip())
    edges = []
    for i in range(n):
        weights = list(map(int, input().strip().split()))
        for j, weight in enumerate(weights):
            if i!=j: #we dont need that edge and dont want to count it
                edges.append((i, j, weight))
    
    return n, edges

def brute_force(n, edges):
    perm = permutations(range(n))
    min_cost = float('inf')
    cycle = []
    for p in perm:
        cost = 0
        for i in range(n):
            cost += edges[p[i]][p[(i+1)%n]]
        if cost < min_cost:
            min_cost = cost
            cycle = p
    return min_cost, cycle
    
def tsp(vertices, edges):    
    edges_sorted = sorted(edges, key=lambda x: x[2])
    visited = [-1]*vertices
    visited[edges_sorted[0][0]] = True

    # dp[i][j] minimum weight starting from i and ending in j
    dp = [[float('inf')]*vertices for _ in range(vertices)]
    for i in range(vertices):
        dp[i][i] = 0
    
    

n, edges = read_input()
print(tsp(n, edges))
