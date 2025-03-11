# i have to find some changing rules of the ball number
# Tn = n(n+1)/2 so we could us for loop to calculate the 10 and before 
# i have to remind that range could not get the last one 
# i can use int to discard the ".0"

for i in range (1,11):
    n = i*(i+1)/2               #Tn = n(n+1)/2
    n = int(n)                  #int to discard the ".0"
    print ("n = ",i,"  Tn = ",n)