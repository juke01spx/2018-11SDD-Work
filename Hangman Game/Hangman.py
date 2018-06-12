import random
fn = "hangwords.txt"

def displayWords(guessLetters, guessWord):
	displayWord = ""
	guessIt = True
	for character in guessWord:
		if character in guessLetters:
			displayWord += f" {character}"
		else:
			displayWord += f" _"
			guessIt = False
	return guessIt
	print(displayWord)

def getWord():
	#1. Read in word list from a file.
	wl = []
	with open(fn,"r") as wf:
		for word in wf:
			wl.append(word.strip().lower())
	
	#2. Randomly choose a word to guess.
	
	guessWord = random.choice(wl)
	return guessWord
	
def getLetter():
	### Play game.
		## Keep type a letter in.
		## It must be only 1 character.
		## It must not already be used.
		## It must be a letter of the alphabet.
	while True:	
		guess = input("Guess a letter: ").lower().strip()
			
		if len(guess) != 1:
			print("One letter please")
		elif guess in guessLetters:
			print(f"'{guess}' Already used : Letters guessed so far: '{guessLetters}'")
		elif guess not in "abcdefghijklmnopqrstuvwxyz":
			print(f"'{guess}' must be a letter of the alphabet")
		else:
			break ## Continue with game if letter is ok.
	return guess
	
	
#### MAIN GAME ####	
def hangMan():
	guessWord = getWord() #get a random word
	#print(guessWord)
	guessLetters = ""
	
	#3. Display _ for each letter.
	#guessed = displayWords(guessLetters, guessWord)
			
	#4. Get a guess and process it.
	lives = 10
	
	while True:
		guessIt = displayWords(guessLetters, guessWord)
		drawHangman(lives)
		if guessIt:
			print("Well done! You guess it with {lives} lives left")
			break
		if lives < 1:
			print("You've been pranked!")
			break
			
		
			
		guess = getLetter()
		guessLetters += guess
		
		if guess not in guessWord:
			lives -= 1
			
			
			
while True:
	play = input("Do you want to play?").lower().strip()
	if "y" in play:
		hangMan()
	else:
		break
			
		
hangMan()
