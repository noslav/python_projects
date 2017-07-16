print("Please think of a number between 0 and 100!")
minNo  = 0 
maxNo = 100

while True :
    bisectNo = (maxNo + minNo) / 2
    print("Is your secret number " + str(bisectNo) +'?')
    input = (raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. "))
    if (input == 'h'):
        maxNo = bisectNo 
    elif (input == 'l'):
        minNo = bisectNo
    elif (input == 'c'):
        break
    else:
        print("Sorry, I did not understand your input.")
print("Game over. Your secret number was: "+ str(bisectNo))