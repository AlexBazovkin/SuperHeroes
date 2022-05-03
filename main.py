import requests

book_of_heroes = {} # dict created from "create_book_of_heroes" def.
                    # (Key: "name", value: "intelligence")


def create_book_of_heroes(url):
    name = requests.get(url).json()["results"][0]["name"]
    intelligence = int(requests.get(url).json()["results"][0]["powerstats"]["intelligence"])
    book_of_heroes[name] = intelligence
    return

# Test lines:
create_book_of_heroes("https://superheroapi.com/api/2619421814940190/search/Hulk")
create_book_of_heroes("https://superheroapi.com/api/2619421814940190/search/Thanos")
create_book_of_heroes("https://superheroapi.com/api/2619421814940190/search/Captain America")


def get_the_smartest(dictionary):
    result = max(dictionary)
    return result


print(get_the_smartest(book_of_heroes))

