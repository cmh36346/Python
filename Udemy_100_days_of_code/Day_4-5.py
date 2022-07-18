Day 4: Randomness
    import random
    random_integer = random.randint(1,10)
    print(random_integer)

    #for a range of 0.0000-0.999999
    random_float = random.random()
    print(random_float)

    #for a range of 0.0000-4.999999
    print(random_float * 5)

Lists
    - order of storage matters
    - first position is zero
    - can count from the end of the list by using (-), end of list would be -1 ...
    - can alter items
    #create list
    states_of_america = ["Delaware", "New Jersey", "New York", ...]
    # alter items
    states_of_america[1] = "Best Jersey"
    #add items
    states_of_america.append = "Puerto Rico"

Split will split a string based on some pre-determined divider, commonly a ", "
    names_string = input("Give me everybody's names, separated by a comma")
    names =names_string.split(", ")

Exercise 2 - two ways of determining who the payer is going to be in card roulette

Nested List
    fruits = ["apple", "pear", "orange"]
    vegetables = ["celery", "kale", "potatoes"]
    dirty_dozen = [fruits, vegetables]

Rock Paper Scissors
    print("Welcome to the game, rock, paper, scissors & shoot.")
    player = input("Begin by selecting your first move, R, P, or S: ")

    import random
    computer = random.randint(0,2)
    # 0 = rock
    # 1 = paper
    # 2 = scissor
    if computer == 0:
        print("computer played rock")
    elif computer == 1:
        print("computer played paper")
    elif computer == 2:
        print("computer played scissors")

        #player & rock
        if player == "R" and computer == 0:
            print("Player" + rock)
            print("Computer" + rock)
            print("Tie game")
        elif player == "R" and computer == 1:
            print("player" + rock)
            print("Computer" + paper)
            print("Computer wins")
        elif player == "R" and computer == 2:
            print("player" + rock)
            print("computer" + scissors)
            print("Player wins")
            #player & paper
        elif player == "P" and computer == 0:
            print("Player" + paper)
            print("Computer" + rock)
            print("Player wins")
        elif player == "P" and computer == 1:
            print("player" + paper)
            print("Computer" + paper)
            print("tie game")
        elif player == "P" and computer == 2:
            print("player" + paper)
            print("computer" + scissors)
            print("Computer wins")
            #player & scissor
        elif player == "S" and computer == 0:
            print("Player" + scissors)
            print("Computer" + rock)
            print("computer wins")
        elif player == "S" and computer == 1:
            print("player" + scissors)
            print("Computer" + paper)
            print("player wins")
        elif player == "S" and computer == 2:
            print("player" + scissors)
            print("computer" + scissors)
            print("Tie game")

For Loops
    for loops will go through every item in the list

    student_scores = input("Input a list of student scores ").split()
    for n in range(0, len(student_scores)):
        student_scores[n] = int(student_scores[n])
    print(student_scores)
    #you could use the max function but thats too easy
    #print(max(student_scores))
    #using a for loop instead!
    highest_score = 0
    for score in student_scores:
        if score > highest_score:
            highest_score = score
    print(f"The highest score in the class is: {highest_score}}")

For Loops & Range
    this will loop through a certain range
    parenthesis is not inclusive

    for number in range(1,10):
        print(number)
    #output
    #1, 2, 3, 4 ,5 ,6, 7, 8, 9

    #third digit serves as a step
    for number in range(1, 11, 3):
        print(number)
    #output
    #1, 4, 7, 10

    total = 0
    for number in range(1, 101):
        total += number
    print(total)
    #output
    #5050

Exercise Adding Even Numbers
    total = 0
    for number in range(2, 101, 2):
        total += number
    print(total)

Exercise Fizzbuzz
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 != 0:
            print("Fizz")
        elif number % 5 == 0 and number % 3 != 0:
            print("Buzz")
        elif number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        else:
            print(number)

    OR ALTERNATIVELY
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)

Exercise Password Generator
    import random
    letters = ['a', 'b', 'c', ... 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', ... '7', '8', '9']
    symbols = ['!', '@', '$', ... '&', '*', '+']

    print("Welcome to the password Generator")
    nr_letters = int(input(How many letters would you like in your password))
    nr_numbers = int(input(How many numbers would you like in your password))
    nr_symbols = int(input(How many symbols would you like in your password))

    password_list = []
    for number in range(1, nr_letters + 1):
        password_list += random.choice(letters)

    for number in range(1, nr_numbers + 1):
        password_list += random.choice(numbers)

    for number in range(1, nr_symbols + 1):
        password_list += random.choice(symbols)

    print(password_list)

    #to shuffle the order
    random.shuffle(password_list)
    print(password_list)

    #to turn into a string instead of a list
    password = ""
    for char in password_list:
        password += char

    print(f"Your password is {password}")
