# Everybody.codes / The Kingdom of Algorithmia [ 2024 ] / Day-01
# https://everybody.codes/event/2024/quests/1

DATA_FILE = 'everybody_codes_e2024_q01_p1.txt'
#DATA_FILE = 'sample1.txt'

"""
Ancient Ant (A): Not very dangerous. Can be managed without using any potions.
Badass Beetle (B): A big and strong bug that requires 1 potion to defeat.
Creepy Cockroach (C): Fast and aggressive! This creature requires 3 potions to defeat it.
"""
potions = {
    "A": 0,
    "B": 1,
    "C": 3
}

def solve_1(input_data: str) -> int:
    potions_needed = 0
    
    for foe in input_data[0]:
        print(f'foe = {foe}')
        if foe in potions:
            print(f'potions[foe] = {potions[foe]}')
            potions_needed += potions[foe]
        else:
            print(f'Unknown foe: {foe}')
            
        input_data = input_data[1:]  # Remove the first line after processing
        
    return potions_needed       
    

def main():
    with open(DATA_FILE, 'r') as f:
        input_data = f.readlines()
        # input_data = f.read().strip()  # .split('\n')

    print(f'input_data = {input_data}')
    print(f'Quest 01, Part 1-- Number of potions needed is {solve_1(input_data)}')
    #print(f'Quest 01, Part 2--Solution to captcha is {solve_2(input_data)}')


if __name__ == '__main__':
    main()
    