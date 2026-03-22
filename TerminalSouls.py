import random

# menu principal
def menu():
    opcion = ""

    while opcion != "1" and opcion != "2":

        print("\n/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
        print("        WELCOME TO THE FINAL BATTLE        ")
        print("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\n")

        print("1. Start Game")
        print("2. Exit")

        opcion = input("Choose an option: ")

        if opcion != "1" and opcion != "2":
            print("Invalid option, try again.\n")

    return opcion


def generar_damage(min, max):
    return random.randint(min, max)
    
def status(hp_heroe, hp_enemy):
    print("\nHERO health:", hp_heroe,"hp")
    print("ENEMY health:", hp_enemy,"hp")
    print("\n============================================")

def critical_hit(damage):
    prob = random.randint(1, 100)

    if prob <= 10:
        print("\nCRITICAL HIT!!!")
        print("Double the damage!!\n")
        return damage * 2

    return damage

def turn_player():
    global hp_heroe, hp_enemy, potion

    invalid_option = False

    while not invalid_option:

        print("""WHAT DO YOU WANT TO DO?:
                    1. Attack
                    2. Potion
                    3. Special Attack
        """)

        option = input("Choose: ")
        print("\n------------HERO'S TURN------------\n")

        if option == "1":
            damage = generar_damage(10, 25) 
            damage = critical_hit(damage)
            hp_enemy -= damage
            hp_enemy = max(hp_enemy, 0)
            print("YOU ATTACKED and dealt:",damage, "DAMAGE")
            invalid_option = True

        elif option == "2":
            if hp_heroe == 100:
                print("Your health is already full! Choose another option.")

            elif potion > 0:
                hp_heroe += 20 
                hp_heroe = min(hp_heroe, 100)
                potion -= 1 
                print("You used a potion, +20 HP") 
                print("Left:", potion)
                invalid_option = True
            else:
                print("No potions left!, you must choose another action")

        elif option == "3":
            probability = random.randint(1, 100)

            if probability <= 50:
                damage = generar_damage(30, 50)
                damage = critical_hit(damage)
                hp_enemy -= damage
                hp_enemy = max(hp_enemy, 0)
                print("SPECIAL ATTACK, damage:",damage)
            else:
                print("You failed your SPECIAL ATTACK")

            invalid_option = True
    
        else:
            print("INVALID OPTION")

def IA_enemy(hp_enemy):
    return hp_enemy <= 24

def turn_enemy():
    global hp_heroe, hp_enemy

    print("\n------------ENEMY'S TURN------------\n")

    if IA_enemy(hp_enemy):
        extra_health = 20
        hp_enemy += extra_health
        hp_enemy = min(hp_enemy, 120)
        print("Enemy used heal! +20 HP")

    else:
        damage = generar_damage(15, 20)
        damage = critical_hit(damage)
        hp_heroe -= damage
        hp_heroe = max(hp_heroe, 0)
        print("THE ENEMY ATTACKED you and dealt:",damage, "DAMAGE")

def who_won():
    global hp_heroe, hp_enemy

    if hp_enemy <= 0:
        print("\nCONGRATULATIONS, YOU WIN!!!")
        return True

    elif hp_heroe <= 0:
        print("\nTHE ENEMY WON, YOU LOST")
        return True

    return False        


# volver a jugar
jugar = "yes"

while jugar == "yes":

    opcion_menu = menu()

    if opcion_menu == "2":
        print("\nSee you later")
        break

    # reinicio de atributos iniciales
    hp_heroe = 100
    potion = 3
    hp_enemy = 120
    turn_heroe = True

    # Bucle principal
    while hp_heroe > 0 and hp_enemy > 0:
        status(hp_heroe, hp_enemy)

        if turn_heroe:
            turn_player()
            turn_heroe = False
        else:
            turn_enemy()
            turn_heroe = True

        if who_won():
            break

    print("\nEND GAME")

    jugar = input("\nDo you want to play again? (yes/no): ").lower()

    while jugar != "yes" and jugar != "no":
        jugar = input("Invalid option. Choose (yes/no): ").lower()

print("\nThanks for playing!!!")
