#It is a game "Word Puzzle" 
#Computer asks the user to guess the letter in the  word which it selected randomly from a list
#User enters the letter and check if it's the same letter which is missing from the word which computer genererated


# for using the random function
import random                                         

# Main function
def main():     
    
    # For genereating a random number between 0 and 5
    number = random.randint(0,5)                      
    list_of_words = ['apple', 'banana', 'watermelon', 'kiwi', 'pineapple', 'mango']
    word = list_of_words[number]
    
    #slicing is done 
    puzzled_word = list_of_words[number][1:]           
    letter_missing = list_of_words[number][:1]
    
    
    print(" I'm thinking of a secret word. \n Try and guess the word. You can guess one letter at a time. \n Each time you guess I will show you which letters have been \n correctly guessed and which letters are still missing. \n You will have 4 guesses to guess all of the letters. Good luck!")
    
    
    print("The answer so far is  _",puzzled_word)

    
    #user asked to enter the letter
    user_letter = input("Guess a letter: ")    
    
    

    #user entered the correct or wrong letter is checked 
    if user_letter == letter_missing:                 
        print("Good job you found the word",word)
    else:
        print("Not quite the correct word was",word," Better luck next time")
        
    
    
    
    #Input from user is taken
    last_answer = input("Press Enter to end the game")
    
    
    
    #user entered ENTER to end the game is checked 
    if last_answer == '':                            
        pass
    
        
        
        
#main function is called   
main()         