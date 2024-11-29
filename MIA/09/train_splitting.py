test_num = int(input())
for i in range(test_num):
    n, m = map(int, input().split()) #cities, routes
    connections = {i: [] for i in range(1, n+1)} 
    routes = []
    for j in range(m):
        x, y = map(int, input().split())
        connections[x].append(y)
        connections[y].append(x)
        routes.append([x, y])
        
        
