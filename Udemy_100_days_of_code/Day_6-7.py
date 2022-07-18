Day 6
Creating a function
    def my_function():
        print("Hello")
        print("Goodbye")

    #call the function
    my_function()

Hurdles
    #define a turn right function
    def turn_right():
        turn_left()
        turn_left()
        turn_left()

    #define a jump function
    def jump():
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()
        turn_left()

    #create for loop that jumps over six hurdles
    for step in range(6):
        move()
        jump()


While Loop
    # replacing the for loop above
    number_of_hurdles = 6
    while number_of_hurdles > 0:
        move()
        jump()
        number_of_hurdles -= 1

    To stop at a random unknown goal, at_goal == True
    #attempt 1 (ME)
    number_of_hurdles = 6
    while number_of_hurdles > 0:
        move()
        jump()
        number_of_hurdles -= 1
        print(number_of_hurdles)
        if at_goal() == True:
            number_of_hurdles = 0

    #attempt 2 (ANGELA)
    while at_goal() != True:
        move()
        jump()

________________________________________________________________________________________________________________________________________________________________________________________________________
Hurdle 3, random hurdles and random end point
    while at_goal() != True:
        if front_is_clear() == True:
            move()
        elif wall_in_front() == True:
            jump()

________________________________________________________________________________________________________________________________________________________________________________________________________
Hurdle 4, random and varying height of hurdles
    #must modify the jump statement
    def jump():
        turn_left()
        while wall_on_right():
            move()
        turn_right()
        move()
        turn_right()

        while front_is_clear():
            move()

        turn_left()

    while not at_goal():
        if front_is_clear() == True:
            move()
        elif wall_in_front() == True:
            jump()

Maze
    def turn_right():
        turn_left()
        turn_left()
        turn_left()

    #keep repeating until at goal
    while not at_goal():
        #essentially follow the right edge
        if right_is_clear():
            turn_right()
            move()
        elif front_is_clear():
            move()
        else:
            turn_left()

Hangman Game
    import random

    #icons that demonstrate when a piece has been added after incorrect guess
    stages = []

    #measures to end game
    end of game = False

    word_list = ["Ardvark", "Baboon", "Camel", "Dog", "Elephant"]
    chosen_word = random.choice(word_list) #randomly selects a word
    word_length = len(chosen_word) #determines length of selected word

    #creates blanks
    display = []
    for _ in range(word_length):
        display += "_"
    print(display)

    lives = 6 #sets amount of lives per game

    while not end_of_game:
        guess = input("Guess a letter: ").lower()

        #check guessed letter
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

        if guess not in chosen_word:
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("You lose")

        print(f"{' '.join(display)}")

        if "_" not in display:
            end_of_game = True
            print("You win")

        if lives == 6:
            print(stages[6])
        elif lives == 5:
            print(stages[5])
        elif lives == 4:
            print(stages[4])
        elif lives == 3:
            print(stages[3])
        elif lives == 2:
            print(stages[2])
        elif lives == 1:
            print(stages[1])
        elif lives == 0:
            print(stages[0])
