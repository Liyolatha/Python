#Loops Control Statements(for)

fruits = ["Apple", "Banana", "Cherry", "Date"]

for fruit in fruits:
    if fruit == "Cherry":
     break # Exit the loop if cherry is found
    print(fruit)
    
print()

for fruit in fruits:
    if fruit == "Cherry":
     continue # Skips the chery and moves to the iteration
    print(fruit)
    
    
print()

for fruit in fruits:
    if fruit == "Cherry":
     pass #placeholder, no action is needes for cherry
    print(fruit)