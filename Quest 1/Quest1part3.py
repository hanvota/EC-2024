# Everybody.codes / The Kingdom of Algorithmia [ 2024 ] / Day-01
# https://everybody.codes/event/2024/quests/1

DATA_FILE = './everybody_codes_e2024_q01_p3.txt'
#DATA_FILE = './sample3.txt'

"""
Ancient Ant (A): Not very dangerous. Can be managed without using any potions.
Badass Beetle (B): A big and strong bug that requires 1 potion to defeat.
Creepy Cockroach (C): Fast and aggressive! This creature requires 3 potions to defeat it.
Diabolical Dragonfly (D): A fast and tricky enemy, hard to hit. This creature requires 5 potions to defeat it. 
"""
potions = {
    "A": 0,
    "B": 1,
    "C": 3,
    "D": 5
}

def solve_3(input_data: str) -> int:
    potions_needed = 0
    
    print(f'input_data = {input_data}')

    while input_data != '':
        foe1 = input_data[0]
        foe2 = input_data[1]
        foe3 = input_data[2]
        potions_for_battle = 0
        foes_in_battle = 3  # Assume we have 3 foes per battle. For every 'x'm we'll subtract 1 from this count to get the actual number of foes in battle.    
        if foe1 in potions:
            #print(f'potions[foe1] = {potions[foe1]}')
            potions_for_battle += potions[foe1]
        else:
            foes_in_battle -= 1
        
        if foe2 in potions:
            #print(f'potions[foe2] = {potions[foe2]}')
            potions_for_battle += potions[foe2]
        else:
            foes_in_battle -= 1
        
        if foe3 in potions:
            #print(f'potions[foe3] = {potions[foe3]}')
            potions_for_battle += potions[foe3]
        else:
            foes_in_battle -= 1
        
        if foes_in_battle <= 1:
            extra_potions_needed = 0
        elif foes_in_battle == 2:
            extra_potions_needed = 2
        elif foes_in_battle == 3:
            extra_potions_needed = 6
        
        potions_for_battle += extra_potions_needed 
        print(f'foe1 = {foe1}, foe2 = {foe2}, foe3 = {foe3}, potions_for_battle = {potions_for_battle}')
                            
        potions_needed += potions_for_battle 
        input_data = input_data[3:]  # Remove the first line after processing
        
    return potions_needed       
    

def main():
    with open(DATA_FILE, 'r') as f:
        #input_data = f.readlines()
        input_data = f.read().strip()  # .split('\n')

    #print(f'input_data = {input_data}')
    #print(f'Quest 01, Part 1-- Number of potions needed is {solve_1(input_data)}')
    #print(f'Quest 01, Part 2-- Number of potions needed is {solve_2(input_data)}')
    print(f'Quest 01, Part 3-- Number of potions needed is {solve_3(input_data)}')



if __name__ == '__main__':
    main()
