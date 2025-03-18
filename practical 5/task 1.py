language_users = { "JavaScript": 62.3, "HTML": 52.9, "Python":51, "SQL": 51, "TypeScript": 38.5 }  
# create a dictionary to store the usage percentage of different programming languages
print(language_users)  # print to display the data
import matplotlib.pyplot as plt  # import matplotlib's pyplot module to plot graphs
plt.figure(figsize = (12,8))    # create a new figure with size 12x8 inches
bars = plt.bar(language_users.keys(), language_users.values(), color = 'skyblue', edgecolor = 'black', width = 0.6) 
# create bar plot with the data from dictionary, x-axis: programming languages, y-axis: usage percentages,and it has black borders, bar width 0.6 (refer the usage and format of plt.bar )
plt.title("Programming Language Popularity", fontsize = 20)  # set the title and the font size
plt.bar_label(bars, fmt='%.1f', fontsize = 12)  #referring to CSDN to know how to add numbers on the bars
plt.xlabel("Programming Languages", fontsize = 16)
plt.ylabel("Usage Percentage of Programming Languages/(M) ", fontsize = 16) # label the x-axis and y-axis
plt.yticks([0, 20, 40, 60, 80, 100])    # set the tick marks with intervals of 20, from 0 to 100
plt.ylim(0,100)  # set the scale of y-axis, (0,100)
plt.show()

a = input("please inpout the Programming Language :  ")   # ask user to input a programming language name
# could also replace with # Programming Language = "Python"
if a in language_users:    #if "Python" in language_users:
    print(language_users[a])  # if the input exists in the dictionary keys, print its usage percentage
else:
	print(a, "not Found")   # if the input is not found, print a not found message
      