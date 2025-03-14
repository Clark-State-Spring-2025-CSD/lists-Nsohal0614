#Create two seperate lists for player one and player two. 
#Each one should contain 10 random numbers between 1 and 50.
#Do NOT sort the lists.
#Compare the lists in order. Whichever list has the higher number wins.
#Keep track of how many times each list wins.
#Find the highest number in each list and it's index. If the number occers multiple times take the first instsance.
#Find the lowest number in each list and it's index. If the number occers multiple times take the first instsance.
#A tie is not record as a win for either player
#Display the lists
#Report to the user how many times each player won and the information from lines 6 and 7.
#For the example output I am limiting the range to 1 to 9 to keep it more readable.

#Player One = [5,7,2,9,1,1,3,8,6,9]
#Player Two = [3,8,5,5,8,1,4,7,4,7]
#Player one won 5 times
#Player two won 4 times
#Player one's highest number is 9 at index 3
#Player two's highest number is 8 at index 1
#Player one's lowest number is 1 at index 4
#Player two's lowest number is 1 at index 5

import random

player1 = [random.randint(1, 50) for i in range(10)]
player2 = [random.randint(1, 50) for i in range(10)]

print(f"Player One = {player1}")
print(f"Player Two = {player2}")

player1Wins = 0
player2Wins = 0 

for i in range(10):
    if player1[i] > player2[i]:
        player1Wins += 1
    elif player1[i] < player2[i]:
        player2Wins += 1

print(f"Player one won {player1Wins} times")
print(f"Player two won {player2Wins} times")

max1, min1 = max(player1), min(player1)
max2, min2 = max(player2), min(player2)

max1Index = player1.index(max1)
min1Index = player1.index(min1)
max2Index = player2.index(max2)
min2Index = player2.index(min2)

print(f"Player one's highest number is {max1} at index {max1Index}")
print(f"Player two's highest number is {max2} at index {max2Index}")
print(f"Player one's lowest number is {min1} at index {min1Index}")
print(f"Player two's lowest number is {min1} at index {min2Index}")
