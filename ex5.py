planets = ["Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"]
usr_input  = input("Entet in capital")
planets_index = planets.index(usr_input)
print("Here are the planets closer than " + usr_input)
print(planets[0:planets_index])
print("Here are the planets further than " + usr_input)
print(planets[planets_index + 1:])# Enter code below