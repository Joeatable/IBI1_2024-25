uk_pops = [57.11, 3.13, 1.91, 5.45]   # define a list of population number for countries in the UK
uk_cons = ["England", "Wales", "Northern Ireland", "Scotland"]   # define the country names in the UK
prc_pops = [65.77, 41.88, 45.28, 61.27, 85.15]   # define population number for Zhejiang province and its neighboring provinces
prc_pros = ["Zhejiang", "Fujian", "Jiangxi", "Anhui", "Jiangsu"]  # define the names of Zhejiang and its neighboring provinces
print("Sorted UK population : ", sorted(uk_pops))
print("Sorted China population : ", sorted(prc_pops))  # print the UK and China population list in ascending order
import matplotlib.pyplot as plt  # import module of pie-chart 
labels1 = uk_cons  # labels = country names
sizes1 = sorted(uk_pops)   # data = sorted UK populations
colors1 = ['darkgreen', 'mediumspringgreen', 'lightseagreen', 'deepskyblue']  # colors is referring to the matplotlib color chart
plt.figure(figsize = (9,9))  # create a 9x9 inch figure for the UK pie chart
plt.pie(sizes1, labels = labels1, colors = colors1, autopct = '%1.1f%%')  # draw pie chart for UK populations with labels and colors and percentage
plt.title("The Pie chart of UK ")  # set chart title
plt.legend(title = "UK Countries", loc = "upper right") 
plt.tight_layout()  # add legend at upper right, and not combining with pie chart
plt.show()  # display the UK pie chart
del prc_pros[0]  # delete Zhejiang Province
prc_pops.remove(65.77)  # delete the population of Zhejiang Province
labels2 = prc_pros   # the same as upper ones, just change the label name
sizes2 = sorted(prc_pops)
colors2 = ['darkviolet', 'violet', 'deeppink', 'crimson']
plt.figure(figsize = (9,9))
plt.pie(sizes2, labels = labels2, colors = colors2, autopct = '%1.1f%%')
plt.title("The Pie chart of China ")
plt.legend(title = "Zhejiang-neighboring provinces", loc = "upper right")
plt.tight_layout()
plt.show()  # display the China pie chart

# Question: how to let the two pie chart present in the same layer ? how to show the data of populations instead of percentage?