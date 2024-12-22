import time
from vertex_cover import brute_force, smt_solver, RandomGraph

def test_max_graph(func, n):
    
    g = RandomGraph(n)
    start = time.time()
    func(g)

    return time.time()-start, g.approx_vert_cover

# brute_max = test_max_graph(brute_force, 50)
# print(f"Brute Force: {brute_max[0]}sec for k={brute_max[1]}")

smt_max = test_max_graph(smt_solver, 2500)
print(f"SMT Solver: {smt_max[0]}sec for k={smt_max[1]}")