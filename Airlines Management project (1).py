flag = 'y';

print("Welcome to Chitkara Airlines","\U0001F6EA")

available_flights = [
    {
        "id": '1',
        "flight_number": "AI-101",
        "from": "New Delhi",
        "to": "Mumbai",
        "date_of_departure": "2023-01-01",
        "time_of_departure": "10:00",
        "date_of_arrival": "2023-01-01",
        "time_of_arrival": "12:30",
        "price": 7000,
        "seats_available": 100
    },
    {
        "id": '2',
        "flight_number": "AI-102",
        "from": "Delhi",
        "to": "Chennai",
        "date_of_departure": "2023-01-05",
        "time_of_departure": "10:00",
        "date_of_arrival": "2023-01-05",
        "time_of_arrival": "12:40",
        "price": 9600,
        "seats_available": 62
    },
    {
        "id": '3',
        "flight_number": "AI-103",
        "from": "Mumbai",
        "to": "Kolkata",
        "date_of_departure": "2023-01-09",
        "time_of_departure": "19:00",
        "date_of_arrival": "2023-01-09",
        "time_of_arrival": "21:40",
        "price": 6000,
        "seats_available": 78
    },
    {
        "id": '4',
        "flight_number": "AI-104",
        "from": "New Delhi",
        "to": "Dubai",
        "date_of_departure": "2023-01-13",
        "time_of_departure": "06:00",
        "date_of_arrival": "2023-01-13",
        "time_of_arrival": "10:10",
        "price": 14000,
        "seats_available": 78
    },
    {
        "id": '5',
        "flight_number": "AI-105",
        "from": "Mumbai",
        "to": "Tokyo",
        "date_of_departure": "2023-01-13",
        "time_of_departure": "18:45",
        "date_of_arrival": "2023-01-14",
        "time_of_arrival": "06:00",
        "price": 65250,
        "seats_available": 98
    },
     {
        "id": '6',
        "flight_number": "AI-106",
        "from": "Mumbai",
        "to": "London",
        "date_of_departure": "2023-01-13",
        "time_of_departure": "18:45",
        "date_of_arrival": "2023-01-14",
        "time_of_arrival": "06:00",
        "price": 65250,
        "seats_available": 98
    },
]


booking_id = 100001
usersBooked = []

def book_ticket():
    print("\nBook a flight ticket")
    print("\nEnter the following details:\n")
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    flightNumber = input("Enter the flight number: ")
    flightFound = False
    print("\nChecking for avaialability of seats...")
    for flight in available_flights:
        if flight["flight_number"] == flightNumber:
            flightFound = True
            if flight["seats_available"] > 0:
                print("Seats are available")
                print("Flight details are: ")
                print_flight_details(flightNumber)
                if input("\nDo you want to book the ticket? (y/n): ") == 'y':
                    flight["seats_available"] -= 1
                    global booking_id
                    user = {
                        "name": name,
                        "age": age,
                        "flight_number": flightNumber,
                        "booking_id": booking_id
                    }
                    usersBooked.append(user)
                    print("\nYour booking is confirmed")
                    print("Your booking id is: ", booking_id)
                    booking_id += 1
                else:
                    break
            else:
                print("\nSorry, seats are not available for this flight")
            break
    if flightFound == False:
        print("Sorry, no flight found with this flight number")


def print_flight_details(flightNumber, flag = False):
    for flight in available_flights:
        if flight["flight_number"] == flightNumber:
            if flag == True:
                print("Id: ", flight["id"])
            print("\tFlight Number: ", flight["flight_number"])
            print("\tFrom: ", flight["from"])
            print("\tTo: ", flight["to"])
            print("\tDate of Departure: ", flight["date_of_departure"])
            print("\tTime of Departure: ", flight["time_of_departure"])
            print("\tDate of Arrival: ", flight["date_of_arrival"])
            print("\tTime of Arrival: ", flight["time_of_arrival"])
            print("\tPrice: ", flight["price"])
            print("\tSeats Available: ", flight["seats_available"])
            break
def view_flights():
    print("\nAvailable flights are: ")
    for flight in available_flights:
        print_flight_details(flight["flight_number"], True)


while flag == 'y':
    print("\nPress 1 to View available flights")
    print("Press 2 to Book a flight ticket")
    choice = int(input("\nEnter your choice: "))
    if choice == 1:
        view_flights()
    elif choice == 2:
        book_ticket()
    else:
        print("Invalid choice, please try again")

