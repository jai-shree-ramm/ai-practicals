from random import choice
print("Time to play hangman!")
print("Start guessing...")
words = ['rainbow', 'computer', 'science', 'programming', 'python', 'mathematics', 'player', 'condition', 'reverse', 'water', 'board', 'geeks']
word = choice(words)
guesses = ''
turns = 10
while turns > 0:         
    failed = 0             
    for char in word:      
        if char in guesses:    
            print (char, end=" "),    
        else:
            print ("_", end=" "),     
            failed += 1
    if failed == 0:   
        print ("\nYou won")
        break            
    guess = input("\nGuess a character: ") 
    guesses += guess              
    if guess not in word:
        turns -= 1
        print ("Wrong")
        print ("You have", turns, 'more guesses')
        if turns == 0:
            print ("You Lose")
