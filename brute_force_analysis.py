import csv

def process_intruder_results(file_path):
    """
    Processes Intruder results from a CSV file.

    Args:
        file_path: Path to the CSV file.

    Returns:
        A tuple containing total attempts, successful attempts, and success rate.
    """

    total_attempts = 0
    successful_attempts = 0

    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            total_attempts += 1
            if int(row['Response Code']) == 200:
                successful_attempts += 1

    success_rate = (successful_attempts / total_attempts) * 100
    return total_attempts, successful_attempts, success_rate

# Assuming the CSV file is in the same directory as the script
file_path = "intruder_results.csv"

total_attempts, successful_attempts, success_rate = process_intruder_results(file_path)

print(f"Total Attempts: {total_attempts}")
print(f"Successful Attempts: {successful_attempts}")
print(f"Success Rate: {success_rate:.2f}%")