#Coursework Version 2.6
#Date: 28/11/2023
#By: F330446

'''
database Module:
This module contains the 3 functions which all read through the text files and
output needed information for the main functions such as renting, searching to function.

- check_id(): this checks the customer_id that is inputted by the user and then checks
the subscription_Info.txt for a matching customer_id. If there is no matches then an 
error message is outputted. This function is used in rent_game(), return_game().
- get_sub_type(): This function uses the previously entered customer_id and uses the
Subscription_Info.txt to find the line that contains the matching customer_id. Then 
from the same line picks up the subscription type, which can be either Basic or Premium.
- get_rental_limit(): This utilises the Rental.txt and counts how many video games a specific
customer_id has rented a game without returning it. Then this count is returned. To be used in
the renting.py file.

'''

#-------------------------------------------
# Importing Files:
#-------------------------------------------

import subscriptionManager as SM

#-------------------------------------------
# Function Definitions:
#-------------------------------------------

customer_id = None
def check_id():
    global customer_id
    #global raw_customer_id
    subscriptions = SM.load_subscriptions("Subscription_Info.txt")
    raw_customer_id = input("Please enter customer ID: ")
    customer_id = raw_customer_id.replace(" ", "")
    sub_type= SM.check_subscription(customer_id, subscriptions)
    found = False  # boolean to track if subscription_type is found
    with open("Subscription_Info.txt", "r") as sub_file:
        for line in sub_file:
            cus_ID, _, _, _ = line.strip().split(',')
            if customer_id == cus_ID:  # Check for exact match
                # _, subscription_type, _, _ = line.strip().split(',')
                # print(f"Subscription status for {customer_id}: {subscription_type.capitalize()}")
                print("Correct ID!")
                found = True
                return customer_id
    if not found:
        print(f"Customer ID {customer_id} not found in the 'subscription_Info'")
        error = "ERROR"
        return error
      
def get_sub_type():
    global customer_id
    found = False  # boolean to track if subscription_type is found
    with open("Subscription_Info.txt", "r") as sub_file:
        for line in sub_file:
            if customer_id in line:
                _, subscription_type, _, _ = line.strip().split(',')
                print(f"Subscription status for {customer_id}: {subscription_type.capitalize()}")
                found = True
                return subscription_type.capitalize()
        if not found:
            print(f"Customer ID {customer_id} not found in the subscription database.")

def get_rental_limit():
    count = 0
    try:
        with open ("Rental.txt","r") as rental_file:
            count= sum(1 for line in rental_file if customer_id in line and line.split(",")[2].strip() == "")
            return count
    except FileNotFoundError:
        print(" 'Rental.txt' is not found.")

# -----------------------------
# Main Program
# -----------------------------
'''
if __name__ == "__main__":

    # Test cases to demonstrate the functions of check_id():
    import subscriptionManager as SM
    # Test Case 1.1: A Successful ID
    print("\n Test Case 1.1: A Successful ID")
    subscriptions = SM.load_subscriptions("Subscription_Info.txt")
    raw_customer_id.input= "lkjh"
    check_id()
    #Test Case 1.2: An Unsuccessful ID
    print("\n Test Case 1.2: An Unsuccessful ID")
    subscriptions = SM.load_subscriptions("Subscription_Info.txt")
    raw_customer_id.input= "wery"
    check_id()

    # Test cases to demonstrate the functions of get_sub_type():
    # Test Case 2.1: A Successful ID
    print("\n Test Case 2.1: A Successful ID")
    customer_id.input = "lkjh"
    get_sub_type()
     #Test Case 2.2: An Unsuccessful ID
    print("\n Test Case 2.2: An Unsuccessful ID")
    customer_id.input= "wery"
    get_sub_type()

    # Test cases to demonstrate the functions of get_rental_limit():
    # Test Case 3.1: A Successful ID
    print("\n Test Case 3.1: A Successful ID")
    customer_id.input = "lkjh"
    get_rental_limit()
     #Test Case 3.2: An Unsuccessful ID
    print("\n Test Case 3.2: An Unsuccessful ID")
    customer_id.input= "wery"
    get_rental_limit()

    #Resetting inputs to original state;
    raw_customer_id.input = input
    customer_id.input= input
    '''