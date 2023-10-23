#Calls trivia api for a list of question based on the paramaters passed

import requests

#Limit can be adjusted here, I only did this for testing purposes
def get_request(cat, dif):
    if (cat != ""):
        categories = "categories=" + cat + "&"
    else:
        categories = ""

    difficulty = "difficulties=" + dif
    limit = "&limit=10"
    
    url = "https://the-trivia-api.com/api/questions?" + categories + limit + "&region=US&" + difficulty
    request = requests.get(url).json()

    return request
