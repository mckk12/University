n, m = map(int, input().split()) #nodes, edges
edges = {i:[] for i in range(1, n+1)}
for i in range(m):
    x, y = map(int, input().split())
    edges[x].append(y)
    edges[y].append(x)



for i in edges:
    if len(edges[i])==m:
        print("star topology")
        exit()

bus=True
ring=True
for i in edges:
        if len(edges[i])!=1 and len(edges[i])!=2:
            bus=False
            ring=False
            break
if n==m+1:
    ring=False  
else:
    bus=False
    
if bus:
    print("bus topology")
    exit()
if ring:
    print("ring topology")
    exit()
print("unknown topology")


