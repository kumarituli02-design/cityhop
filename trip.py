# Trip class using Object-Oriented Programming
class Trip:
    def __init__(self, distance, ride_type, is_peak_hour):
        self.__distance = distance
        self.__ride_type = ride_type
        self.__is_peak_hour = is_peak_hour

    # Getter methods
    def get_distance(self):
        return self.__distance

    def get_ride_type(self):
        return self.__ride_type

    def is_peak(self):
        return self.__is_peak_hour

    # Method to calculate price
    def calculate_price(self):
        if self.__ride_type == "Standard":
            price = self.__distance * 1.50
        elif self.__ride_type == "Premium":
            price = self.__distance * 2.50
        else:
            price = 0

        if self.__is_peak_hour:
            price += 5.00

        return price


# Main driver code
def main():
    trips = [
        Trip(10.0, "Standard", True),
        Trip(5.5, "Premium", False),
        Trip(3.0, "Standard", False)
    ]

    total_distance = 0
    total_fare = 0
    total_points = 0

    for trip in trips:
        distance = trip.get_distance()
        total_distance += distance
        total_fare += trip.calculate_price()

        if trip.get_ride_type() == "Premium":
            total_points += distance * 2
        else:
            total_points += distance

    print(f"Total Distance Traveled: {total_distance}")
    print(f"Total Fare Due: ${total_fare:.2f}")
    print(f"Total Loyalty Points Earned: {total_points}")

if __name__ == "__main__":
    main()