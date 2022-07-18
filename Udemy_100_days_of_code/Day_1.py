Print Function
    print([whatever you want to be displayed])
    LOWERCASE
    the pieces of text wrapped in "[word]" are strings

    print('string concatenation is done with the "+" sign.')
    # use different quotes to distinguish

Indentation matters!!!!

Input function
    input("What is your name")

    print("hello " + input("What is your name?"))
    #output
        #What is your name?
        #Camille
        #hello Camile

Nested
    print(len(input("What is your name?")))
    #output
        #What is your name?
        #Camille
        #7

    VS
    name = input("what is your name?")
    print(len(name))
    #output
        #what is your name
        #camille
        #7

    VS
    name = input("What is your name")
    length = len(name)
    print(length)

Data Types
    Strings - string of characters, can pull out each individual character via its position/index, which starts at zero
        Convert to a string by creating a new variable = str(other_variable)
        print("Hello"[0])
        #output
            #h

        print("Hello"[4])
        #output
            #o
    Integer
        Any whole, positive or negative number
        Float - includes a decimal point

    Boolean - True or False
