import csv

def write_csv(file_path, data):
    with open(file_path, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(data)

def read_csv(file_path):
    with open(file_path, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            print(row)

# Example data to write to CSV
data_to_write = [
    ['Name', 'Age', 'City'],
    ['John', '25', 'New York'],
    ['Alice', '30', 'San Francisco'],
    ['Bob', '22', 'Chicago']
]

# Specify the file path
csv_file_path = 'example.csv'

# Write data to CSV file
write_csv(csv_file_path, data_to_write)

# Read and display the content of the CSV file
print("Content of the CSV file:")
read_csv(csv_file_path)
