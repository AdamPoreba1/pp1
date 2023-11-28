countries = [
    {"name":"Poland", "population":38000000},
    {"name": "Slovakia", "population":5447000},
    {"name": "Germany", "population":83200000},
    {"name": "Spain", "population":47420000},
    {"name": "Turkey", "population":84780000},
]


i = 0
while i < len(countries):
    string = ""
    dictionary = countries[i]
    string += dictionary["name"] + " "
    string += "Population:" + str(dictionary["population"])
    print(string)
    string = ""
    i = i + 1


