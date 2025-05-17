import random
import string
import time

import random, string, time

sort_key = "name"

class Patient:
    def __init__(self, patient_id, name, age, diagnosis):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.diagnosis = diagnosis

def set_sort_key(key):
    global sort_key
    sort_key = key

def _greater(a, b):
    return a.name > b.name if sort_key == "name" else a.age > b.age

def _equal(a, b):
    return a.name == b.name if sort_key == "name" else a.age == b.age

def _less(a, b):
    return a.name < b.name if sort_key == "name" else a.age < b.age

def bubble_sort(patients):
    n = len(patients)
    for i in range(n):
        for j in range(0, n - i - 1):
            if _greater(patients[j], patients[j + 1]):
                patients[j], patients[j + 1] = patients[j + 1], patients[j]
    return patients

def merge_sort(patients):
    if len(patients) <= 1:
        return patients
    mid = len(patients) // 2
    left = merge_sort(patients[:mid])
    right = merge_sort(patients[mid:])
    merged, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if _less(left[i], right[j]):
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

def quick_sort(patients):
    if len(patients) <= 1:
        return patients
    pivot = patients[0]
    less = [p for p in patients[1:] if _less(p, pivot)]
    equal = [p for p in patients if _equal(p, pivot)]
    greater = [p for p in patients[1:] if _greater(p, pivot)]
    return quick_sort(less) + equal + quick_sort(greater)

def linear_search(patients, target):
    for patient in patients:
        if _equal(patient, target):
            return patient
    return -1

def binary_search(patients, target):
    left, right = 0, len(patients) - 1
    while left <= right:
        mid = (left + right) // 2
        if _equal(patients[mid], target):
            return patients[mid]
        elif _less(patients[mid], target):
            left = mid + 1
        else:
            right = mid - 1
    return -1

def generate_patients(n):
    patients = []
    for i in range(n):
        pid = i + 1
        name = ''.join(random.choices(string.ascii_uppercase, k=5))
        age = random.randint(1, 100)
        diagnosis = random.choice(['Flu', 'Cold', 'Fracture', 'Allergy'])
        patients.append(Patient(pid, name, age, diagnosis))
    return patients

#GENERATE 100 RANDOM PATIENTS
num_patients = 100
patients = generate_patients(num_patients)

for key in ['name', 'age']:
    print(f"\nSorting by {key}:\n")
    set_sort_key(key)

    #Bubble Sort
    patients_copy = patients[:]
    start = time.perf_counter()
    bubble_sort(patients_copy)
    print(f"Bubble Sort Time: {time.perf_counter() - start:.6f} seconds")

    target = patients_copy[num_patients // 2]

    #Linear Search
    start = time.perf_counter()
    linear_search(patients_copy, target)
    print(f"Linear Search Time: {time.perf_counter() - start:.6f} seconds")

    #Binary Search
    start = time.perf_counter()
    binary_search(patients_copy, target)
    print(f"Binary Search Time: {time.perf_counter() - start:.6f} seconds")

    #Merge Sort
    patients_copy = patients[:]
    start = time.perf_counter()
    patients_copy = merge_sort(patients_copy)
    print(f"Merge Sort Time: {time.perf_counter() - start:.6f} seconds")

    target = patients_copy[num_patients // 2]

    #Linear Search
    start = time.perf_counter()
    linear_search(patients_copy, target)
    print(f"Linear Search Time: {time.perf_counter() - start:.6f} seconds")

    #Binary Search
    start = time.perf_counter()
    binary_search(patients_copy, target)
    print(f"Binary Search Time: {time.perf_counter() - start:.6f} seconds")

    #Quick Sort
    patients_copy = patients[:]
    start = time.perf_counter()
    patients_copy = quick_sort(patients_copy)
    print(f"Quick Sort Time: {time.perf_counter() - start:.6f} seconds")

    target = patients_copy[num_patients // 2]

    #Linear Search
    start = time.perf_counter()
    linear_search(patients_copy, target)
    print(f"Linear Search Time: {time.perf_counter() - start:.6f} seconds")

    #Binary Search
    start = time.perf_counter()
    binary_search(patients_copy, target)
    print(f"Binary Search Time: {time.perf_counter() - start:.6f} seconds")