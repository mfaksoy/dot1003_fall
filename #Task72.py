#Task72
unique_elements = set()
running = True

while running:
    element = input("Enter an element for set: ").strip()

    if element.lower() == "exit":
        running = False
        
    elif element in unique_elements:
        print(f"{element} is already in our set.")
        
    else:
        unique_elements.add(element)

for item in unique_elements:
    print(item)