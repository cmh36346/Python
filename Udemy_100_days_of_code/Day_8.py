Positional Arguments
    def my_function(a, b, c):
        print(a)
        print(b)
        print(c)
    my_function(1, 2, 3)

    ex.
    def greet(name, location):
        print(f"Welcome {name}")
        input("How are you doing today")
        print(f"What is the weather like in {location} today?")
    greet("Camille", "New Jersey")
    #can also be rewritten as
    greet(name ="Camille", location="New Jersey")

Calculate Area of a Wall for Paint
    import math
    def paint_calc(height, width, cover):
        area = height * width
        #print(area)
        divide = area / cover
        #print(divide)
        round = math.ceil(divide)
        print(f"You will need {round} can(s) of paint")

    test_h = int(input("Height of wall: "))
    test_w = int(input("Width of wall: "))
    coverage = 5
    paint_calc(height=test_h, width=test_w, cover=coverage)

Prime Number Check

    def prime_checker(number):
      is_prime = True
      for i in range(2, number):
        if number % i == 0:
          is_prime = False
      if is_prime:
        print("It is a prime number")
      else:
        print("It is not a prime number")

    n = int(input("Check this number: "))
    prime_checker(number=n)

Caesar Cipher
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def encrypt(plain_text, shift_amount):
        cipher_text = ""
        for letter in plain_text:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            cipher_text += alphabet[new_position]
        print(f"The encoded text is {cipher_text}")

    def decrypt(plain_text, shift_amount):
        cipher_text = ""
        for letter in plain_text:
            position = alphabet.index(letter)
            new_position = position - shift_amount
            cipher_text += alphabet[new_position]
        print(f"The decoded text is {cipher_text}")

    if direction == "encode":
        encrypt(plain_text=text, shift_amount=shift)
    elif direction == "decode":
        decrypt(plain_text=text, shift_amount=shift)

Combining and Making the Caesar Cipher Dynamic
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def caesar(start_text, shift_amount, cipher_direction):
        end_text = ""
        if cipher_direction == "decode":
            shift_amount *= -1
        for letter in start_text:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        print(f"The {cipher_direction}d text is {end_text}")

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

Final Update to the Caesar Cipher
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    def caesar(start_text, shift_amount, cipher_direction):
        end_text = ""
        if cipher_direction == "decode":
            shift_amount *= -1
        for char in start_text:
            if char in alphabet:
                position = alphabet.index(char)
                new_position = position + shift_amount
                end_text += alphabet[new_position]
            #this will append the end text with any original sympbols and numbers
            else:
                end_text += char

        print(f"Here's the {cipher_direction}d result: {end_text}")

    #this brings in the logo from a separate file
    from art import logo
    print(logo)

    #this will make the program repeatable
    again = True
    while again:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        if shift > 50:
            while shift > 50:
                shift = shift - 50

      caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

      #this prompts the user to go again
        result = input("Would you like to encode or decode another word? (Yes or No)")
        if result == "No" or result == "no":
            again = False
            print("Goodbye")
