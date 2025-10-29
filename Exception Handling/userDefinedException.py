class InvalidAgeException(Exception):
    pass

age=int(input("Enter age:"))

try:
    if age<18:
        raise InvalidAgeException
    else:
        print("You can vote")
except InvalidAgeException:
    print("IvalidAgeException:You ar not eligible to vote")
