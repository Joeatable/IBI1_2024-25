# Prompt the user to indicate whether they know their height in cm:
#     If they **do not know**, they should input "000"
#     If they **know**, they should input "111"

# If the user inputs "000" (does not know height):
#     Ask the user to input their height in feet (ft) and inches (in)
#     Convert feet to meters: h0 = ft * 0.3048
#     Convert inches to meters: h0 = h0 + in * 0.0254
#     Set h = h0 (final height in meters)

# If the user inputs "111" (knows height):
#     Ask the user to input their height in meters (m)
#     Convert input to a float number
#     If height is greater than or equal to 10 (assuming input is in cm):
#         Convert cm to meters: h = h / 100

# Ask the user to input their weight in kg
# Calculate BMI:
#     BMI = weight / (height ** 2)
#     Round BMI to **one decimal place**

# Print the calculated BMI value
# Determine BMI category:
#     If BMI < 18.5: Print "You are underweight"
#     If 18.5 ≤ BMI ≤ 30: Print "You have a normal weight"
#     Otherwise: Print "You are obese"



judge = input ("if you do not know your height in cm, input 000\nif you know, input 111\nmy choice is :  ")
if judge == "000":
    ft = float(input ("your are /ft and  "))
    in0 = float(input ("/in  "))
    h0 = 0.3048 * ft + 0.0254 * in0
    h = h0
else:
    h = float(input ("your height / m  :  ") )
    while h >=10:
        h = h/100
w = float(input ("your weight / kg  :  "))
BMI_pure = w/h**2
BMI = round (BMI_pure, 1)
print ("Your BMI is ",BMI)
if BMI < 18.5:
    print ("\nYou are underweight\n")
elif 18.5 <= BMI <= 30: 
    print ("\nYou are normal weight\n")
else:
    print ("\nYou are obese\n")