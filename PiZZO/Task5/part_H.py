import time
from vertex_cover import generate_random_graphs, brute_force, smt_solver
import matplotlib.pyplot as plt

# function that checks how much time does algortihm take to solve the problem of given graph size and k vertex cover
def func_timer(func, args):
    s2 = time.time()
    graph_info = []
    for arg in args:
        start = time.time()
        func(arg)
        graph_info.append((arg.size, arg.approx_vert_cover, time.time()-start))
    print(f"Time taken for {func.__name__}: {time.time()-s2}")
    return graph_info

graphs_for_testing = generate_random_graphs(100, 40)

# (size, k, time)
brute_info = func_timer(brute_force, graphs_for_testing)
smt_info = func_timer(smt_solver, graphs_for_testing)

# sort the data for better visualization
brute_info.sort(key=lambda x: x[1])
smt_info.sort(key=lambda x: x[1])
brute_info.sort(key=lambda x: x[0])
smt_info.sort(key=lambda x: x[0])

# plot the data
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(projection='3d')
ax.plot([x[0] for x in brute_info], [x[1] for x in brute_info], [x[2] for x in brute_info], label='Brute Force')
ax.plot([x[0] for x in smt_info], [x[1] for x in smt_info], [x[2] for x in smt_info], label='SMT Solver')
ax.set_xlabel('Graph Size')
ax.set_ylabel('k vertex cover')
ax.set_zlabel('Eval Time')
ax.set_title('Graph size vs k vs time')
ax.view_init(elev=10, azim=-50, roll=0)
plt.legend()
plt.show()



