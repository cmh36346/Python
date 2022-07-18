Dictionary
    {"Key" : "Value", "Ex1" : "Value1"}

    to retrieve an item of the dictionary, you pull items via their key

programming_dictionary = {
  "Key": "Value",
  "Bug": "An error in a program that prevents the program from running as expected.",
  "Function": "A piece of code that you can easily call over and over again.",
}

#retrieving an item
print(programming_dictionary["Bug"])

#adding a new item
programming_dictionary["Loop"] = "The action of doing something over and over again"

#you can also create an empty dictionary via
empty_dictionary = {}

#wipe an existing dictionary the same way as above
programming_dictionary = {}

#edit an item in the dictionary, if it finds nothing with the same key then it will create a new one
programming_dictionary["Bug"] = "some new definition/value"

for key in programming_dictionary:
  print(key)
  print(programming_dictionary[key])


Student Scores Example
    student_scores = {
        "Harry": 81,
        "Ron": 78,
        "Hermione": 99,
        "Draco": 74,
        "Neville": 62,
    }

    student_grades = {}

    for student in student_scores:
        score = student_scores[student]
        if score > 90:
            student_grades[student] = "Outstanding"
        elif score > 80:
            student_grades[student] = "Exceeds Expectations"
        elif score > 70:
            student_grades[student] = "Acceptable"
        else:
            student_grades[student] = "Fail"

    print(student_grades)

Nesting Within Dictionaries
    new_dictionary = {
        key: [list],
        key2: {dictionary}
    }

    eg
    #nesting a list in a dictionary
    travel_log = {
        "France": ["Paris", "Dieppe", "Lille", "Nice"],
        "Germany": ["Berlin", "Hamburg"]
    }

    eg
    #nesting a dictionary in a dictionary
    travel_log = {
        "France": {"cities_visited" : ["Paris", "Dieppe", "Le Treport"], "Favorite_foods": ["Steak Frites", "Moules", "Brie", "Pain au chocolat"]},
        "England": {"cities_visited: London", "Favorite_foods": "Fish and chips"}
    }

    eg
    #nesting a dictionary in a list
    travel_log = [
        {
        "country": "France",
        "cities_visited" : ["Paris", "Dieppe", "Le Treport"],
        "Favorite_foods": ["Steak Frites", "Moules", "Brie", "Pain au chocolat"],
        },
        {
        "country": "England",
        "cities_visited: London",
        "Favorite_foods": "Fish and chips"
        }
    ]

Nested Dictionaries
    travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
    ]

    def add_new_country(country_visited, times_visited, cities_visited):
        #creating a new dictionary called new_country and adding all the various pieces that correspond to the inputs found below
        new_country = {}
        new_country["country"] = country_visited
        new_country["visits"] = times_visited
        new_country["cities"] = cities_visited
        #travel log is a list so to add a new value, namely new_country, you have to append it
        travel_log.append(new_country)

    add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
    print(travel_log)

Highest Bidder
    from replit import clear

    #import logo
    from art import logo
    print(logo)

    bids = {}

    def find_highest_bidder(bidding_record):
        #bidding_record{Camille: 123, James: 321}
        highest_bid = 0
        for bidder in bidding_record:
            bid_amount = bidding_record[bidder]
            if bid_amount > highest_bid:
                highest_bid = bid_amount
                winner = bidder
        print(f"The winner is {winner} and won with a bid of ${highest_bid}")

    bidding_finished = False
    while not bidding_finished:
        #name
        name = input("What is your name?: ")
        #bid
        price = int(input("What is your bid?: $"))
        #add to dictionary
        #set the key
        bids[name]= price
        should_continue = input("Are there any other bidders? (Y or N)")
        if should_continue == "N":
            bidding_finished = True
            find_highest_bidder(bids)
        elif should_continue == "Y":
            clear()

docstrings - create documentation for functions
    def format_name(f_name, l_name):
        """ This function takes a first and last name and formats it to return the title of the name
        """
    #then when you run the fucntion, your doc string will appear in a pop up

Example Code and Result
    def add(n1, n2):
        return n1 + n2

    def subtract(n1, n2):
        return n1 - n2

    def multiply(n1, n2):
        return n1 * n2

    def divided(n1, n2):
        return n1 / n2

    print(add(2, multiply(5, divide(8,4))))
        #first assess divide(8,4) = 2 thus it becomes add(2, multiply(5,2))
        #second assess multiply(5,2) = 10 thus it becomes add(2,10)
        #third assess add(2,10) = 12
        #output is 12

Example Code and Result
    def outer_function(a, b):
        def inner_function(c, d):
            return c + d
        return inner_function(a, b)

    result = outer_function(5, 10)
    print(result)
    #since a = 5 then c = 5 and since b = 10 then d = 10
    #result of inner function is 5 + 10 = 15
    #thus result of outer function is 15

Example Code and Result
    def my_function(a):
        if a < 40:
            return
            print("Terrible")
        if a < 80:
            return "Pass"
        else:
            return "Great"
        print(my_function(25))
