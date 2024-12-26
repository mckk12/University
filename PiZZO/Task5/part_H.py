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
# smt_info = func_timer(smt_solver, graphs_for_testing)
# brute_info = func_timer(brute_force, graphs_for_testing)

# # print the data into 2 files
# with open('brute_info.txt', 'w') as f:
#     for x in brute_info:
#         f.write(f"{x[0]} {x[1]} {x[2]}\n")
# with open('smt_info.txt', 'w') as f:
#     for x in smt_info:
#         f.write(f"{x[0]} {x[1]} {x[2]}\n")

with open('brute_info.txt', 'r') as f:
    brute_info = []
    brute_info = f.readlines()
    brute_info = [x.strip().split() for x in brute_info]
    brute_info = [(int(x[0]), int(x[1]), float(x[2])) for x in brute_info]

with open('smt_info.txt', 'r') as f:
    smt_info = []
    smt_info = f.readlines()
    smt_info = [x.strip().split() for x in smt_info]
    smt_info = [(int(x[0]), int(x[1]), float(x[2])) for x in smt_info]


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

brute_info = brute_info[90:]
smt_info = smt_info[90:]
# plot the data
ks = [(x[1]+10)*2 for x in brute_info] # +10 for better visualization
plt.scatter([x[0] for x in brute_info], [x[2] for x in brute_info], label='Brute Force', s=ks) #size of the ball changes with k
ks = [(x[1]+10)*2 for x in smt_info]
plt.scatter([x[0] for x in smt_info], [x[2] for x in smt_info], label='SMT Solver', s=ks) 
plt.xlabel('Graph Size')
plt.ylabel('Time')
plt.title('Graph size vs time')
plt.legend()
plt.show()

