import time
from vertex_cover import brute_force, smt_solver, RandomGraph

def test_max_graph(func):
    time_taken = 0
    n = 10   
    earlier_info = (0,0,0)
    while time_taken<120:
        g = RandomGraph(n)
        start = time.time()
        func(g)
        time_taken = time.time()-start
        n+=5
        earlier_info=(n, g.approx_vert_cover, time_taken) # not what i wanted, change it!
        print(f"Currennt time for {func.__name__}: {time_taken}")

    return earlier_info

brute_max = test_max_graph(brute_force)
print(f"Brute Force in 2 min: {brute_max}")

smt_max = test_max_graph(smt_solver)
print(f"SMT Solver in 2 min: {smt_max}")