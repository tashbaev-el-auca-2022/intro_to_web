import csv

filename = "text.txt"
content = ("ONE\n"
           "TWO\n"
           "THREE")

# Запись в файл
with open(filename, "w") as f:
    f.write(content)

# Чтение
with open(filename, "r") as f:
    read_content = f.read()

print("File content:")
print(read_content)

csv_filename = "text.csv"
data = [
    ["Name", "Age", "Country"],
    ["Rick", 90, "USA"],
    ["Morty", 15, "UK"],
    ["Jerry", 35, "Canada"]
]

# Запись данных в CSV
with open(csv_filename, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)
    print("CSV file written successfully.")

# Чтение из CSV
with open(csv_filename, "r", newline="") as f:
    reader = csv.reader(f)
    print("CSV content:")
    for row in reader:
        print(row)

add_text = "\nFOUR"
with open(filename, "a") as f:
    f.write(add_text)
print("Text appended to file.")

with open(filename, "r") as f:
    updated_content = f.read()

print("Updated file content:")
print(updated_content)
