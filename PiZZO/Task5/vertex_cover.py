from random import randint
from itertools import combinations
from z3 import Solver, Bool, Or, If, Sum

class RandomGraph():
    def __init__(self, n):
        self.size = n
        self.num_of_edges = 0
        self.vertices = set(i for i in range(n))
        self.neighbors = {i:[] for i in range(n)}
        self.edges = set()
        self.approx_vert_cover = 0
        self.generate_edges()
        self.greedy_eval()
    
    # Part A
    def generate_edges(self):
        r = randint(self.size-2, self.size**2)
        for _ in range(r):
            u = randint(0, self.size-1)
            v = randint(0, self.size-1)
            if u != v and (v, u) not in self.edges and (u, v) not in self.edges:
                self.edges.add((u, v))
                self.neighbors[u].append(v)
                self.neighbors[v].append(u)
                self.num_of_edges += 1
            
    
    # Part B
    def greedy_eval(self):
        neigh = {v: self.neighbors[v].copy() for v in self.neighbors}
        highest_degree_vertex= max(neigh, key=lambda v: len(neigh[v]))
        # vertex_cover_approx = set()
        vertex_cover_approx = 0

        while len(neigh[highest_degree_vertex])>0:
            # vertex_cover_approx.add(highest_degree_vertex)
            vertex_cover_approx+=1

            for v in neigh[highest_degree_vertex]:
                neigh[v].remove(highest_degree_vertex)
            neigh[highest_degree_vertex] = []

            highest_degree_vertex = max(neigh, key=lambda v: len(neigh[v]))
        
        self.approx_vert_cover = max(0, vertex_cover_approx-randint(0, 1))


# Part C
def generate_random_graphs(max_vertex):
    graphs = []
    for i in range(1, max_vertex+1):
        for _ in range(3):
            g = RandomGraph(i)
            graphs.append(g)
    return graphs


# Part D
def brute_force(graph):
    k = graph.approx_vert_cover
    possibilities = combinations(graph.vertices, k)
    for p in possibilities:
        flag = True
        for edge in graph.edges:
            if edge[0] not in p and edge[1] not in p:
                flag = False
                break
        if flag:
            return p
    return None

# Part G
def smt_solver(graph):
    k = graph.approx_vert_cover

    solver = Solver()
    vertex_vars = {v: Bool(f'v_{v}') for v in graph.vertices}

    for u, v in graph.edges:
        solver.add(Or(vertex_vars[u], vertex_vars[v]))

    solver.add(Sum([If(vertex_vars[v], 1, 0) for v in graph.vertices]) <= k)

    solver.check()
    try:
        model = solver.model()
        return [v for v in vertex_vars if model[vertex_vars[v]]]
    except:
        return None
