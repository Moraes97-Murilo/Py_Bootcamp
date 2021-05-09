#BMI calculator

height = float(input("Hi, how tall are you? "))
weight = float(input("What's your weight? "))

bmi = round(weight/height**2, 2)

if bmi < 18:
    print(f"You are underweighted, your bmi is {bmi}.")
elif 18 < bmi < 26:
    print(f"You are regular, your bmi is {bmi}.")
else:
    print(f"You are overweighted, your bmi is {bmi}.")
