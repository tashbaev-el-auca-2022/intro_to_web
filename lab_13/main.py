#LAB EXERCISES
import re

#Lab1
text = "Call 555-1234, 555-5678, or 555-9999 for assistance."
phone_numbers = re.findall(r'\d{3}-\d{4}', text)
print("Phone Numbers Found:", phone_numbers)


#Lab2
text1 = "Hello world!"
text2 = "Say Hello to the world."

match1 = re.match(r"Hello", text1)
match2 = re.match(r"Hello", text2)

if match1:
    print("Using re.match() on text1: Match found:", match1.group())
else:
    print("Using re.match() on text1: No match found.")

if match2:
    print("Using re.match() on text2: Match found:", match2.group())
else:
    print("Using re.match() on text2: No match found.")

search1 = re.search(r"Hello", text1)
search2 = re.search(r"Hello", text2)

if search1:
    print("Using re.search() on text1: Found:", search1.group())
else:
    print("Using re.search() on text1: No match found.")

if search2:
    print("Using re.search() on text2: Found:", search2.group())
else:
    print("Using re.search() on text2: No match found.")


#Lab3
text = "There are 10 apples, 20 oranges, and 30 bananas in the basket."
modified_text = re.sub(r'\d+', 'NUMBER', text)
print("Modified Text:", modified_text)


#Lab4
text = "Contact us at support@example.com or sales@example.org."
emails = re.findall(r'\b\w+@\w+\.\w+\b', text)
print("Email Addresses Found:", emails)


#Lab5
text = "An apple a day keeps away even elephants enjoying eating."
words = re.findall(r'\b[aeiouAEIOU]\w*\b', text)
print("Words starting with a vowel:", words)
