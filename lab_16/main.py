import json

student_data = {
    "name": "Alice",
    "age": 21,
    "courses": ["Math", "Science", "History"]
}

json_string = json.dumps(student_data, indent=4)
print("Serialized JSON string:")
print(json_string)

filename = "student.json"
with open(filename, "w") as file:
    json.dump(student_data, file, indent=4)
print(f"\nData has been written to {filename}")

with open(filename, "r") as file:
    loaded_data = json.load(file)

print("\nData loaded from the JSON file:")
print(loaded_data)
