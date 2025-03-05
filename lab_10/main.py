import math
from math import sqrt
import random
from datetime import datetime, timedelta

print(math.sqrt(16))
print(sqrt(16))
print(math.pi)

names = ["Elmur", "Mirai", "Charlie", "Vox"]
random_name = random.choice(names)
print(f"The random name is: {random_name}")

now = datetime.now()
print(f"Current date and time: {now}")
future = now + timedelta(days=5)
print(f"Date and time after 5 days: {future}")
