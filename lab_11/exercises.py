#Exercise 1
numbers = [10, 20, 30, 40, 50]
numbers.append(60)
numbers.insert(1, 15)
numbers.remove(30)
numbers.reverse()
numbers.sort()

print(numbers)

#Exercise 2
numbers = [10, 20, 30, 40, 50]
print(numbers[:3]) 
print(numbers[-2:])
print(numbers[::-1])

#Exercise 3
student = {"name": "Alice", "age": 22, "grade": "A"}
student["subject"] = "Math"
student["grade"] = "A+"
del student["age"]
print(student.keys())
print(student.values())

#Exercise 4
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.union(set2)) 
print(set1.intersection(set2))
print(set1.difference(set2))

#Exercise 5
colors = ("red", "blue", "green", "red", "yellow")
print(colors.index("green"))
print(colors.count("red"))
