#Kenny Hedlund

from datetime import time, timedelta, date, datetime
import locale

#Get date input from user
def date_inp():
    while True:
        date = input("Estimated date of departure (YYYY-MM-DD): ")
        try: #Try-Except validation loop
            departX = datetime.strptime(date, "%Y-%m-%d")
            return departX #Returning Date value
        except ValueError:
            print()
            print("*=========================================================")
            print("*Invalid date format. Please use (YYYY-MM-DD) format. ")
            print("*")
            print("*For Example: ")#Example of format for clarification
            print("*If the date was July 10, 2019 you should type (2019-07-10)")
            print("*=========================================================")
            print()
            continue

#Get time input from user
def time_inp():
    while True:
        time = input("Estimated time of departure (HH:MM AM/PM): ")
        try: #Try-Except validation loop
            departY = datetime.strptime(time, "%I:%M %p")
            return departY #Returning Time value
        except ValueError:
            print()
            print("*=====================================================")
            print("*Invalid time format. Please use (HH:MM AM/PM) format. ")
            print("*")
            print("*For Example: ")#Example of format for clarification
            print("*If the time was 3:54PM you should type (03:54 PM)")
            print("*=====================================================")
            print()
            continue

#Get mile value from user
def mile_inp():
    while True:
        mile = input("Enter miles: ")
        try: #Try-Except validation loop
            mile = int(mile)
            if mile <= 0: #If-Else validation to force natural numbers from input
                print()
                print("*===========================================================")
                print("*Please enter a valid number of miles(Must be greater than 0")
                print("*===========================================================")
                print()
            else:
                return mile #Returning Mile/Distance value
        except ValueError: #End of Try-Except validation
            print()
            print("*===============================================================================")
            print("*Invalid mile format. Please enter the distance of the trip in number of miles. ")
            print("*===============================================================================")
            print()
            continue

#Get MPH value from user
def MPH_inp():
    while True:
        mph = input("Enter miles per hour: ")
        try: #Try-Except validation loop
            speed = int(mph)
            if speed <= 0: #If-Elif-Else validation to force natural numbers from user mph input
                print()
                print("*==========================================================")
                print("*Please enter a valid speed. Greater than 0 Miles Per Hour.")
                print("*==========================================================")
            elif speed >= 120:
                print()
                print("*===========================================")
                print("*Please enter a valid speed.(0~120MPH range)")
                print("*===========================================")
                print()
            else:
                return speed #Returning Speed/MPH value
        except ValueError: #End of Try-Except validation
            print()
            print("*==============================================================================")
            print("*Invalid speed format. Please use numbers to enter the speed in miles per hour.")
            print("*==============================================================================")
            print()
            continue

#Function for calculating the values
def calculate(departX, departY, mile, speed):
    #Calculating the time, speed, and distance.
    hrs = int(mile/speed)
    mins = int(((mile/speed)-hrs)*60)
    complete_time = timedelta(hours=hrs, minutes=mins)
    
    #Calculating and setting data for the amount of days the trip will take
    midnight = datetime.strptime("12:00 AM", "%I:%M %p") #Variable for the program to count new days
    time_to_midnight = (midnight - departY) + timedelta(days=1) #Variable to calculate midnight in relation to the travel time to calculate days
    passed_time = complete_time #Variable used to store day amounts
    #If statement adds a counter for every time passed_time variable is greater than or equal to the midnight variable in calculation
    if passed_time >= time_to_midnight: 
        passed_time += timedelta(days = 1)

    #Printing results to user  
    print("\n\nEstimated Travel Time")
    print("Hours: ", hrs)
    print("Minutes: ", mins)
    arrival_date = departX + passed_time #Date with passed_time day counter
    print("Estimated Date of Arrival: ", arrival_date.strftime("%Y-%m-%d"))
    arrival_time = departY + complete_time #Time with passed_time day counter
    print("Estimated Time of Arrival: ", arrival_time.strftime("%I:%M %p"))
    print()

#Beginning of Hierarchy
def main():
    print("Arrival Time Estimator")
    print()
    choice = "y"
    #While statement for Boolean
    while choice.lower() == "y":
        #Call the functions and loop the program
        departX = date_inp()
        departY = time_inp()
        mile = mile_inp()
        speed = MPH_inp()
        calculate(departX, departY, mile, speed)
        choice = input("Continue? (Y/N)")
    #Printed if user inputs anything other than Y on choice
    print()
    print("Bye!")

if __name__ == "__main__":
    main()
    
