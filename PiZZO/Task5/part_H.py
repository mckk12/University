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

def plot_graph_info(graph_info, title):
    graph_info.sort(key=lambda x: x[0])
    sizes = [info[0] for info in graph_info]
    times = [info[2] for info in graph_info]

    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.plot(sizes, times, c='blue', label='Size vs Time')
    plt.xlabel('Graph Size')
    plt.ylabel('Time (s)')
    plt.title(f'{title} - Size vs Time')
    plt.legend()

    
    graph_info.sort(key=lambda x: x[1])
    times = [info[2] for info in graph_info]
    k_values = [info[1] for info in graph_info]

    plt.subplot(1, 2, 2)
    plt.plot(k_values, times, c='red', label='K vs Time')
    plt.xlabel('K (Vertex Cover Size)')
    plt.ylabel('Time (s)')
    plt.title(f'{title} - K vs Time')
    plt.legend()

    plt.tight_layout()
    plt.show()

graphs_for_testing = generate_random_graphs(10, 30)

# (size, k, time)
brute_info = func_timer(brute_force, graphs_for_testing)
smt_info = func_timer(smt_solver, graphs_for_testing)

plot_graph_info(brute_info, 'Brute Force')
plot_graph_info(smt_info, 'SMT Solver')

