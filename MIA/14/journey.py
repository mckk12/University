from collections import defaultdict as dd

N = int(input())
answer = 0.0
adjacency = dd(list)

for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    adjacency[a].append(b)
    adjacency[b].append(a)

def dfs(start):
    global answer
    stack = [(start, -1, 1.0, 0)]
    while stack:
        at, parent, probability, depth = stack.pop()
        children = [i for i in adjacency[at] if i != parent]
        for i in children:
            stack.append((i, at, probability / len(children), depth + 1))
        if not children:
            answer += probability * depth

dfs(0)
print("{:.20f}".format(answer))