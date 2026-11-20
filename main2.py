cities = {
    "Rome": {
        "Country": "Italy",
        "Population": "2868000 people",
        "Fact": 'Rome is one of the oldest cities in the world, the capital of Ancient Rome. Therefore, Rome is often called the "eternal city".'
    },
    "Canberra": {
        "Country": "Australia",
        "Population": "381448 people",
        "Fact": 'The design of Canberra was based on the concept of a garden city, which includes significant areas of natural vegetation, which earned for Canberra the title of "bush capital" (translated from the English "forest capital").'
    },
    "Toronto": {
        "Country": "Canada",
        "Population": "2503281 people",
        "Fact": 'In the world of professional sports, the city is the most famous hockey team of Toronto Maple Leafs. The city holds the nickname of the "hockey universe center".'
    }
}

for city, info in cities.items():
    print(f"{city}:")
    for key, value in info.items():
        print(f"\t{key}: {value}")

