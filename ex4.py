"""
Planet	Distance from sun
Mercury	57900000
Venus	108200000
Earth	149600000
Mars	227900000
Jupiter	778600000
Saturn	1433500000
Uranus	2872500000
Neptune	4495100000
"""
first_planet_input = input('Enter the distance from the sun for the first planet in KM')
second_planet_input = input('Enter the distance from the sun for the second planet in KM')
first_planet = int(first_planet_input)
second_planet = int(second_planet_input)
distance_km = second_planet - first_planet
print(abs(distance_km))