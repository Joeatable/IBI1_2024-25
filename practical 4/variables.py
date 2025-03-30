a = 15 #walk to bus station
b = 75 #bus time
c = a + b #T=total time for bus option
d = 90 #driving time
e = 5 #walk to the office
f = d + e #total time for car option
if c < f :
    print ("by bus")
elif c == f:
    print("the same")
else:
    print("by car") 

# bus is faster

#Boolean variable setup 
X = True
Y = False
W = X and Y

# Truth table for W:
#   X   ｜   Y   ｜ W = X+Y |
#  True     True     True   
#  True     False    False 
#  False    True     False
#  False    False    False 