#It is a game "Word Puzzle"
# Computer asks the user to guess the letter in the  word which it selected randomly from a list
# User enters the letter and check if it's the same letter which is missing from the word which computer genererated


# for using the random function
import random


# Main function
def main():
    # For genereating a random number between 0 and 5
    number = random.randint(0, 5)
    list_of_words = ['apple', 'banana', 'watermelon', 'kiwi', 'pineapple', 'mango']
    
    #for storing the user input as combination of "_" and user inputed digit
    fake_list=[]
    #for printing the the answer so far
    counter=0
    loop_counter=0
    
    
    #reading from file
    
    infile = open('intructions.txt','r')
    intructions = infile.read()
    print(intructions)


    # printing the number of dashes in word

    print("The answer so far is ", end="")
    for word in list_of_words[number]:
        fake_list.append("_")
        print(fake_list[counter]," ",end="")
        counter+=1


    # user asked to enter the letter
    user_letter = input("\nGuess a letter: ")


    # user entered the correct or wrong letter is checked
    print("The answer so far is ", end="")

    # each letter in the word is checked with the user entered letter

    for character in list_of_words[number]:
        if user_letter == character:
            fake_list[loop_counter] = character

        print(fake_list[loop_counter]," ",end = "")
        loop_counter+=1

    # user letter presence is checked in the word to display the result

    if user_letter in list_of_words[number]:
        print("\nGood Job you fount the word", list_of_words[number])
    else:
        print("\nNot quite,the correct word was", list_of_words[number], ". Better luck next time")
              
    # Input from user is taken
    last_answer = input("Press Enter to end the game")

    # user entered ENTER to end the game is checked
    if last_answer == '':
        pass


# main function is called
main()