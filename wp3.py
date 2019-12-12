# It is a game "Word Puzzle"
# Computer asks the user to guess the letter in the  word which it selected randomly from a list
# User enters the letter and check if it's the same letter which is missing from the word which computer genererated


# for using the random function
import random
num_guesses = 4
def display_instructions():
    infile = open('intructions.txt','r')
    intructions = infile.read()
    print(intructions)    
def display_result(is_win,answer):
    if is_win:
        print("\nGood Job you fount the word", answer)

    else:
        print("\nNot quite,the correct word was", answer, ". Better luck next time")


def is_word_found(puzzle):
    if not "_" in puzzle:
        flag=True

    else:
        flag=False

    return flag

def display_puzzle_string(puzzle,answer):

 # puzzle is displayed
    num=0
    for char in puzzle:
        print(puzzle[num], " ", end="")
        num=num+1



def get_guess(num_guesses):
    # user asked to enter the letter
    print("\nGuess a letter (", num_guesses, "guesses are remaining):", end="")
    user_letter = input("")
    print("The answer so far is ", end="")

    return user_letter

def update_puzzle_string(puzzle,answer,guess):
    # each letter in the word is checked with the user entered letter
    loop_counter = 0
    check = True
    global num_guesses

    for character in answer:
        if guess == character:
            updated = True
            if puzzle[loop_counter]== character:
                if check== True:
                    num_guesses-=1
                    check = False
            else:
                puzzle[loop_counter] = character
        

        loop_counter += 1


    if guess in answer:
        pass
    else:
        num_guesses = num_guesses - 1
        updated = False
        
    return updated






def play_game(puzzle,answer):
    run = True

    while run:
    # guess function is called to ask the user to enter the guess
    
        guess = get_guess(num_guesses)
    
    #update_puzzle_string is called to compare the user entered with the computer selected    
        updated= update_puzzle_string(puzzle,answer,guess)
        
    #display_puzzle_string is called to display the current state of the puzzle
    
        display_puzzle_string(puzzle,answer)
        
    #is_word_function is called to check if the user guessed all the letters correctly or not
        is_win=is_word_found(puzzle)
        
    # conditions are checked for getting out of the loop    
        if is_win:
            run = False
        if num_guesses == 0:
            run = False
    return is_win





# Main function
def main():
    # For genereating a random number between 0 and 5
    
    list_of_words = ['apple', 'banana', 'watermelon', 'kiwi', 'pineapple', 'mango']
    number = random.randint(0, len(list_of_words)-1)
    answer= list_of_words[number]
    puzzle=[]
    
    #printing Instructions
    
    display_instructions()



    #making puzzle list with "_"
    
    counter = 0
    print("The answer so far is ", end="")
    for word in answer:
        puzzle.append("_")
        print(puzzle[counter]," ",end="")
        counter+=1
    
    #play_game function is called
    
    is_win = play_game(puzzle,answer)
    
    #display_result is called to display the result if the user won or not        

    display_result(is_win,answer)
    
    # Input from user is taken
    last_answer = input("Press Enter to end the game")

    # user entered ENTER to end the game is checked
    if last_answer == '':
        pass


# main function is called
main()