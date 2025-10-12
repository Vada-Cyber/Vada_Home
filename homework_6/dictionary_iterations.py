persons_list = {
    'Georgia' : 'Tbilisi',
    'USA' : 'NYC',
    'Zimbabwe' : 'Harare',
    'Australia' : 'Canberra',
    'Canada' : 'Ottawa',
    'Japan' : 'Tokyo'
}

for country, city in persons_list.items():
    print(f"The capital of {country} is {city}.")

    country = city
    city = country

    inverted_list = {city: country for country, city in persons_list.items()}


    #print(f"The {country} city is a capital of {city}.")
persons_list = inverted_list
for city, country in inverted_list.items():
    print(f"{city} city is a capital of {country}.")
