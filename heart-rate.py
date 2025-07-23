import csv
# module for working with CSV files

def calculate_heart_rate_range(age):
    # Calculate normal heart rate range based on age
    max_heart_rate = 220 - age
    min_target = int(max_heart_rate * 0.5)
    max_target = int(max_heart_rate * 0.85)
    return min_target, max_target

def save_to_csv(name, age, heart_rate, status):
    # Save user data in CSV file called heart_data.csv
    with open("heart_data.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        # write headers if the file is empty
        if file.tell() == 0:
            writer.writerow(["Name", "Age", "Heart Rate", "Status"])
        # write the user's data as a new row
        writer.writerow([name, age, heart_rate, status])

def main():
    print(" Normal Heart Rate Checker ")

    # ask user for input
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    heart_rate = int(input("Enter your current heart rate: "))

    # calculate normal heart rate range
    min_hr, max_hr = calculate_heart_rate_range(age)
    print(f"\nYour normal heart rate should be between {min_hr} and {max_hr} bpm.")

    # check if current heart rate is within the normal range
    if min_hr <= heart_rate <= max_hr:
        status = "Normal"
        print(" Your heart rate is in the normal range.")
    else:
        status = "Not Normal"
        print(" Your heart rate is outside the normal range")

    # save the data to CSV
    save_to_csv(name, age, heart_rate, status)
    print("\n Your data has been saved to heart_data.csv.")

# run the main function
if __name__ == "__main__":
    main()
