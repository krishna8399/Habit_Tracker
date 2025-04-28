# Import the CSV module - built-in Python library for CSV file handling
import csv

# Initialize an empty list to store habit names
habits = []

# Start a loop to gather habits from the user
while True:
    # Ask the user to input a habit name or 'q' to quit
    habit_name = input("Enter a habit (or 'q' to quit): ").strip()

    # If user enters 'q' (lowercase or uppercase), exit the loop
    if habit_name.lower() == 'q':
        break
    
    # Otherwise, add the entered habit to the habits list
    habits.append(habit_name)

# Save the habits list to a CSV file
# Open a new CSV file called 'habits.csv' in write mode ("w")
with open('habits.csv', mode='w', newline='') as file:
    # Create a CSV writer object that will write into the file
    writer = csv.writer(file)

    # Write a header row (optional) - this labels the columns
    writer.writerow(['Habit Name'])

    # Write each habit as a new row under the header
    for habit in habits:
        writer.writerow([habit])

# Confirm to the user that data was saved
print("Habits saved to habits.csv successfully.")
