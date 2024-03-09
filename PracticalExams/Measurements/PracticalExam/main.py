from Repo.repo import MeasurentsRepository

repo = MeasurentsRepository()

repo.AddMeasurement(3.3, 55, 10)
repo.AddMeasurement(4, 40, 11)
repo.AddMeasurement(2.5, 90, 9)
repo.AddMeasurement(7.7, 20, 10)
repo.AddMeasurement(8.9, 60, 11)

while(True):
    try:
        print("1. Add measurement")
        print("2. Display measurements higher than a value")
        print("3. View measurements")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            pressure = float(input("Enter pressure: "))
            hours_of_day = int(input("Enter hours_of_day: "))
            temperature = int(input("Enter temperature: "))
            repo.AddMeasurement(pressure, hours_of_day, temperature)
        elif choice == "2":
            value = int(input("Enter value: "))
            print(repo.DisplayMeasurementsHigher(value))
        elif choice == "3":
            print(repo.PrintAll())
        elif choice == "4":
            break
        else:
            print("Invalid choice")
    except ValueError as ve:
        print(ve)
