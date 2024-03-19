#Coursework Version 3.4
#Date: 05/12/2023
#By: F330446 

'''
saerching Module:
This module contains the function for searching for any term within the Game_Info.txt
this can be a title, platform, genre as prompted. It also displays the avaiability of
of the games that match the searched word.

- search_game(): First opens Game_Info.txt to read through it and find a match to the 
inputted serch_term. The search_term, and file info is converted to lowercase before
the matching to prevent mismatch due to case difference. Then once it has found a term,
from the same line in Game_Info it uses the game_id to check the availibility of the 
game by opening Rental.txt and checks if the game_id is on a line with an empty return_date
if so then outputs the game's info from Game_Info and then NOT AVAILABLE. If no empty
return_date is found then AVAILABLE instead of NOT AVAILABLE is outputted.  

'''
#-------------------------------------------------------
# Function Definitions:
#-------------------------------------------------------
availability= None

def search_game():
    global availability
    search_term = input("Please enter a term (title, genre, or platform) related to the game: ")
    try:
        with open("Game_Info.txt", "r") as game_file:
            print("Results:")
            for line in game_file:
                search_values = line.strip().split(",")
                game_id = search_values[0]  # this is the first element in line
                if search_term.lower() in line.lower():  # Case-insensitive search
                    try:
                        with open("Rental.txt", "r") as rental_file:
                            available = False  # Assume the game is available by default
                            for rental_line in rental_file:
                                    rental_game_id, _, return_date, _ = map(str.strip, rental_line.split(","))
                                    if game_id == rental_game_id and not return_date:
                                        available = True  # Set to False if there is a non-empty return_date
                                        break  # No need to check further  
                            if available:
                                availability = "NOT AVAILABLE"
                            elif not available:
                                availability = "AVAILABLE"
                            print(f"{line.strip()} - {game_id}:{availability}")
                    except FileNotFoundError:
                        print("The 'Rental.txt' file is not found.")
                        break
                    except Exception as e:
                        print(f"An error occurred while processing 'Rental.txt': {e}")
                        break
    except FileNotFoundError:
        print("ERROR: The file 'Game_Info.txt' was not found.")

#-------------------------------------------------------
# Test Cases:
#-------------------------------------------------------
'''
if __name__ == "__main__":

    # Test cases to demonstrate the functions of search_game():
    # Test Case 1.1: A Successful search term
    print("\n Test Case 1.1: A Successful search term")
    search_term.input="Horror"
    search_game()
    #Test Case 1.2: An Unsuccessful search term
    print("\n Test Case 1.2: An Unsuccessful search term")
    search_term.input="@"
    search_game()

    #Resetting inputs to original state;
    search_term.input = input
    customer_id.input= input
'''