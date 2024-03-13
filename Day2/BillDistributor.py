
# Program takes input of overall bill and distribute among people 
print("\n##################################### Welcome to Tip Calculator ############################################\n ")

expense = float(input("What was your total bill: Rs "))
tip_percent=float(input("What percentage of tip you want to give on expense: "))
number_people=int(input("Among how many people you want to distribute the bill: "))
tip_amount= (tip_percent/100)*expense
print(f"\nThe amount everyone has to pay is : Rs {round(((expense+tip_amount)/number_people),2)} ")



