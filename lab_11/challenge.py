company = {
    "employees": [
        {"name": "Elmurat", "position": "Manager", "salary": 5000},
        {"name": "Sherlock", "position": "Developer", "salary": 4000}
    ]
}
company["employees"].append({"name": "Notch", "position": "Designer", "salary": 3500})
for employee in company["employees"]:
    print(employee["name"])
