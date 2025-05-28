import random

# Function to calculate the volume of paracetamol needed based on patient weight and syrup strength
def calculate_paracetamol_volume(weight, strength):
    # Validate weight is within safe dosing range
    if weight > 100 or weight < 10:
        return "Error: Weight must be between 10 and 100 kg."
    
    # Determine concentration in mg/ml based on label strength
    if strength == "120 mg/5 ml":
        concentration = 24  # 120 ÷ 5 = 24 mg/ml
    elif strength == "250 mg/5 ml":
        concentration = 50  # 250 ÷ 5 = 50 mg/ml
    else:
        return "Strength must be '120 mg/5 ml' or '250 mg/5 ml'."
    
    # Standard dosage is 15 mg per kg of body weight
    dose_mg = 15 * weight

    # Calculate the required volume in ml and round to 1 decimal place
    volume_ml = round(dose_mg / concentration, 1)

    return volume_ml



# Example：
# Generate a random test case for demonstration
weight_kg = round(random.uniform(5, 120), 1)  # Random weight between 5 and 120 kg
strength_choice = ["120 mg/5 ml", "250 mg/5 ml", "200 mg/5 ml"]  # Include one invalid option to test error handling
strength_mg_ml = random.choice(strength_choice)  # Randomly pick one strength


print("The weight of the patient is", weight_kg)
print("The strength of paracetamol is", strength_mg_ml)
print("The volume of paracetamol is", calculate_paracetamol_volume(weight_kg, strength_mg_ml))
