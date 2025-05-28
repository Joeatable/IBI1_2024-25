# Define a class to store patient information
class patients():
    # Initialize the patient with name, age, date of latest admission, and medical history
    def __init__(self, name, age, date_of_latest_admission, medical_history):
        self.name = name
        self.age = age
        self.date_of_latest_admission = date_of_latest_admission
        self.medical_history = medical_history

    # Method to print all stored patient information in a readable format
    def print_information_of_patient(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Date of Latest Admission:", self.date_of_latest_admission)
        print("Medical History:", self.medical_history)

# Example: 
patient_1 = patients("Joey Chandler", "19", "2024-11-18", "No known allergies")
patient_1.print_information_of_patient()
