import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


os.chdir("/Users/joey/Desktop/IBI1_2024-25/Practical 10") # Change working directory to where the data file is located and import the file
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

print(dalys_data.iloc[0,3]) # Iloc is used to access a group of rows and columns by integer position(s)
# dalys_data.iloc [row, column]
# dalys_data.iloc [row_start:row_end, column_start:column_end]

print(dalys_data.head()) # Display the first 5 rows of the dataframe
dalys_data.info()


print(dalys_data.iloc[0:10, 2])   # Show the third column (Year) for the first 10 rows

# The 10th year for which DALYs were recorded in Afghanistan is 1999


print(dalys_data.loc[dalys_data["Year"] == 1990, "DALYs"]) # Show all DALYs values for the year 1990 using Boolean indexing

# UK has more DALYs than France if above value is greater
uk = dalys_data.loc[dalys_data.Entity == "United Kingdom", ["DALYs", "Year"]] # Compare average DALYs between UK and France
france = dalys_data.loc[dalys_data.Entity == "France", ["DALYs", "Year"]]
print("UK Mean DALYs:", uk["DALYs"].mean())
print("France Mean DALYs:", france["DALYs"].mean())


# Plot DALYs in the UK over time
plt.plot(uk.Year, uk.DALYs, 'b+')
plt.xticks(uk.Year, rotation=-90)
plt.title("DALYs in the UK over Time")
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.tight_layout()
plt.show()

# Additional analysis: Compare DALYs between China and the UK over time
china = dalys_data.loc[dalys_data.Entity == "China", ["DALYs", "Year"]]
plt.plot(china.Year, china.DALYs, 'r-o', label='China')
plt.plot(uk.Year, uk.DALYs, 'b--s', label='United Kingdom')
plt.title("DALYs over Time: China vs United Kingdom")
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.xticks(china.Year, rotation=-90)
plt.legend()
plt.tight_layout()
plt.show()

# Calculate difference in DALYs between China and the UK for each year
a = np.array(china["DALYs"])
b = np.array(uk["DALYs"])
print(a - b)  # Positive values mean China > UK in DALYs
