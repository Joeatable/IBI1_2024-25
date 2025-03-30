# import necessary libraries
import numpy as np
import matplotlib . pyplot as plt
N = 10000 # total population
I = 1 # initial number of infected individuals
R = 0 # initial number of recovered individuals
S = 9999 # initial number of susceptible individuals
beta = 0.3 # infection rate
gamma = 0.05 # recovery rate

S_arrays = [S] # array to store the number of susceptible individuals
I_arrays = [I] # array to store the number of infected individuals
R_arrays = [R] # array to store the number of recovered individuals

for i in range(1000): # simulate the time step
    if S == 0:  # insure that there exist the source of infection and people will be infected.
        new_I_individuals = 0
    elif I == 0:
        new_R_individuals = 0
    else:
        infection_prob = beta * ( I / N ) # the rate of infection is determined as beta*I/N
        infection_prob = np.clip (infection_prob,0,1)  # ensure the prob is between 0 and 1
        new_I_individuals = np.random.choice([0, 1], size=S, p=[1 - infection_prob, infection_prob]).sum() 
        # use np.random.choice to randomly select individuals to be infected,0 -> safe; 1 -> infected
        new_R_individuals = np.random.choice([0, 1], size=I, p=[1 - gamma, gamma]).sum()
        # use np.random.choice to randomly select individuals to be recovered ,0 -> infected; 1 -> recovered

    S = S - new_I_individuals # new number of susceptible individuals
    I = I + new_I_individuals - new_R_individuals # new number of infected individuals
    R = R + new_R_individuals # new number of number of recovered individuals

    S_arrays.append(S) # new arrays of susceptible、infected & recovered individuals
    I_arrays.append(I)
    R_arrays.append(R)

    
plt.figure(figsize = (6,6) , dpi =200) 
plt.plot(S_arrays, label = 'Susceptible', color = 'skyblue' , linewidth = 2) # draw three plots
plt.plot(I_arrays, label = 'Infected', color = 'crimson', linewidth = 2)
plt.plot(R_arrays, label = 'Recovered', color = 'darkgreen', linewidth = 2)
plt.xlabel('Time Steps') # define x/y labels
plt.ylabel('Number of Individuals')
plt.title('SIR Model') # define title
plt.legend() 
plt.savefig("/Users/joey/Desktop/IBI_2024-25/IBI1_2024-25/Practical 6/SIR_plot.png") #save them in my file 
plt.show() #show the plot