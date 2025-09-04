import random
import my_module

namesAsCSV=input("Enter all the names separating by comma: ")
names=namesAsCSV.split(", ")

random_choice = random.randint(0,len(names)-1)

print(f"The bill is going to be paid by {names[random_choice]}") 
