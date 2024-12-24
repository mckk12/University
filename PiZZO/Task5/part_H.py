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

graphs_for_testing = generate_random_graphs(40)

# (size, k, time)
smt_info = func_timer(smt_solver, graphs_for_testing)
brute_info = func_timer(brute_force, graphs_for_testing)

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

#plot size vs time with k points
plt.plot([x[0] for x in brute_info], [x[2] for x in brute_info], label='Brute Force', color='red')
plt.plot([x[0] for x in smt_info], [x[2] for x in smt_info], label='SMT Solver', color='blue')
plt.scatter([x[1] for x in brute_info], [x[2] for x in brute_info], color='red')
plt.scatter([x[1] for x in smt_info], [x[2] for x in smt_info], color='blue')
plt.xlabel('Graph Size with k points')
plt.ylabel('Time')
plt.title('Graph size vs time with k points')
plt.legend()
plt.show()






