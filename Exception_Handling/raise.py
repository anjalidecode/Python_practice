def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    else:
        print("Valid age entered.")

try:
    check_age(-5)
except ValueError as ve:
    print(f"An error occurred: {ve}")
    