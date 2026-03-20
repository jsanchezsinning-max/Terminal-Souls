import random

#heroe
hp_heroe = 100
potion = 3

#enemigo
hp_enemy = 120

turn_heroe = True

print("-------------------------------")
print("MENU")
print("-------------------------------\n")
print("1. Start game\n2. Exit")

def generar_damage(min, max):
    return random.randint(min, max)
    
def status(hp_heroe, hp_enemy):
    print("\nhero health: ", hp_heroe)
    print("enemy health: ", hp_enemy)
    print()

def critical_hit(damage):
    critical_hit = random.randint(1, 100)

    if critical_hit <= 10:
        print("CRITICAL HIT!!!")
        return damage * 2

    return damage

def turn_player():
    global hp_heroe, hp_enemy, potion

    invalid_option = False

    while not invalid_option:

        print("""what are you going to do?:
                    1. Attack
                    2. Potion
                    3. Special Attack
        """)

        option = input("Choose: ")

        if option == "1":
            damage = generar_damage(10, 25) 
            damage = critical_hit(damage)
            hp_enemy -= damage
            print("you attacked and dealt ",damage, " damage")
            invalid_option = True

        elif option == "2":
            if hp_heroe == 100:
                print(" Your health is already full! Choose another option.")

            elif potion > 0:
                hp_heroe += 20 
                if hp_heroe >= 100:
                        hp_heroe = 100
                potion -= 1 
                print("you used a potion, Left: ", potion) 
                invalid_option = True
            else:
                print("No potions left!, you must choose another action")

        elif option == "3":
            probability = random.randint(1, 100)

            if probability <= 50:
                damage = generar_damage(30, 50)
                damage = critical_hit(damage)
                hp_enemy -= damage
                print("SPECIAL ATTACK, damage: ",damage)
            else:
                print("You failed your SPECIAL ATTACK")

            invalid_option = True
    
        else:
            print("INVALID OPTION")

def turn_enemy():
    global hp_heroe

    damage = generar_damage(15, 20)
    damage = critical_hit(damage)
    hp_heroe -= damage
    print("\nthe enemy attacked you and dealt: ",damage, " damage")

def who_won():
    global hp_heroe, hp_enemy

    if hp_heroe <= 0:
        print("THE ENEMY WON, YOU LOST")
        return True

    elif hp_enemy <= 0:
        print("YOU WIN!")
        return True

    return False        

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

print("END GAME")
