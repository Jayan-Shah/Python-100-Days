import random
import my_module

row1 = ['⬜','⬜','⬜']
row2 = ['⬜','⬜','⬜']
row3 = ['⬜','⬜','⬜']

map=[row1,row2,row3]
print(f'{row1}\n{row2}\n{row3}')

print("Enter where you want to try your luck..")
horizontal_choice = int(input("Enter you choice row number: "))-1
vertical_choice=int(input("Enter you choice columnn number:")) -1

horizontal_row = random.randint(0,2)
vertical_row=random.randint(0,2)

if horizontal_choice == horizontal_row and vertical_choice==vertical_row:
    map[horizontal_choice][vertical_choice]='💰'
    print("\nYou won your treasure...Use wisely...")


else:
    print("\nYou lost..Better Luck next time")
    map[horizontal_choice][vertical_choice]='👎'

print(f'\n{row1}\n{row2}\n{row3}')