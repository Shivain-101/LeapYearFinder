# Python program to check if a year is a leap year or not 
def is_leap_year(year):
    # A leap year is exactly divisible by 4 except for century years (years ending with 00).
    # The century year is a leap year only if it is perfectly divisible by 400.
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        return True
    else:
        return False

# Example usage
year_to_check = int(input("Enter Year ="))
if is_leap_year(year_to_check):
    print(f"{year_to_check} is a leap year.")
else:
    print(f"{year_to_check} is not a leap year.")
