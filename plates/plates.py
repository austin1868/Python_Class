def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
    if len(s) < 2 or len(s) > 6:
        return False

    # “All vanity plates must start with at least two letters.”
    if not s[0].isalpha() or not s[1].isalpha():
        return False

    # “No periods, spaces, or punctuation marks are allowed.
    if any(char in s for char in ['.', ',', '!', '?', ' ', ';', ':']):
        return False

    # If there are numbers in the plate, they must be at the end
    numbers_started = False
    for char in s[2:]:
        if char.isdigit():
            numbers_started = True
        elif numbers_started and char.isalpha():
            return False

    # Checking if the first number is '0'
    if any(char.isdigit() for char in s):
        first_number_position = next((i for i, char in enumerate(s) if char.isdigit()), None)
        if s[first_number_position] == '0':
            return False

    return True

main()
