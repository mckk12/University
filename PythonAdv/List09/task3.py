import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def LangtonsAnt(n, iterations=1000):

    matrix = np.ones([n, n], dtype=np.float32)
    ant_img = mpimg.imread('ant.png')  
    ant_img = np.rot90(ant_img, k=2)  
    
    x, y = n // 2 - 1, n // 2 - 1  
    direction = 3  

    with plt.ion():  
        fig, ax = plt.subplots()
        mx_plot = ax.imshow(matrix, cmap='gray', interpolation='none', vmin=0, vmax=1) 
        ant_plot = ax.imshow(ant_img, extent=(y - 0.5, y + 0.5, x - 0.5, x + 0.5)) 
        
        ax.set_xlim(-0.5, n - 0.5)
        ax.set_ylim(n - 0.5, -0.5)

        for _ in range(iterations):
            if matrix[x, y] == 1.0:  # white square
                matrix[x, y] = 0.0
                direction = (direction + 1) % 4
            else:  # black square
                matrix[x, y] = 1.0
                direction = (direction - 1) % 4

            x = (x + [-1, 0, 1, 0][direction]) % n
            y = (y + [0, 1, 0, -1][direction]) % n

            rot_ant = np.rot90(ant_img, k=direction)
            mx_plot.set_data(matrix)
            ant_plot.set_data(rot_ant)  
            ant_plot.set_extent((y - 0.5, y + 0.5, x - 0.5, x + 0.5))  
            plt.pause(0.3)   
    plt.show()

LangtonsAnt(10, 10)
