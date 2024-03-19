#Coursework Version 5.3
#Date: 10/12/2023
#By: Safa Merchant 

'''
inventorypruning Module:
This function analyzes game rental data, identifies the least popular games,
and provides the option to visualize this information through either a table 
or a bar chart, with special attention to games with very low rental frequencies
by showing their bars as red.

- inv_pruning(): Firstly the data is read from the Rental.txt and counts the 
frequency of each game based on the munber of times it has been rented out.
Then it determines 10 games with the lowest rental frequencies, then displays
a table showing the game IDs and their corresponding frequences. Then a prompt
is given to the user to display an optional bar chart. If user choses yes,
generates a bar chart, games with the rental frequency of 1 are highlighted red.
The code tells the user that the red games are recommended to be removed.

'''

#-------------------------------------
# Importing Files:
#-------------------------------------

import matplotlib.pyplot as plt

#--------------------------------------
# Function Definitions:
#--------------------------------------

def inv_pruning():
    try:
        frequency = {} #declare an empty dictionary 
        # Collect frequency from Rental.txt
        with open("Rental.txt", "r") as rental_file:
            for line in rental_file:
                game_id = line.split(",")[0].strip()#gets the game_ids
                frequency[game_id] = frequency.get(game_id, 0) + 1
        least_popular = sorted(frequency, key=frequency.get)[:10]#last 10 in frequency data are held
        print("\nTop 10 Least Popular Games:")
        print("GAME_ID          FREQUENCY")# printed in a table
        for game_id in least_popular:
            print(f"{game_id}               {frequency[game_id]}")
        option = input("Would you like to view the data in a bar chart? (Yes/No)").lower()
        if option == "yes":# Plotting the bar chart
            print("Recommended to remove games wih red bars in the bar chart")
            categories = least_popular
            values = [frequency[game_id] for game_id in least_popular]
            colors = ['red' if freq == 1 else 'blue' for freq in values]#colour red if 1 rental frequency
            plt.bar(categories, values, color=colors)
            plt.xlabel('Game IDs')
            plt.ylabel('No. of times rented')
            plt.title('Bar Chart to show rental frequency of 10 most unpopular games')
            plt.show()
        elif option == "no":
            return
    except FileNotFoundError:
        print("ERROR: The 'Rental.txt' file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# ----------------------------------
# Test Cases:
# ----------------------------------
'''
if __name__ == "__main__":

    # Test cases to demonstrate the functions of inv_pruning():
    # Test Case 1.1: A Successful display of table and bar chart
    print("\n Test Case 1.1: A Successful display of table and bar chart")
    option.input="yes"
    inv_pruning()
    #Test Case 1.2: An Successful display of table only
    print("\n Test Case 1.2: An Successful display of table only")
    option.input="no"
    inv_pruning()

    #Resetting inputs to original state;
    option.input=input
    '''

    

