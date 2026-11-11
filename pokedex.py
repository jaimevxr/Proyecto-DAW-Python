# Importacion lista con los pokemons validos con su tipo y numero de pokedex
from pokemon_validos import pokemon_validos

# Lista de pokemons capturados
PokemonCaptured = []

class Pokemon:
    """Representa una captura de Pokémon."""

    siguiente_id = 1

    def __init__(self, especie, nivel, mote="", shiny=False):
        self.id = Pokemon.siguiente_id
        Pokemon.siguiente_id += 1
        self.especie = especie
        self.nivel = nivel
        self.mote = mote
        self.shiny = shiny



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

def mostrar_pokemon(pokemon):
    """Muestra por terminal los datos de una captura."""
    datos_oficiales = pokemon_validos[pokemon.especie]
    tipos = ", ".join(datos_oficiales["tipo"])

    print("\n--- Datos de la captura ---")
    print(f"ID: {pokemon.id}")
    print(f"Especie: {pokemon.especie}")
    print(f"Número de Pokédex: {datos_oficiales['numero']}")
    print(f"Tipo(s): {tipos}")
    print(f"Nivel: {pokemon.nivel}")
    print(f"Mote: {pokemon.mote}")
    print(f"Shiny: {'Sí' if pokemon.shiny else 'No'}")

# Agregar la funcion para capturar pokemons(añadir a lista)
def capturar_pokemon():
    """Funcion para capturar pokemons(añadir a lista)."""

    especie = input("Ingrese el nombre de la especie del Pokémon a capturar: ").strip().capitalize()

    if especie in pokemon_validos:
        print(f"¡Has capturado a un {especie}!")

        print("Que nivel tiene el Pokémon? (1-100)")
        try:
            nivel = int(input())
        except ValueError:
            print("Entrada inválida. Debes escribir un número.")
            return
        if 1 <= nivel <= 100:
            print(f"¡El nivel de {especie} es {nivel}!")
            print("¿El Pokemon capturado es Shiny? (si/no)")
            respuestaShiny = input().lower()

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

            if respuestaMote == "si":
                mote = input("Ingrese el mote para el Pokémon: ")
            elif respuestaMote == "no":
                mote = especie
            else:
                print("Respuesta inválida. Se asignará el nombre de la especie como mote.")
                mote = especie
            
            pokemon_capturado = Pokemon(
                especie=especie,
                nivel=nivel,
                mote=mote,
                shiny=shiny)
            PokemonCaptured.append(pokemon_capturado)
            
            print(f"¡Has capturado a {mote}({especie})!")
            mostrar_pokemon(pokemon_capturado)
        else:
            print("Nivel inválido. Por favor, ingrese un nivel entre 1 y 100.")
    else:
        print(f"{especie} no es un Pokémon válido. Por favor, ingrese un nombre de especie válido.")

def buscar_pokemon():
    # menu_busqueda()
    opcion = -1
    # opcion = input("Introduzca el numero para buscar/filtrar: ")

    while opcion not in [1,2,3,4,5,6,7]:
        menu_busqueda()
        opcion = input("Introduzca el numero para buscar/filtrar: ")

        if opcion == "1":
            busquedaID()
        elif opcion == "2":
            busquedaEspecie()
        elif opcion == "3":
            BusquedaMote()
        elif opcion == "4":
            BusquedaShiny()
        elif opcion == "5":
            BusquedaNumeroPokedex()
        elif opcion == "6":
            BusquedaTipo()
        elif opcion == "7":
            print("Saliendo del menu de busqueda")
            return
        elif opcion not in [1,2,3,4,5,6,7]:
            print("Respuesta inválida. Volviendo a mostrar el menu de busqueda. ")

    




def main():
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