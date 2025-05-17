from enum import Enum

class Specialization(Enum):
    CARDIOLOGY = 1
    NEUROLOGY = 2
    ORTHOPEDICS = 3

# doctors dictionary
doctors = {}

# Add doctors
doctors["Dr. Bob"] = Specialization.CARDIOLOGY
doctors["Dr. John"] = Specialization.NEUROLOGY
doctors["Dr. T"] = Specialization.ORTHOPEDICS

print("Doctors after adding:")
for name, spec in doctors.items():
    print(name, ":", spec.name)

# Update Dr. T's specialization
doctors["Dr. T"] = Specialization.CARDIOLOGY

print("\nDoctors after update:")
for name, spec in doctors.items():
    print(name, ":", spec.name)

# Retrieve Dr. Bob's specialization
doc_name = "Dr. Bob"
if doc_name in doctors:
    print(f"\n{doc_name} specializes in {doctors[doc_name].name}")
else:
    print(f"\n{doc_name} not found")

# Delete Dr. John
del doctors["Dr. John"]

print("\nDoctors after deletion:")
for name, spec in doctors.items():
    print(name, ":", spec.name)

