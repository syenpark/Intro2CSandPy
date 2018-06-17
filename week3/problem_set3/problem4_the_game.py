def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is', len(secretWord), 'letters long.')
    
    letters = []
    mistakes = 8
    
    while mistakes:
        print('-------------')
        print('You have', mistakes, 'guesses left.')
        print('Available letters:', getAvailableLetters(str(letters)))
        
        guess = input('Please guess a letter: ')
        guessInLowerCase = guess.lower()
        
        
        if guessInLowerCase in secretWord and guessInLowerCase not in letters:
            letters.append(guessInLowerCase)
            print('Good guess: ', getGuessedWord(secretWord, letters))
            if isWordGuessed(secretWord, letters):
                print('-------------')
                print('Congratulations, you won!')
                break
        elif guessInLowerCase in letters: 
            print('Oops! You\'ve already guessed that letter:', getGuessedWord(secretWord, letters)) 
        else:
            letters.append(guessInLowerCase)
            print('Oops! That letter is not in my word:', getGuessedWord(secretWord, letters))
            mistakes -= 1
    
    if not mistakes:
        print('-------------')
        print('Sorry, you ran out of guesses. The word was', secretWord) 
