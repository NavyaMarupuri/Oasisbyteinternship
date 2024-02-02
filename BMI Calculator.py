# BMI Calculator

def get_user_input():
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
        return weight, height
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return get_user_input()

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def display_result(bmi, category):
    print(f"Your BMI is: {bmi:.2f}")
    print(f"Category: {category}")

def bmi_calculator():
    print("Welcome to the BMI Calculator!")
    
    weight, height = get_user_input()
    
    bmi = calculate_bmi(weight, height)
    category = categorize_bmi(bmi)

    display_result(bmi, category)

# Run the BMI Calculator
bmi_calculator()
