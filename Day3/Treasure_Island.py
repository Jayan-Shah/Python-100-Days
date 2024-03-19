# Challenege of finding the treasure in the island
print("\n################################ Welcome To Treasure Island #########################################\n")
print("Your mission is to find the treasure-:")
print("You are at cross road ----- Where do you want to go? ------ \nLeft or Right??")
direction=input().lower()
if direction=="right":
    print("Game Over...Try next time")
else:
    print("You came to a lake --- There is an island in the middle of the lake --- \nType 'wait' to wait for boat...Type 'swim' to to swim across")
    boat_swim=input().lower()
    if boat_swim == "swim":
        print("Game Over...Please try next time")
    else:
        print("You arrived at the island unharmed...\nThere is a house with three doors...\nOne red one blue and one yellow..\nWhich color do you choose")
        color=input().lower()
        if color == "yellow" or color == "blue":
            print("Game Over..Please Try Next Time..")
        else:
            print("Congratulations!!!.....You won the treasure..Use it wisely")


