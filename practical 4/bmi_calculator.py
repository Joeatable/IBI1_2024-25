judge = input ("if you do not know your height in centimeters, input 000\nif you know, input 111\nmy choice is :  ") # prompt the user to indicate whether they know their height in cm
if judge == "000":   #if they do not know, they should input "000"
    ft = float(input ("Enter your height in feet and inches.\nYou are /ft and  "))
    in0 = float(input ("/in  "))
    h0 = 0.3048 * ft + 0.0254 * in0    #convert feet to meters: h0 = ft * 0.3048 ; inches to meters: h0 = h0 + in * 0.0254
    h = h0    #let h = h0 (final height in meters)
else:   #if they know, they should input "111" or something else
    h = float(input ("your height / m  :  ") )    #convert height to a float number
    while h >=3:    # assuming input is in cm
        h = h/100   # convert cm to meters: h = h / 100
w = float(input ("your weight / kg  :  "))     # ask the user to input their weight in kg
BMI_pure = w/h**2     # BMI = weight / height ** 2
BMI = round (BMI_pure, 1)    # round BMI to one decimal place
print ("Your BMI is ",BMI)      # print the calculated BMI value
if BMI < 18.5:                  # judge the condition of the body
    print ("\nYou are underweight\n")
elif 18.5 <= BMI <= 30: 
    print ("\nYou are normal weight\n")
else:
    print ("\nYou are obese\n") 