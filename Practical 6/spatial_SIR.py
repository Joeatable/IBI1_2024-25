#import necessary libraries
import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

population = np.zeros((100,100)) #create a squre of susceptible individuals
x, y = random.randint(1,100), random.randint(1,100)
population[x,y] = 1 #primary infected people
time_step = [0, 20, 50, 100]
plots = { }

beta = 0.3
gamma = 0.05
for t in range (101) : #use for to simulate time step
    Ix, Iy = np.where(population == 1) #find all infected people
    for i in range (len(Ix)):
        x = Ix [i] #value the (x,y) of the infected one
        y = Iy [i]
        
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:  #except the infected one, make it as a origin of disease
                    continue
                nx, ny = dx + x, dy + y # determine the position of infected people

                if 0<= ny < 100 and 0 <= nx < 100:  #ensure that the neibors are within the range
                    if population[nx, ny] == 0 :  #if the neibors are susceptible individuals
                        if random.uniform(0,1) <= beta :
                            population[nx, ny] = 1  #mark the infected one as 1
        if random.uniform(0,1) <= gamma: #judge if the infecting individual have the oppotunity to recover
            population[x, y] = 2  #mark recovered individual as 2
    if t in time_step:
        plots[t] = population.copy()  #import the datas in plots

fig, axes = plt.subplots(1, len(time_step), figsize=(15, 4), dpi=200)
for idx, t in enumerate(time_step):
    axes[idx].imshow(plots[t], cmap= cm.get_cmap('viridis', 3), interpolation='nearest')
    axes[idx].set_title(f"Time {t}")
    axes[idx].axis('off')

plt.tight_layout()
plt.savefig('/Users/joey/Desktop/IBI_2024-25/IBI1_2024-25/Practical 6/spatial_SIR(2D).png')
plt.show()
