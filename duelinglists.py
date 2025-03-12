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

#Be use the random module to generate the random numbers for each list.

import random

#Create two seperate lists for player one and player two.
#Each one should contain 10 random numbers between 1 and 50.
#Do NOT sort the lists.

playerOne = [4, 10, 12, 31, 22, 19, 41, 21, 33, 15]

playerTwo = [5, 14, 17, 23, 44, 38, 29, 11, 25, 30]

#Compare the lists in order. Whichever list has the higher number wins.

playerOneWins = 0
playerTwoWins = 0

for i in range(10):
    if playerOne[i] > playerTwo[i]:
        playerOneWins += 1
    elif playerTwo[i] > playerOne[i]:
        playerTwoWins += 1
    else:
        continue

#Keep track of how many times each list wins.
#Find the highest number in each list and it's index. If the number occers multiple times take the first instsance.
#Find the lowest number in each list and it's index. If the number occers multiple times take the first instsance.

playerOneHighest = max(playerOne)
playerOneHighestIndex = playerOne.index(playerOneHighest)
playerOneLowest = min(playerOne)
playerOneLowestIndex = playerOne.index(playerOneLowest)

playerTwoHighest = max(playerTwo)
playerTwoHighestIndex = playerTwo.index(playerTwoHighest)
playerTwoLowest = min(playerTwo)
playerTwoLowestIndex = playerTwo.index(playerTwoLowest)

#Display the Lists

print("Player One: ", playerOne)
print("Player Two: ", playerTwo)

#Report to the user how many times each player won and the information from lines 6 and 7.

print(f"Player one won {playerOneWins} times")
print(f"Player two won {playerTwoWins} times")
print(f"Player one's highest number is {playerOneHighest} at index {playerOneHighestIndex}")
print(f"Player two's highest number is {playerTwoHighest} at index {playerTwoHighestIndex}")
print(f"Player one's Lowest number is {playerOneLowest} at index {playerOneLowestIndex}")
print(f"Player two's Lowest number is {playerTwoLowest} at index {playerTwoLowestIndex}")

#I got the help of copilot for to do this code. 






