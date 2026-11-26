# Importacion lista con los pokemons validos con su tipo y numero de pokedex
from pokemon_validos import pokemon_validos

# Lista de pokemons capturados
PokemonCaptured = []
siguiente_id = 1


def menu():
    """Menu de la Pokedex."""
    print("================================")
    print("         PC de alguien          ")
    print("================================")
    print("1. Capturar Pokémon")
    print("2. Buscar Pokémon")
    print("3. Modificar Pokémon")
    print("4. Liberar Pokémon")
    print("5. Mostrar Pokémon")
    print("6. Salir")

def menu_busqueda():
    """Menu de busqueda"""
    print("================================")
    print("       Menu de Busqueda         ")
    print("================================")
    print("1. Buscar por ID")
    print("2. Filtrar por Especie")
    print("3. Filtrar por Mote")
    print("4. Filtrar por Shiny")
    print("5. Filtrar por Numero de Pokedex")
    print("6. Filtrar por tipo(s)")
    print("7. Volver al menu Global")

def menuModificar():
    """Menu de busqueda"""
    print("================================")
    print("       Menu de Modificar        ")
    print("================================")
    print("1. Cambiar mote")
    print("2. Cambiar nivel")
    print("3. Volver al menu Global")



def mostrar_pokemon(pokemon):
    """Muestra por terminal los datos de una captura."""
    datos_oficiales = pokemon_validos[pokemon["especie"]]
    tipos = ", ".join(datos_oficiales["tipo"])

    print("\n--- Datos de la captura ---")
    print(f"ID: {pokemon['id']}")
    print(f"Especie: {pokemon['especie']}")
    print(f"Número de Pokédex: {datos_oficiales['numero']}")
    print(f"Tipo(s): {tipos}")
    print(f"Nivel: {pokemon['nivel']}")
    print(f"Mote: {pokemon['mote']}")
    print(f"Shiny: {'Sí' if pokemon['shiny'] else 'No'}")

# Agregar la funcion para capturar pokemons(añadir a lista)
def capturar_pokemon():
    """Funcion para capturar pokemons(añadir a lista)."""

    # Pasamos la variable de siguiente_id para poder sumarle la ID
    global siguiente_id

    # Validacion y peticion del pokemon
    especie = input("Ingrese el nombre de la especie del Pokémon a capturar: ").strip().capitalize()
    while especie not in pokemon_validos:
        print("La especie no existe o no esta registrada")
        especie = input("Ingrese el nombre de la especie del Pokémon a capturar: ").strip().capitalize()

    # Si la especie introducida es valida hace la captura y sigue
    if especie in pokemon_validos:
        print(f"¡Has capturado a un {especie}!")
        
        # Validacion de nivel
        print("Que nivel tiene el Pokémon? (1-100)")
        try:
            nivel = int(input("Introduce el nivel: "))
        except ValueError:
            print("Entrada inválida. Debes escribir un número.")
            return
        if 1 <= nivel <= 100:
            print(f"¡El nivel de {especie} es {nivel}!")
            print("¿El Pokemon capturado es Shiny? (si/no)")
            respuestaShiny = input().lower()

            # Validacion si es shiny (booleano)
            # solo admite la respuesta si o no
            while respuestaShiny not in ["si", "no"]:
                print("Respuesta inválida. Por favor, responda 'si' o 'no'.")
                respuestaShiny = input().lower()
                
            if respuestaShiny == "si":
                shiny = True 
            elif respuestaShiny == "no":
                shiny = False
            else:
                print("Respuesta inválida. Se asignará 'no shiny' por defecto.")
                shiny = False

            print("¿Desea ponerle un mote al Pokémon? (si/no)")
            respuestaMote = input().lower()

            # solo admite la respuesta si o no
            while respuestaMote not in ["si","no"]:
                print("Respuesta inválida. Por favor, responda 'si' o 'no'.")
                respuestaMote = input().lower()
            
            if respuestaMote == "si":
                mote = input("Ingrese el mote para el Pokémon: ")
            elif respuestaMote == "no":
                mote = especie
            else:
                print("Respuesta inválida. Se asignará el nombre de la especie como mote.")
                mote = especie

            # se crea el pokemon con los parametros introducidos
            pokemon_capturado = {
                "id":siguiente_id,
                "especie":especie,
                "nivel":nivel,
                "mote":mote,
                "shiny":shiny}
            
            # se suma la id para que el siguiente que añadas tenga la siguiente id
            siguiente_id +=1

            # se agrega el pokemon a la lista
            PokemonCaptured.append(pokemon_capturado)
            
            print(f"¡Has capturado a {mote}({especie})!")
            mostrar_pokemon(pokemon_capturado)
        else:
            print("Nivel inválido. Por favor, ingrese un nivel entre 1 y 100.")
    else:
        print(f"{especie} no es un Pokémon válido. Por favor, ingrese un nombre de especie válido.")

def busquedaID():
    """Busca una captura por su ID."""

    # pide al usuario un numero entero para buscar por el id, si no es numero entero vuelve
    try:
        id_buscado = int(input("Introduce el ID que quieres buscar: "))
    except ValueError:
        print("Entrada inválida. Debes escribir un número.")
        return
    
    # se crea la variable de encontrado
    encontrado = False

    # bussqueda de la captura
    for captura in PokemonCaptured:

        # si la id de la captura equivale a la buscada muestra el pokemon, devuelve el pokemon y encontrado lo pone en true
        if captura["id"] == id_buscado:
            mostrar_pokemon(captura)
            encontrado = True
            return captura
        
    # si no lo encontró no devuelve nada
    if not encontrado:
        print(f"No se ha encontrado ninguna captura con el ID {id_buscado}.")

def busquedaEspecie():
    """Filtra las capturas por su especie."""
    especie = input("Introduce la especie que quieres filtrar: ").strip().capitalize()

    # comprueba que la especie introducida se encuentre en la validacion
    if especie not in pokemon_validos:
        print(f"{especie} no es una especie válida.")
        return
    
    # se crea la variable de encontrado
    encontrado = False

    # busqueda de la captura
    for captura in PokemonCaptured:

        #si la especie equivale a la especie buscada muestra todos los pokemons que tengan dicha especie y encontrado lo pone en true
        if captura["especie"] == especie:
            mostrar_pokemon(captura)
            encontrado = True

    # si no lo encontró no devuelve nada
    if not encontrado:
        print(f"No se ha encontrado ninguna captura de la especie {especie}.")


def busquedaMote():
    """Filtra las capturas por su mote."""
    mote = input("Introduce el mote que quieres filtrar: ").strip()

    # se crea la variable de encontrado
    encontrado = False

    #busqueda de la captura
    for captura in PokemonCaptured:
        #si el mote equivale a el mote buscado muestra todos los pokemons que tengan dicho mote y encontrado lo pone en true
        if captura["mote"].strip().lower() == mote.lower():
            mostrar_pokemon(captura)
            encontrado = True
    
    # si no lo encontró no devuelve nada
    if not encontrado:
        print(f"No se ha encontrado ninguna captura con el mote: {mote}.")
    
def busquedaShiny():
    """Filtra las capturas Shiny"""

    respuesta = input("¿Quieres filtrar por Pokémon shiny? (si/no): ").strip().lower()
    
    # validacion de shiny (booleano)
    # solo admite la respuesta si o no
    if respuesta == "si":
        shiny = True
    elif respuesta == "no":
        shiny = False
    else:
        print("Respuesta inválida. Escribe si o no.")
        return

    # se crea la variable de encontrado
    encontrado = False

    # busqueda de la captura
    for captura in PokemonCaptured:
        
        # muestra el pokemon si es shiny y pon encontrado a true
        if captura["shiny"] == shiny:
            mostrar_pokemon(captura)
            encontrado = True

    # si no lo encontró no devuelve nada
    if not encontrado:
        print(f"No se ha encontrado ningun con el requisito especificado")
        

def busquedaNumeroPokedex():
    """Filtra las capturas por numero de pokedex"""
    
    # variable que pide un numero entero, en caso contrario devuelve entrada invalida
    try:
        numPokedex = int(input("Introduce el numero de pokedex que quieres filtrar: "))
    except ValueError:
        print("Entrada inválida. Debes escribir un número.")
        return

    # validacion numero de pokedex, minimo: 1, maximo: 151
    if not 1 <= numPokedex <= 151:
        print("El número debe estar entre 1 y 151.")
        return
    
    # se crea la variable de encontrado
    encontrado = False

    # busqueda de la captura
    for captura in PokemonCaptured:
        
        # si el numero de la pokedex del pokemon valido equivale al numero de pokedex introducido muestra al pokemon y pone encontrado en true
        if pokemon_validos[captura["especie"]]["numero"] == numPokedex:
            mostrar_pokemon(captura)
            encontrado = True

    # si no lo encontro no devuelve nada
    if not encontrado:
        print(f"No se ha encontrado ninguna captura con el numero de la pokedex {numPokedex}.")

def busquedaTipo():
    """Filtra las capturas por tipo"""
    
    # introduccion de variable tipo 1(OBLIGATORIA PARA LA BUSQUEDA)
    tipo1 = input("Introduce el primer tipo: ").strip().capitalize()
    
    # introduccion de variable tipo 2 (OPCIONAL PARA LA BUSQUEDA)
    tipo2 = input("Introduce el segundo tipo (o pulsa Enter para omitirlo): ").strip().capitalize()

    # se crea la variable encontrado
    encontrado = False

    # busqueda de la captura
    for captura in PokemonCaptured:
        # busca de los tipos validados los tipos oficiales de la especie actual
        tipos_pokemon = pokemon_validos[captura["especie"]]["tipo"]
        
        # la captura debe de tener el primer tipo de manera obligatoria
        if tipo1 in tipos_pokemon:
            
            # el segundo tipo si es dejado en blanco/vacio no comprobamos segundo tipo, y si si es rellenado la captura debe de tener ese segundo tipo
            if tipo2 == "" or tipo2 in tipos_pokemon:
                mostrar_pokemon(captura)
                encontrado = True

    # si no lo encontró no devuelve nada
    if not encontrado:
        print(f"No se ha encontrado ninguna captura con el numero de la pokedex {tipo1}{tipo2}.")

def buscar_pokemon():
    """Funcion menu buscar pokemons"""
    
    # creacion variable de opcion, obligatorio para entrar al while
    opcion = ""

    # mientras no introduca la opcion 7(salida) sigue dando vueltas por el menu de busqueda
    while opcion != "7":
        
        # muestra el menu de busqueda
        menu_busqueda()
        
        # sobrescrive la variable de opcion
        opcion = input("Seleccione la manera de buscar/fltrar: ")

        # si opcion = 1 entra en la funcion busquedaID() para buscar el pokemon especificado
        if opcion == "1":
            busquedaID()
            
        # si opcion = 2 entra en la funcion busquedaEspecie() para filtrar la especie especificada    
        elif opcion == "2":
            busquedaEspecie()

        # si opcion = 3 entra en la funcion busquedaMote() para filtrar por el mote especificada               
        elif opcion == "3":
            busquedaMote()
        
        # si opcion = 4 entra en la funcion busquedaShiny() para filtrar por la variante shiny especificado
        elif opcion == "4":
            busquedaShiny()
        
        # si opcion = 5 entra en la funcion busquedaNumeroPokedex() para filtrar por el numero de la pokedex especificada
        elif opcion == "5":
            busquedaNumeroPokedex()
            
        # si opcion = 6 entra en la funcion busquedaTipo() para filtrar por el/los tipo/s especificado/s
        elif opcion == "6":
            busquedaTipo()
            
        # si opcion = 7 sale del bucle y vuelve al menu general   
        elif opcion == "7":
            print("Saliendo del menu de busqueda")
            return
        
        # si no es un numero entero (1-7) dibuja en pantalla respuesta invalida y vuelve a hacer el bucle
        elif opcion not in ["1","2","3","4","5","6","7"]:
            print("Respuesta inválida. Volviendo a mostrar el menu de busqueda. ")


def modificar_pokemon():
    """Modifica las caracteristicas no esenciales del pokemon"""
    
    # valida que el id a buscar sea entero, sino vuelve y dibuja en pantalla entrada invalida
    try:
        id_buscado = int(input("Introduce un ID para modificar el pokemon: "))
    except ValueError:
        return print("Entrada inválida, debes introducir un numero")

    # creamos parametro encontrado
    encontrado = False


    # busqueda de la captura
    for captura in PokemonCaptured:
        
        # si el id de la captura es el mismo que el buscado muestra el pokemon, pone encontrado en true y muestra el menu de modificacion
        if captura["id"] == id_buscado:
            mostrar_pokemon(captura)
            encontrado = True
            menuModificar()
            
            # valida que la opcion sea entero, sino vuelve y dibuja en pantalla entrada invalida
            try:
                opcion = int(input("Elige una opcion para modificar el pokemon: "))
            except ValueError:
                return print("Entrada inválida, debes introducir un numero")
            
            # si opcion = 1 pide mote nuevo para captura
            if opcion == 1:
                captura["mote"] = input(f"Introduce el mote nuevo para {captura['mote']}")

            # si opcion = 2 pide el nivel nuevo para captura    
            elif opcion == 2:
                
                # valida que el nivel sea entero, sino vuelve y dibuja en pantalla entrada invalida
                try:
                    nivel_nuevo = int(input(f"Introduce el nivel nuevo (actual: {captura['nivel']}): "))
                except ValueError:
                    print("Entrada inválida. Debes introducir un número.")
                    return


                # si el nivel no esta entre el 1 al 100, cambia el nivel antiguo al nuevo y enseña por pantalla nivel actualizado
                if 1 <= nivel_nuevo <= 100:
                    captura["nivel"] = nivel_nuevo
                    print("Nivel actualizado.")
                    
                # si no es valido devuelve los requisitos    
                else:
                    print("El nivel debe estar entre 1 y 100.")
                    
            # si opcion = 3 vuelve al menu general        
            elif opcion == 3:
                print("Volviendo al menu general")
                return
            
            # si opcion no es un numero del 1 al 3, te enseña por pantalla los requisitos del menu
            else:
                print("Opción inválida. Elige una opción del menú.")
    
    # si no es encontrado, no devuelve nada
    if not encontrado:
        print(f"No se ha encontrado ninguna captura con el ID {id_buscado}.")

def liberar_pokemon():
    """Libera al pokemon por ID"""

    # valida que el id a buscar sea entero, sino vuelve y dibuja en pantalla entrada invalida
    try:
        id_buscado = int(input("Introduce un ID para liberar el pokemon"))
    except ValueError:
        return print("Entrada inválida, debes introducir un numero")

    # se crea variable encontrado
    encontrado = False

    # busqueda captura
    for captura in PokemonCaptured:

        # si la id de captura es igual a la del id buscado muestra el pokemon, activa encontrado y pide confirmacion para liberar el pokemon
        if captura["id"] == id_buscado:
            mostrar_pokemon(captura)
            confirmacion = input("¿Seguro que quieres liberar el pokemon del PC?").strip().lower()
            encontrado = True

            # confirmacion = si libera captura
            if confirmacion == "si":
                PokemonCaptured.remove(captura)
                print(f"Has liberado a {captura['mote']} ({captura['especie']}).")
                return

            # confirmacion = no cancela liberacion captura    
            elif confirmacion == "no":
                print("Liberación cancelada, volviendo al menu")
                return
            
            # si confirmacion no es ni si ni no enseña por pantalla los requisitos y vuelve
            else:
                print("Respuesta inválida. Escribe 'si' o 'no'.")
                return

    # si no es encontrado, no devuelve nada     
    if not encontrado:
        print(f"No se ha encontrado ninguna captura con el ID {id_buscado}.")



def mostrar_pokemons():
    """Muestra todos los pokemons"""
    
    # se crea variable encontrado
    encontrado = False
    
    # busqueda captura
    for captura in PokemonCaptured:

        # por cada captura los muestra y activa encontrado
        mostrar_pokemon(captura)
        encontrado = True

    # si no es encontrado no se dispone de pokemons en el PC    
    if not encontrado:
        print("No dispones ningun pokemon en el PC")


def main():
    """Funcion principal para actuar a las demas funciones"""
    
    # entra en el bucle, enseña el menu y espera a que introduzcas una opción
    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        # opcion = 1 funcion capturar_pokemon(), captura pokemon
        if opcion == "1":
            capturar_pokemon()

        # opcion = 2 funcion buscar_pokemon(), muestra menu de busqueda
        elif opcion == "2":
            buscar_pokemon()
            
        #  opcion = 3 funcion modificar_pokemon(), muestra menu modificar    
        elif opcion == "3":
            modificar_pokemon()

        # opcion = 4 funcion liberar_pokemon(), liberacion captura    
        elif opcion == "4":
            liberar_pokemon()
            
        # opcion = 5 funcion mostrar_pokemons(), muestra todos los pokemons disponibles    
        elif opcion == "5":
            mostrar_pokemons()

        # opcion = 6 sale del programa con break    
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        
        # sino se introduce un numero del 1 al 6, enseña por pantalla opcion invalida y vuelve a hacer el bucle
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

main()