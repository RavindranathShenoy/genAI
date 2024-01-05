def calculate_year_of_100(age):
    import datetime
    current_year = datetime.datetime.now().year
    return current_year + (100 - age)

def main():
    print("Welcome to the Age Calculator!")
    
    # Taking user input for name and age
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    
    # Calculating the year when the user turns 100
    year_of_100 = calculate_year_of_100(age)
    
    # Displaying a personalized greeting
    print(f"Hello, {name}! You will turn 100 years old in the year {year_of_100}.")

if __name__ == "__main__":
    main()
