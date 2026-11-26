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

    if respuesta == "si":
        shiny = True
    elif respuesta == "no":
        shiny = False
    else:
        print("Respuesta inválida. Escribe si o no.")
        return

    encontrado = False

    for captura in PokemonCaptured:
        if captura["shiny"] == shiny:
            mostrar_pokemon(captura)
            encontrado = True

    if not encontrado:
        print(f"No se ha encontrado ningun con el requisito especificado")
        

def busquedaNumeroPokedex():
    """Filtra las capturas por numero de pokedex"""
    try:
        numPokedex = int(input("Introduce el numero de pokedex que quieres filtrar: "))
    except ValueError:
        print("Entrada inválida. Debes escribir un número.")
        return

    if not 1 <= numPokedex <= 151:
        print("El número debe estar entre 1 y 151.")
        return
    
    encontrado = False

    for captura in PokemonCaptured:
        if pokemon_validos[captura["especie"]]["numero"] == numPokedex:
            mostrar_pokemon(captura)
            encontrado = True

    if not encontrado:
        print(f"No se ha encontrado ninguna captura con el numero de la pokedex {numPokedex}.")

def busquedaTipo():
    """Filtra las capturas por tipo"""

    tipo1 = input("Introduce el primer tipo: ").strip().capitalize()
    tipo2 = input("Introduce el segundo tipo (o pulsa Enter para omitirlo): ").strip().capitalize()

    
    encontrado = False

    for captura in PokemonCaptured:
        tipos_pokemon = pokemon_validos[captura["especie"]]["tipo"]
        if tipo1 in tipos_pokemon:
            if tipo2 == "" or tipo2 in tipos_pokemon:
                mostrar_pokemon(captura)
                encontrado = True

    if not encontrado:
        print(f"No se ha encontrado ninguna captura con el numero de la pokedex {tipo1}{tipo2}.")

def buscar_pokemon():
    """Funcion menu buscar pokemons"""
    opcion = ""

    while opcion != "7":
        menu_busqueda()
        opcion = input("Seleccione la manera de buscar/fltrar: ")

        if opcion == "1":
            busquedaID()
        elif opcion == "2":
            busquedaEspecie()
        elif opcion == "3":
            busquedaMote()
        elif opcion == "4":
            busquedaShiny()
        elif opcion == "5":
            busquedaNumeroPokedex()
        elif opcion == "6":
            busquedaTipo()
        elif opcion == "7":
            print("Saliendo del menu de busqueda")
            return
        elif opcion not in ["1","2","3","4","5","6","7"]:
            print("Respuesta inválida. Volviendo a mostrar el menu de busqueda. ")


def modificar_pokemon():
    """Modifica las caracteristicas no esenciales del pokemon"""
    try:
        id_buscado = int(input("Introduce un ID para modificar el pokemon: "))
    except ValueError:
        return print("Entrada inválida, debes introducir un numero")

    encontrado = False

    for captura in PokemonCaptured:
        if captura["id"] == id_buscado:
            mostrar_pokemon(captura)
            encontrado = True
            menuModificar()
            try:
                opcion = int(input("Elige una opcion para modificar el pokemon: "))
            except ValueError:
                return print("Entrada inválida, debes introducir un numero")
            if opcion == 1:
                captura["mote"] = input(f"Introduce el mote nuevo para {captura['mote']}")
            elif opcion == 2:
                try:
                    nivel_nuevo = int(input(f"Introduce el nivel nuevo (actual: {captura['nivel']}): "))
                except ValueError:
                    print("Entrada inválida. Debes introducir un número.")
                    return

                if 1 <= nivel_nuevo <= 100:
                    captura["nivel"] = nivel_nuevo
                    print("Nivel actualizado.")
                else:
                    print("El nivel debe estar entre 1 y 100.")
            elif opcion == 3:
                print("Volviendo al menu general")
                return
            else:
                print("Opción inválida. Elige una opción del menú.")
            
    if not encontrado:
        print(f"No se ha encontrado ninguna captura con el ID {id_buscado}.")

def liberar_pokemon():
    """Libera al pokemon por ID"""

    try:
        id_buscado = int(input("Introduce un ID para liberar el pokemon"))
    except ValueError:
        return print("Entrada inválida, debes introducir un numero")

    encontrado = False

    for captura in PokemonCaptured:
        if captura["id"] == id_buscado:
            mostrar_pokemon(captura)
            confirmacion = input("¿Seguro que quieres liberar el pokemon del PC?").strip().lower()
            encontrado = True
            if confirmacion == "si":
                PokemonCaptured.remove(captura)
                print(f"Has liberado a {captura['mote']} ({captura['especie']}).")
                return
            elif confirmacion == "no":
                print("Liberación cancelada, volviendo al menu")
                return
            else:
                print("Respuesta inválida. Escribe 'si' o 'no'.")
                return

            
    if not encontrado:
        print(f"No se ha encontrado ninguna captura con el ID {id_buscado}.")



def mostrar_pokemons():
    """Muestra todos los pokemons"""
    encontrado = False
    for captura in PokemonCaptured:
        mostrar_pokemon(captura)
        encontrado = True
    if not encontrado:
        print("No dispones ningun pokemon en el PC")


def main():
    """Funcion principal para actuar a las demas funciones"""
    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            capturar_pokemon()
        elif opcion == "2":
            buscar_pokemon()
        elif opcion == "3":
            modificar_pokemon()
        elif opcion == "4":
            liberar_pokemon()
        elif opcion == "5":
            mostrar_pokemons()
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

main()