#Scoreboard reading and writing. 

def write_score(score):
    name = input("Enter a 3 character name(ex. ECS): ")
    #Verifies name is 3 characters
    if (len(name) > 3 or len(name) < 3):
        print("Name not 3 characters, try again.")
        write_score(score)
    else:
        #Adds : between name and score
        insert = name.upper() + ":" + str(score) + "\n"
        file = open("scoreboard.txt", "r")
        scoreboard = file.readlines()
        file.close()
        #Checks where in the highscores the score goes
        for i in range(len(scoreboard)):
            split = scoreboard[i].split(":")
            if (score < float(split[1])):
                continue
            else:
                scoreboard.insert(i, insert)
                file = open("scoreboard.txt", "r+")
                file.seek(0)
                file.writelines(scoreboard)
                file.truncate()
                file.close()
                break
            
def print_scoreboard():
    file = open("scoreboard.txt", "r")
    scoreboard = file.readlines()
    file.close()

    print("HIGHSCORES")    
    print("")

    for i in range(10):
        print(scoreboard[i])