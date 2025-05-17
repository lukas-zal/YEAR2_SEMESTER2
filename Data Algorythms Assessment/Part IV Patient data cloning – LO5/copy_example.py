import copy

class Patient:
    def __init__(self, name, age, diagnosis, address):
        self.name = name
        self.age = age
        self.diagnosis = diagnosis
        self.address = address  # we assume address is a dictionairy 
    def __repr__(self):
        return f"Patient(name={self.name}, age={self.age}, diagnosis={self.diagnosis}, address={self.address})"

# original patient record
original_patient = Patient(
    "Alice",
    30,
    "Flu",
    {"street": "Amalias 52", "city": "Athens"}
)

# shallow copy
shallow_copied_patient = copy.copy(original_patient)
# deep copy
deep_copied_patient = copy.deepcopy(original_patient)

print("Before changes:")
print("Original:", original_patient)
print("Shallow Copy:", shallow_copied_patient)
print("Deep Copy:", deep_copied_patient)

# modifying shallow copy's address, DOES affect the original record
shallow_copied_patient.address["street"] = "Amalias 142"
# modifying deep copy's diagnosis, DOES NOT affect the original record
deep_copied_patient.diagnosis = "Cold"

print("\nAfter changes:")
print("Original:", original_patient)
print("Shallow Copy:", shallow_copied_patient)
print("Deep Copy:", deep_copied_patient)
