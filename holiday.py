''' In this city break holiday program, functions are used to calculate
the user's total holiday cost taking the user's input of city 
choice, number of nights stay in a hotel and the number of car-rental days.

First define the function for the total hotel cost with the number
of nights parameter.
The number of nights will be taken from the user input as the argument
and multiplied to the price per night which is £100.

Second, define the function for plane cost with city flight as the parameter.
There will be a choice of three city flights each with a different price.
Set up 'if elif statements' in this function so that the price of the 
city flight will be depend on the city chosen by user input.  
ie. the argument for this function will be the price of the city_flight.

Third, define the function for calculating total car rental cost.
The parameter for this function will be the number of rental days.
The price per day is £150 which will be multiplied to the argument
rental_days provided by user input.

Then define a function for calculating the total holiday cost in £.
This will have parameters set as total hotel cost, plane cost and
car rental cost.
This will return the total holiday cost.

Set up a welcome message for users.

Set up a while loop which will display the choices for users
to select the city choice until the user decides to exit the program.
For each city choice, allow the user to input the number of nights,
and rental days for car hire.

The function "holiday_cost" will be called to using the user input
arguments for num_nights, city_flight and rental_days.
For the user: Set up a f string to display the total holiday cost
including the name of the city, number of nights stay and rental days. 
'''


def hotel_cost(num_nights):
    """Function for calculating the total hotel cost (price per night £100).
    num_nights argument will be taken from the user input.
    """
    tot_hotel_cost = (num_nights) * 100
    return tot_hotel_cost



def plane_cost(city_flight):
    """Function for plane (flight) cost will return a price in £
    depending on the user's input for city_flight.
    """
    if city_flight == 1: # Flight to London
        return 500
    elif city_flight == 2: # Flight to Paris
        return 400
    elif city_flight == 3: # Flight to New York
        return 800
    else:
        return 0


  
def car_rental(rental_days):    
    """Function for calculating total car rental cost in £.
    The price per day is £150.  The number of rental_days will be taken
    from user input.
    """  
    tot_car_rental = (rental_days) * 150
    return tot_car_rental



def holiday_cost(hotel_cost, plane_cost,car_rental):
    """Function for calculating the total holiday cost in £.
    """
    tot_holiday_cost = hotel_cost + plane_cost + car_rental
    return tot_holiday_cost


# Welcome display for the user.
space = " "*35
print("*"*100)
print(f"{space}WELCOME TO CITY BREAKS{space}")
print("*"*100)
print()

city_flight = ""

while city_flight != 4: # The below user input will be requested until
                        # the user enters 4 to quit.
    
    print("Which city would you like to visit?\n")
    city_flight = int(input("Please enter a number 1 , 2, 3 or 4:\n\n\
1 for London city break\n2 for Paris city break\n\
3 for New York city break\n4 to  quit\n\n"))
    
    if city_flight == 1: # User input 1 for London city break.
        num_nights = int(input("\nEnter a number. How many nights would \
you like to stay in London?:\nNight(s): "))
        rental_days = int(input("\nEnter a number.  How many days would \
you like to rent a car?\nCar rental day(s): "))
        
        # The function "holiday_cost" is called to using the user input
        # arguments for num_nights, city_flight and rental_days.
        # The Total holiday cost is printed for London City break.
        print(f"\nFor {num_nights} night(s) stay with car hire for \
{rental_days} day(s), your London city break will cost:") 
        print(f"£ {holiday_cost(hotel_cost(num_nights), \
            plane_cost(city_flight), car_rental(rental_days))}\n")
        break
    
    elif city_flight == 2: # User input 2 for Paris city break.
        num_nights = int(input("\nEnter a number. How many nights would \
you like to stay in Paris?:\nNight(s): "))
        rental_days = int(input("\nEnter a number.  How many days would \
you like to rent a car?\nCar rental day(s): "))
        
        print(f"\nFor {num_nights} night(s) stay with car hire for \
{rental_days} day(s), your Paris city break will cost:") 
        print(f"£ {holiday_cost(hotel_cost(num_nights), \
            plane_cost(city_flight), car_rental(rental_days))}\n")
        break
    
    elif city_flight == 3: # User input 3 for New York city break.
        num_nights = int(input("\nEnter a number. How many nights would \
you like to stay in New York?:\nNight(s): "))
        rental_days = int(input("\nEnter a number.  How many days would \
you like to rent a car?\nCar rental day(s): "))
        
        print(f"\nFor {num_nights} night(s) stay with car hire for \
{rental_days} day(s), your New York city break will cost:") 
        print(f"£ {holiday_cost(hotel_cost(num_nights), \
            plane_cost(city_flight), car_rental(rental_days))}\n")
        break
    
    # User enters 4 to quit.
    elif city_flight == 4:
        print("Thank you for visiting CITY BREAKS")
        break
    
    # User enters anything other than 1, 2, 3, 4.
    else:
        print("Invalid entry")   
        print("Which city would you like to visit?\n")
        city_flight = int(input("Please enter a number 1 , 2, 3  or 4:\n\n\
1 for London city break\n2 for Paris city break\n\
3 for New York city break\n4 to  quit\n\n"))
    
        


