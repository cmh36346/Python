Day 2 Exercise 2: BMI Calculator
    height = input("enter your height in m:")
    weight = input("enter your weight in kg:")
    print(type(height))
    print(type(weight))
    int_height = float(height)
    int_weight = float(weight)
    sq_height = int_height * int_height
    bmi = int_weight / sq_height
    int_bmi = int(bmi)
    print(int_bmi)

Day 2 Exercise 3: Days Remaining
    age = input("What is your current age")
    print(type(age))
    int_age = int(age)
    print(type(int_age))
    years_left = 90 - int_age
    print(years_left)
    days = years_left * 365
    week = years_left * 52
    month = years_left * 12
    message = f"you have {days} days, {week} weeks, and {month} months left"
    print(message)

Tip Calculator
    print("Welcome to the tip calculator. \n")
    bill = input("What was the total bill? $")
    tip_percent = input("What percentage tip would you like to give? 10, 15, 20 ")
    people = input("How many people will split the bill? ")

    tip_total = str(1) + tip_percent
    tip_divide = int(tip_total) / 100

    int_bill = float(bill)
    int_people = int(people)

    total = int_bill * tip_divide
    individual = total / int_people

    pay = round(individual, 2)
    print(f"Each person should pay: $ {pay}")

If Else Statements
    print("Welcome to the rollercoaster")
    height = int(input("What is your height in cm?"))
    if height > 120:
        print("You can ride the rollerocoaster")
    #elif height == 120:
        #print("can you??")
    else:
        print("You can not ride the rollercoaster")

Equal to: ==
    Using 1 equal sign means youre assigning
    Using 2 equal signs means youre checking if equal to

Not Equal to: !=

BMI calculator
    height = float(input("enter your height in m: "))
    weight = float(input("enter your weight in kg: "))
    bmi = round(weight / height ** 2)
    if bmi >= 40:
        print(f"Your BMI is {bmi}, you are clinically obese")
    elif bmi >= 33:
        print(f"Your BMI is {bmi}, you are obese")
    elif bmi >= 26:
        print(f"Your BMI is {bmi}, you are slightly overweight")
    elif bmi >= 22:
        print(f"Your BMI is {bmi}, you have a normal weight")
    else:
        print(f"Your BMI is {bmi}, you are underweight")

Leap Year
    Is it cleanly divisible by 4?
        - No, then not leap
        - Yes, then
            Is it cleanly divisible by 100
                - No, then leap
                - Yes, then
                    Is it cleanly divisble by 400
                        - Yes, then Leap
                        - No, then not leap
    year = int(input("Which year do you want ot check?"))
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Leap year")
            else:
                print("Not leap years")
        else:
            print("Leap year")
    else:
        print("Not leap year")

Pizza bill
    print("welcome to python pizza deliveries!")
    size = input("What size pizza do you want? S, M, or L")
    add_pepperoini = input()
    ...

Treasure Hunt
    print("Welcome to Treasure Island. Your mission is to find the treasure.")
    crossroad = input("You are at a crossroad, would you like to go left or right? (L or R)")
    if crossroad == "R":
        print("You've fallen into a hole. GAME OVER")
    else:
        print("Your path led to a river")
        river = input("would you like to swim or wait for the next ferry? (S or F)")
        if river == "S":
            print("You were attacked by trout and died. GAME OVER")
        else:
            print("A ferry arrived 45 minutes later")
            print("At the dock across the river, there is a house with three rooms")
            house = input("Which room would you like to enter, red, blue, or yellow? (R, B, Y)")
            if house == "R":
                print("A fire ensues and you die. GAME OVER")
            elif house == "B":
                print("You opened the door to beasts. GAME OVER")
            elif house == "Y":
                print("Congratulatios, you found the treasure. YOU WIN")
            else:
                print("Incorrect. GAME OVER")
