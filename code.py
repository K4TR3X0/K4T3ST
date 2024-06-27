MC = {
            "Hank": "Protagonista de la saga",
            "Sanford": "El primero de los 3 compañeros de el protagonista(Hank)",
            "Deimos": "El segundo de los 3 compañeros de el protagonista(Hank)",
            "2Bdamned": "El tercero de los 3 compañeros de el protagonista(Hank), pero este se encarga de devolver a la vida a los otros 3 si fallan en una mision",
            "Jebus": "Uno de los 2 antiheroes que existen en Nevada, considerado el salvador",
            "Tricky": "El otro antiheroe de Nevada, el payaso loco que hace lo que quiere",
            }
            
print("Bienvenido #Grunt# de este mundo.")

for i in range (5):
    word = input("Dime un personaje de las series de Madness Combat y te dire su rol(Recuerda la mayuscula del principio): ")

    if word in MC.keys():
        print(MC[word])
    else:
        print("Este personaje no existe.")
