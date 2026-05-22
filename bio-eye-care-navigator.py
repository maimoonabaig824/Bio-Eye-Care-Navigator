def check_eye_condition(age, symptom, eye_pressure):
    risk_score = age + eye_pressure
    condition = ""
    severity = ""

    if symptom == "flash":
        if age > 50 or eye_pressure > 21:
            condition = "Retinal Problem"
            severity = "Critical"
        else:
            condition = "Minor Eye Issue"
            severity = "Abnormal"

    elif symptom == "blurry":
        if age > 40:
            condition = "Possible Cataract"
            severity = "Abnormal"
        else:
            condition = "Weak Vision"
            severity = "Normal"

    elif symptom == "red":
        if eye_pressure > 24:
            condition = "Glaucoma Risk"
            severity = "Critical"
        else:
            condition = "Eye Allergy"
            severity = "Normal"

    else:
        condition = "Eye Strain"
        severity = "Normal"

    return condition, severity, risk_score


patients = []

while True:
    print("\nEnter Patient Details")

    name = input("Enter patient name: ")

    age = int(input("Enter age: "))
    if age <= 0:
        print("Invalid age! Skipping...")
        continue

    symptom = input("Enter symptom (flash / blurry / red / strain): ").lower()
    if symptom not in ["flash", "blurry", "red", "strain"]:
        print("Invalid symptom! Using default: strain")
        symptom = "strain"

    eye_pressure = int(input("Enter eye pressure: "))
    if eye_pressure <= 0:
        print("Invalid eye pressure! Skipping...")
        continue

    condition, severity, risk_score = check_eye_condition(age, symptom, eye_pressure)

    patient_data = {
        "Name": name,
        "Age": age,
        "Symptom": symptom,
        "Eye Pressure": eye_pressure,
        "Condition": condition,
        "Severity": severity,
        "Risk Score": risk_score
    }

    patients.append(patient_data)

    print("\n--- Patient Report ---")
    print("Name:", name)
    print("Age:", age)
    print("Symptom:", symptom)
    print("Eye Pressure:", eye_pressure)
    print("Condition:", condition)
    print("Severity:", severity)
    print("Risk Score:", risk_score)

    choice = input("\nDo you want to enter another patient? (yes/no): ").lower()
    if choice != "yes":
        break


print("\n--- All Patients ---")
for p in patients:
    print(p)