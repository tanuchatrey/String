string = input("Enter a string: ")

result = ""

for char in string:
    if char.islower():
        result += char.upper()
    elif char.isupper():
        result += char.lower()
    else:
        result += char

print("Converted string:", result)
