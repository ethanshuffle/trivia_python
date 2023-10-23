#This file gathers category and difficulty parameters for the api call

def print_category():
    print("")
    print("CATEGORIES")
    print("1. Music")
    print("2. Sports and Leisure")
    print("3. Film and TV")
    print("4. Arts and literature")
    print("5. History")
    print("6. Society and Culture")
    print("7. Science")
    print("8. Geography")
    print("9. Food and Drink")
    print("10. General Knowledge")
    print("11. All Categories")
    print()

def print_difficulty():
    print("")
    print("DIFFICULTY")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    print()

def choose_category():
    print_category()

    choice = input("Select a choice 1 through 11: ")

    match choice:
        case '1':
            category = "music"
        case '2':
            category = "sport_and_leisure"
        case '3':
            category = "film_and_tv"        
        case '4':
            category = "arts_and_literature" 
        case '5':
            category = "history"
        case '6':
            category = "society_and_culture"
        case '7':
            category = "science"
        case '8':
            category = "geography"
        case '9':
            category = "food_and_drink"
        case '10':
            category = "general_knowledge"
        case "11":
            category = ""
        case _:
            print("")
            print("INVALID CHOICE; TRY AGAIN")
            choose_category()
        
    return category
        
def choose_difficulty():
    print_difficulty()

    choice = input("Select a choice 1 through 3: ")

    match choice: 
        case '1':
            difficulty = "easy"
        case '2':
            difficulty = "medium"
        case '3':
            difficulty = "hard"
        case _:
            print("")
            print("INVALID CHOICE; TRY AGAIN")
            choose_difficulty()

    return difficulty

def menu_sequence():
    category = choose_category()
    difficulty = choose_difficulty()
    return category, difficulty