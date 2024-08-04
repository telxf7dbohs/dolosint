import csv

def read_account_data(csv_filename):
    try:
        with open(csv_filename, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            data = [row for row in reader]
            return data
    except FileNotFoundError:
        print(f"File '{csv_filename}' not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
