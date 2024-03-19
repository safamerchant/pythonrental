#Coursework Version 4.7
#Date: 10/12/2023
#By: F330446 

'''
returning Module:
This module contains the function for returning a previously rented game. This also has
adds an update record to show the date of which the return has been made

- rent_game(): First verifies the customer ID (by the check_id function in database.py). 
Then prompts user to input game id, then checks in the Rental.txt for an entry that has the same
game_id and customer_id in that line, as well as the game being currently unavailable. If all of
these checkpoints are passed then the program overwrites that current line in the file to a new 
line which includes the game_id, rent_date, return_date, customer_id. 

'''
#-------------------------------------------------------
# Importing Files:
#-------------------------------------------------------

import feedbackManager as FM
import database as DB
from datetime import datetime #for the current date needed for return_date

#-------------------------------------------------------
#Function Defintions:
#-------------------------------------------------------

def return_game():
    customer_id = DB.check_id()
    if customer_id == "ERROR":
        print("Redirecting to menu...")
        return  # goes back to the main menu as an incorrect customer ID
    game_id = input("Enter game ID: ")
    try:
        with open("Game_Info.txt", "r") as game_file:
            print("Results:")
            for line in game_file:
                if game_id in line:  # Case-insensitive search
                    try:
                        with open("Rental.txt", "r+") as rental_file:
                                available = False  # Assume the game is available by default
                                for rental_line in rental_file:
                                    rental_game_id, _, return_date, _ = map(str.strip, rental_line.split(","))
                                    if game_id == rental_game_id and not return_date:        
                                        available = True  # Set to True empty return_date 
                                        break# No need to check further if the game is already found                        
                                if available:
                                    availability = "NOT AVAILABLE"
                                elif not available:
                                    availability = "AVAILABLE"
                                print(f"{line.strip()} - {game_id}:{availability}")
                                if availability == "NOT AVAILABLE":
                                    return_choice = input(f"Do you wish to return {game_id}? (Yes/No)").lower()
                                    if return_choice == "yes":  # Find the specific line in Rental.txt and overwrite it
                                                rental_file.seek(0)
                                                lines = rental_file.readlines()# read through file
                                                rental_file.seek(0)
                                                for n, rental_line in enumerate(lines):
                                                    rental_game_id, rent_date, _, rental_customer_id = rental_line.strip().split(",")
                                                    if game_id == rental_game_id and customer_id == rental_customer_id:
                                                        current_date = datetime.now().strftime("%Y-%m-%d")
                                                        new_line = f"{game_id},{rent_date},{current_date},{customer_id}\n"
                                                        lines[n] = new_line #replaces current line at 'n' in the file with the updated one
                                                        rental_file.seek(0) #needed to move file pointer for overwriting purpose
                                                        rental_file.writelines(lines) # writes the new line in
                                                        rental_file.truncate()# removes any remaining data
                                                        print("DONE!")
                                                        print("FEEDBACK:")#Feedback section begins here
                                                        FM.load_feedback("Game_Feedback.txt")
                                                        rating = int(input("Please enter a rating (out of 5):"))
                                                        if rating < 6:  
                                                            option = input("Would you like to leave a comment? (Yes/No)").lower()
                                                            if option == "yes":
                                                                comments = str(input("Enter any comments:"))
                                                            else:
                                                                comments = " "# Prepare the feedback data
                                                            feedback_data = f"{game_id}, {rating}, {comments}\n"# Write feedback to 'Game_Feedback.txt' ensures newline
                                                            with open('Game_Feedback.txt', 'a') as feedback_file:
                                                                feedback_file.write(feedback_data)# Call the existing add_feedback function with an empty comments string
                                                                FM.add_feedback(game_id, rating, " ", 'Game_Feedback.txt')
                                                                print("Thank you for the feedback")
                                                            return
                                                        elif rating > 5:
                                                            print("Sorry feedback incorrect, must be a rating out of 5")
                                                            return
                                                break  # Break out of the loop if game is found in game_file
                                    elif return_choice == "no":
                                        return
                                    else: 
                                        print("Sorry invalid input. Try again...")
                                        return
                                else:
                                    print(f"Sorry, cannot return as {game_id} is already Available")
                    except FileNotFoundError:
                        print("The 'Rental.txt' file is not found.")
                        break
                    except Exception as e:
                        print(f"An error occurred while processing 'Rental.txt': {e}")
                        break
    except FileNotFoundError:
        print("ERROR: The file 'Game_Info.txt' was not found.")
        
# ----------------------------------
# Test Cases:
# ----------------------------------
'''
if __name__ == "__main__":

    # Test cases to demonstrate the functions of return_game():
    import feedbackManager as FM
    # Test Case 1.1: A Successful return and feedback
    print("\n Test Case 1.1: A Successful return and feedback")
    customer_id.input= "wsxw"
    game_id.input="aab01"
    return_choice.input= "yes"
    rating.input="4"
    option.input="yes"
    comments.input="Loved it!"
    return_game()
    #Test Case 1.2: An Unsuccessful rental- incorrect ID
    print("\n Test Case 1.2: An Unsuccessful rental - incorrect ID")
    customer_id.input= "wery" #should show error 
    return_game()
    #Test Case 1.3: A Successful rental, unsuccessful feedback
    print("\n Test Case 1.3: A Successful rental, unsuccessful feedback")
    customer_id.input= "mold"
    game_id.input="aaa01"
    return_choice.input= "yes"
    rating.input="9"#should show error 
    return_game()

    #Resetting inputs to original state;
    customer_id.input= input
    return_choice.input= input
    rating.input=input
    option.input=input
    comments.input=input
    game_id.input=input
    '''