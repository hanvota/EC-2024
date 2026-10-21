# Everybody.codes / The Kingdom of Algorithmia [ 2024 ] / Day-01
# https://everybody.codes/event/2024/quests/1

DATA_FILE = './everybody_codes_e2024_q01_p2.txt'
#DATA_FILE = './sample2.txt'

"""
Ancient Ant (A): Not very dangerous. Can be managed without using any potions.
Badass Beetle (B): A big and strong bug that requires 1 potion to defeat.
Creepy Cockroach (C): Fast and aggressive! This creature requires 3 potions to defeat it.
Diabolical Dragonfly (D): A fast and tricky enemy, hard to hit. This creature requires 5 potions to defeat it. 
"""
potions = {
    "A": 1,
    "B": 2,
    "C": 4,
    "D": 6,
    "x": -1
}

def solve_2(input_data: str) -> int:
    potions_needed = 0
    
    print(f'input_data = {input_data}')

    while input_data != '':
        foe1 = input_data[0]
        foe2 = input_data[1]
        potions_for_battle = 0
            
        if foe1 in potions:
            #print(f'potions[foe1] = {potions[foe1]}')
            potions_for_battle += potions[foe1]
        else:
            print(f'Unknown foe1: {foe1}')
        
        if foe2 in potions:
            #print(f'potions[foe2] = {potions[foe2]}')
            potions_for_battle += potions[foe2]
        else:
            print(f'Unknown foe2: {foe2}')
              
        print(f'foe1 = {foe1}({potions[foe1]}), foe2 = {foe2}({potions[foe2]}), potions_for_battle = {potions_for_battle}')
                
        if potions_for_battle < 0:  # Battle with 2 'x' foes, no potions needed
            potions_for_battle = 0
            
        potions_needed += potions_for_battle 
        input_data = input_data[2:]  # Remove the first line after processing
        
    return potions_needed       
    

def main():
    with open(DATA_FILE, 'r') as f:
        #input_data = f.readlines()
        input_data = f.read().strip()  # .split('\n')

    #print(f'input_data = {input_data}')
    #print(f'Quest 01, Part 1-- Number of potions needed is {solve_1(input_data)}')
    print(f'Quest 01, Part 2-- Number of potions needed is {solve_2(input_data)}')


if __name__ == '__main__':
    main()
