import random

#heroe
hp_heroe = 100
potion = 3

#enemigo
hp_enemigo = 120

print("MENU")
print("1. Start game\n2. Exit")

def generar_damage(min, max):
    return random.randint(min, max)
    
def status(hp_heroe, hp_enemigo):
    print("hero health: ", hp_heroe)
    print("enemy health: ", hp_enemigo)

def turn_heroe():
    global hp_heroe, hp_enemigo, potion

    invalid_option = False

    while invalid_option == False:

        print("""what are you going to do?:
                    1. Attack
                    2. Potion
                    3. Special Power
        """)

    if invalid_option == "1":
        damage = generar_damage(10, 25) 
        hp_enemigo -= damage
        print("you attacked and dealt ",damage, " damage")
        invalid_option == True

    if invalid_option == "2":
        hp_heroe += 20 
        potion -= 1 
        print("you used a potion, te quedan: ", potion) 



while hp_heroe > 0 and hp_enemigo > 0:
    print("hola")
