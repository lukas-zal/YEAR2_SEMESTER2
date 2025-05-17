class Node:
    def __init__(self, data, priority=10):  # i set default priority to 10 for regular patients 
        self.data = data
        self.priority = priority
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
    
    def enqueue(self, patient_name, emergency=False, priority=None):
        if not emergency:
            priority = 10
        elif priority is None:
            priority = 0  # default emergency queue priority 
        
        new_node = Node(patient_name, priority)
        
        # insert by priority - lower number means higher priority
        if self.front is None or priority < self.front.priority:
            new_node.next = self.front
            self.front = new_node
        else:
            current = self.front
            while current.next and current.next.priority <= priority:
                current = current.next
            new_node.next = current.next
            current.next = new_node
        
        if emergency:
            print(f"{patient_name} (Priority {priority}) added as emergency.")
        else:
            print(f"{patient_name} added as regular patient.")
    
    def dequeue(self):
        if self.front is None:
            print("No patients in line.")
            return
        patient = self.front.data
        priority = self.front.priority
        self.front = self.front.next
        if priority == 10:
            print(f"{patient} is being served from the regular queue.")
        else:
            print(f"{patient} (Priority {priority}) is being served from the emergency queue.")
    
    def display(self):
        current = self.front
        if current is None:
            print("Queue is empty.")
            return
        patients = []
        while current:
            if current.priority == 10:
                patients.append(f"{current.data} (Regular)")
            else:
                patients.append(f"{current.data} (Emergency Priority {current.priority})")
            current = current.next
        print("Queue: ", patients)


# QUEUE TEST


import random
import time

# Using the Queue class from above

def test_queue():
    queue = Queue()
    #Add some regular patients
    queue.enqueue("Patient_A")
    queue.enqueue("Patient_B")
    #Add emergency patients with different priorities (lower = higher priority)
    queue.enqueue("Emergency_John", emergency=True, priority=2)
    queue.enqueue("Emergency_Anne", emergency=True, priority=1)
    # Add more regular patients
    queue.enqueue("Patient_C")
    # Add another emergency with the default priority (highest priority)
    queue.enqueue("Emergency_Bob", emergency=True)
    # Display queue
    queue.display()

    # Serve all patients
    print("\nServing patients:")
    while queue.front:
        queue.dequeue()
        time.sleep(0.5)
test_queue()