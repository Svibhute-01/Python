
text = " Hello World!123 "


print("Original String:", repr(text))


print("Length:", len(text))

print("Lowercase:", text.lower())
print("Uppercase:", text.upper(),"treating first character as space")
print("Capitalized:", text.capitalize())
print("Title Case:", text.title())


print("Strip (both):", text.strip())
print("LStrip (left):", text.lstrip())
print("RStrip (right):", text.rstrip())

print("Replace 'World' with 'Python':", text.replace("World", "Python"))


print("Find 'World':", text.find("World"))
try:
    print("Index 'World':", text.index("World"))
except ValueError:
    print("Index 'World': not found")


print("Count of 'l':", text.count("l"))


print("Starts with ' Hello':", text.startswith(" Hello"))
print("Ends with '123 ':", text.endswith("123 "))


split_text = text.strip().split(" ")
print("Split by space:", split_text)
joined_text = "-".join(split_text)
print("Join with '-':", joined_text)


print("Is Alphanumeric:", text.strip().isalnum())
print("Is Alphabetic:", text.strip().isalpha())
print("Is Digit (only digits):", "123".isdigit())
print("Is Lowercase:", "hello".islower())
print("Is Uppercase:", "HELLO".isupper())


print("Is whitespace only:", "   ".isspace())
