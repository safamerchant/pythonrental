#Coursework Version 1.7
#Date: 05/12/2023
#By: F330446

'''
renting Module:
This module contains the function for renting out video games, it also includes
functionalities to add details of a rented item to 'Rental.txt.' Before renting it 
checks the customer ID, and the rental limit of the customers subscription. 

- rent_game(): First verifies the customer ID (by the check_id function in database.py). 
Then prompts user to input game id, retrieves the subscription type of the user (by 
get_sub_type function in databse.py), and the rental limit of that subscription type
 (by the get_rental_limit function in subscriptionManager.py). If the game is available
 and the customer has not reached their rental limit, then allows customer to select
 'yes' to rent out the videogame. Records this rental in the Rental.txt

'''
#-------------------------------------
# Importing Files:
#-------------------------------------

import database as DB
import subscriptionManager as SM

#-------------------------------------
# Function Definition:
#-------------------------------------

def rent_game():
    customer_id = DB.check_id()
    if customer_id == "ERROR":
        print("Redirecting to menu... ")
    else:
        sub_status = DB.get_sub_type()
        rental_limit = SM.get_rental_limit(sub_status)
        #print(f"Subscription limit is {sub_status}")
        game_id = input("Enter game ID: ")
        found = False  # Boolean to track if game_id is found in game_file
        availability = None
        try:
            with open("Game_Info.txt", "r") as game_file:
                print("Results:")
                for line in game_file:
                    if game_id in line:  # Case-insensitive search
                        try:
                            with open("Rental.txt", "r") as rental_file:
                                available = False  # Assume the game is available by default
                                for rental_line in rental_file:
                                    rental_game_id, _, return_date, _ = map(str.strip, rental_line.split(","))
                                    if game_id == rental_game_id and not return_date:
                                        available = True  # Set to True empty return_date
                                      # No need to check further if the game is already found
                                        break 
                                if available:
                                    availability = "NOT AVAILABLE"
                                elif not available:
                                    availability = "AVAILABLE"
                                print(f"{line.strip()} - {game_id}:{availability}")
                                if availability == "AVAILABLE":
                                    found = True #if game_id is found
                                    count = DB.get_rental_limit()
                                    new_rental_limit = rental_limit - count
                                    print(f"Your current rental limit is {new_rental_limit}")
                                    if new_rental_limit > 0: # new rental limit got by substracting the subscription limit with the count (customers rented)
                                        print(f"{customer_id} can rent {new_rental_limit} more") # print how many more games can be rented
                                        confirm_rent = input(f"Do you wish to rent {game_id}? (Yes/No)").lower()
                                        if confirm_rent == "yes":
                                            try:
                                                with open("Rental.txt", "a") as rental_file:
                                                    from datetime import datetime# needed for the current time to be recorded
                                                    current_datetime = datetime.now()
                                                    format_date = current_datetime.strftime("%Y-%m-%d")
                                                    new_record = f"\n{game_id},{format_date}, ,{customer_id}"
                                                    rental_file.write(new_record)# writes new record
                                                    print("DONE!")
                                            except FileNotFoundError:
                                                print("The 'Rental.txt' file is not found")
                                                break
                                            except Exception as e:
                                                print(f"An error has occurred: {e}")
                                        else:
                                            print("Redirecting to menu...")
                                    else:
                                        print(f"Rental limit for {customer_id} is full. Cannot rent more games.")
                                        break  # Break out of the loop if the game is found in the game_file
                                else:
                                    print(f"Sorry cannot rent as {game_id} is {availability}")
                                    break  # Break out of the loop if the game is found in the game_file
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

    # Test cases to demonstrate the functions of rent_game():
    import subscriptionManager as SM
    # Test Case 1.1: A Successful rental
    print("\n Test Case 1.1: A Successful rental")
    customer_id.input= "lkjh"
    sub_status.input= "Premium"
    rental_limit.input = SM.get_rental_limit(sub_status)
    game_id.input="hre08"
    rent_game()
    #Test Case 1.2: An Unsuccessful rental- incorrect ID
    print("\n Test Case 1.2: An Unsuccessful rental - incorrect ID")
    customer_id.input= "wery" #should show error 
    rent_game()
    #Test Case 1.3: An Unsuccessful rental- incorrect sub_type
    print("\n Test Case 1.3: An Unsuccessful rental - incorrect sub_type")
    customer_id.input= "lkjh" 
    sub_status.input= "Hello"#should show error 
    rental_limit.input = SM.get_rental_limit(sub_status)
    rent_game()
    #Test Case 1.4: An Unsuccessful rental- incorrect game_id
    print("\n Test Case 1.4: An Unsuccessful rental - incorrect game_id")
    customer_id.input= "lkjh" 
    sub_status.input= "Premium"
    rental_limit.input = SM.get_rental_limit(sub_status)
    game_id.input= "low88"#should show error 
    rent_game()

    #Resetting inputs to original state;
    customer_id.input= input
    sub_type.input=input
    rental_limit.input=input
    game_id.input=input
    '''