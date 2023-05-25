# Hospitals and medical facilities
# Define a list to store patient information
patients = []

# Define a list to store appointments
appointments = []

# Function to add patient information
def add_patient():
    name = input("Enter patient name: ")
    age = int(input("Enter patient age: "))
    gender = input("Enter patient gender: ")
    address = input("Enter patient address: ")
    phone = input("Enter patient phone number: ")
    patient = {"name": name, "age": age, "gender": gender, "address": address, "phone": phone}
    patients.append(patient)
    print("Patient added successfully!")

# Function to view patient information
def view_patients():
    for patient in patients:
        print("Name:", patient["name"])
        print("Age:", patient["age"])
        print("Gender:", patient["gender"])
        print("Address:", patient["address"])
        print("Phone:", patient["phone"])
        print()

# Function to update patient information
def update_patient():
    name = input("Enter patient name to update: ")
    for patient in patients:
        if patient["name"] == name:
            patient["age"] = int(input("Enter new age: "))
            patient["gender"] = input("Enter new gender: ")
            patient["address"] = input("Enter new address: ")
            patient["phone"] = input("Enter new phone number: ")
            print("Patient information updated successfully!")
            return
    print("Patient not found.")

# Function to schedule an appointment
def schedule_appointment():
    name = input("Enter patient name: ")
    for patient in patients:
        if patient["name"] == name:
            date = input("Enter appointment date (MM/DD/YYYY): ")
            time = input("Enter appointment time (HH:MM AM/PM): ")
            appointment = {"name": name, "date": date, "time": time}
            appointments.append(appointment)
            print("Appointment scheduled successfully!")
            return
    print("Patient not found.")

# Function to view appointments
def view_appointments():
    for appointment in appointments:
        print("Name:", appointment["name"])
        print("Date:", appointment["date"])
        print("Time:", appointment["time"])
        print()

# Main program loop
while True:
    print("Choose an option:")
    print("1. Add patient information")
    print("2. View patient information")
    print("3. Update patient information")
    print("4. Schedule an appointment")
    print("5. View appointments")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_patient()
    elif choice == 2:
        view_patients()
    elif choice == 3:
        update_patient()
    elif choice == 4:
        schedule_appointment()
    elif choice == 5:
        view_appointments()
    elif choice == 6:
        break
    else:
        print("Invalid choice. Please try again.")
