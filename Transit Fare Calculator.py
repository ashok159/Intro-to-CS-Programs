#Name: Ashok Surujdeo
#Email: Ashok.Surujdeo65@myhunter.cuny.edu
#Date: March 22, 2021
#This program runs: Transit Fare Calculator

def computeFare(zone, ticketType):
    fare = 0 
    if (zone <= 2) and (ticketType == "adult"):
        fare = 23
    elif (zone <= 2 and ticketType == "child"):
        fare = 11.5
    elif (zone == 3) and (ticketType == "adult"):
        fare = 34.5
    elif (zone == 3) and (ticketType == "child"):
        fare = 23
    elif (zone == 4) and (ticketType == "child"):
        fare = 23
    elif (zone == 4) and (ticketType == "adult"):
        fare = 46
    else:
        fare = -1
        
    return(fare)

def main():
    z = int(input("Enter the number of zones: "))
    t = input("Enter the ticket type(adult/child): ").lower()
    fare = computeFare(z, t)
    print("The fare is", fare)

if __name__ == "__main__":
    main()
