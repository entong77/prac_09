from taxi import Taxi


def main():
    taxi = Taxi("Prius 1", 100)
    taxi.drive(40)
    print(taxi)  # calling taxi.__str__
    print(f"Current fare: ${taxi.get_fare():.2f}")
    print()
    taxi.start_fare()
    print(f"Current fare: ${taxi.get_fare():.2f} before moving any new distance")
    distance_driven = taxi.drive(100)
    print(f"After attempting to drive another 100km.., Actual distance: {distance_driven} km")
    print(taxi)
    print(f"Current fare: ${taxi.get_fare():.2f}")


if __name__ == '__main__':
    main()