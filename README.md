# Terminal Souls – Final Battle

## Description
Terminal Souls – Final Battle is a turn-based combat game developed in Python and played in the console.  
The player controls a hero who battles an enemy using different actions such as attacks, potions, and special abilities.

The game includes random damage, critical hits, enemy AI, and input validation to create a dynamic experience.

---

## Features
- Turn-based combat system
- Random damage generation
- Critical hit mechanic (10% chance)
- Healing system with limited potions
- Basic enemy AI (heals when low HP)
- Replay system (play again option)
- Input validation

---

## Technologies Used
- Python 3
- random module

---

## Game Mechanics

### Player Actions
- Attack: Deals 10–25 damage
- Potion: Restores 20 HP (max 100 HP)
- Special Attack: Deals 30–50 damage with 50% success rate

### Enemy Behavior
- Attacks with 15–20 damage
- Heals 20 HP when health is less than or equal to 24

### Critical Hits
- 10% chance to double damage

---

## How to Run

1. Make sure Python is installed  
2. Clone or download the project  
3. Run the file:

```bash
python main.py
