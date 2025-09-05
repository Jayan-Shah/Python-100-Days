import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
        'q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
        ]

numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','&','(',')','*','+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("\n How many letters do you want: "))
nr_symbols = int(input("\n How many symbols would you like: "))
nr_numbers= int(input("\nHow many numbers would you like: "))

total_length=nr_letters+nr_numbers+nr_symbols
password=""
password_List=[]

for i in range (0,nr_letters):
    password += random.choice(letters)
    password_List.append(random.choice(letters))
   
for i in range (0,nr_symbols):
    password += random.choice(symbols)
    password_List.append(random.choice(symbols))

for i in range (0,nr_numbers):
    password += random.choice(numbers)
    password_List.append(random.choice(numbers))

print(password)


# Randomisation of password with loops

password_index = []
password_final=''

while(len(password_index)<total_length):
    flag = 0
    random_choice = random.randint(0,total_length-1)
    
    for j in password_index: 
        if(j==random_choice):
            flag=1
            break
     
    if(flag==1):
        continue

    else:
       password_index.append(random_choice)
       password_final = password_final + password[random_choice] 


print(f"\n Final Password is: {password_final}")

# Using shuffle function-------------------------

# print(password_List)
random.shuffle(password_List)
# print(password_List)

password_final=''
for char in password_List:
    password_final+=char

print(password_final)