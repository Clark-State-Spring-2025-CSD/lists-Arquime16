#prompt the user to enter 5 numbers. Store them in a list.
#Display the list as entered, small to large, and large to small
#Calculate and display the mean and median
#This is a guided practice. You can follow the video or your instructor will go
#over this in class


thisIsAList = ["hello", "world"]
thisIsATuple = ("hello", "world")

thisIsADictionary = {"word1": "hello", "word2": "world"} 
thisIsASet = {"hello", "world"}

print("line A: " + thisIsAList[0] + "," + thisIsATuple[1])

print("line B: " + thisIsADictionary["word1"] + ", " + thisIsADictionary["word2"])

theString = ""
for word in thisIsASet:
    if word == "hello": 
        theString = word
    else: theString = theString + ", " + word

print("line C: " + theString)
