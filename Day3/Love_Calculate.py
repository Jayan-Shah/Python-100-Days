# Print the compatibility of your love by following method
print("Enter your name")
name=input().lower()
print("Enter your partners name")
name_partner=input().lower()
string_combined = name+name_partner
count_r=string_combined.count('r')
count_t=string_combined.count('t')
count_u=string_combined.count('u')
count_e=string_combined.count('e')
count_l=string_combined.count('l')
count_o=string_combined.count('o')
count_v=string_combined.count('v')
count_e=string_combined.count('e')
result=str(count_r+count_t+count_u+count_e) + str(count_l+count_o+count_v+count_e)
print(f"Your love compatibility is :{result} ")


