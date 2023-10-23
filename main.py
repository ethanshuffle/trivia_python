#PyTrivia is a console based trivia game using the trivia api found here
#https://the-trivia-api.com/
#
#Users can pick their category and difficulty, as well as save their
#scores to a scoreboard.

from api_call import get_request
from quiz import quiz_loop
from game_select import menu_sequence

print(" ___   _    _____  ___   _   _      _    __   ")
print("| |_) \ \_/  | |  | |_) | | \ \  / | |  / /\  ")
print("|_|    |_|   |_|  |_| \ |_|  \_\/  |_| /_/--\ ")

cat, dif = menu_sequence()
quiz_loop(get_request(cat, dif))


