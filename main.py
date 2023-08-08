import string
import sys
import random

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "0"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "~"]

def create_random_string():
    try:
        characters = int(input("\nHow Many Characters Do You Want This Password To Have?: "))
    except ValueError:
        print("Wrong Input.")
        sys.exit()
    print("\nChoose One Or More Of These Options: \nLetters(L)\nNumbers(N)\nSymbols(S)")
    character_choices = input("\nInput: ").lower()
    
    if character_choices == "L".lower():
        return ''.join(random.choice(string.ascii_letters) for x in range(characters))
    if character_choices == "N".lower():
        return ''.join(random.choice(numbers) for x in range(characters))
    if character_choices == "S".lower():
        return ''.join(random.choice(symbols) for x in range(characters))
    if character_choices == "LN".lower() or character_choices == "NL".lower():
        merged_length = min(len(string.ascii_letters), len(numbers))
        random_indices = random.sample(range(merged_length), merged_length)
        merged_list = [string.ascii_letters[idx] + numbers[idx] for idx in random_indices]
        return ''.join(random.choice(merged_list) for x in range(characters))
    if character_choices == "LS".lower() or character_choices == "SL".lower():
        merged_length = min(len(string.ascii_letters), len(symbols))
        random_indices = random.sample(range(merged_length), merged_length)
        merged_list = [string.ascii_letters[idx] + symbols[idx] for idx in random_indices]
        return ''.join(random.choice(merged_list) for x in range(characters))
    if character_choices == "SN".lower() or character_choices == "NS".lower():
        merged_length = min(len(numbers), len(symbols))
        random_indices = random.sample(range(merged_length), merged_length)
        merged_list = [numbers[idx] + symbols[idx] for idx in random_indices]
        return ''.join(random.choice(merged_list) for x in range(characters))
    if character_choices == "NSL".lower() or character_choices == "NLS".lower() or character_choices == "SNL".lower() or character_choices == "SLN".lower() or character_choices == "LNS".lower() or character_choices == "LSN".lower():
        merged_length = min(len(string.ascii_letters), len(symbols), len(numbers))
        random_indices = random.sample(range(merged_length), merged_length)
        merged_list = [string.ascii_letters[idx] + symbols[idx] + numbers[idx] for idx in random_indices]
        return ''.join(random.choice(merged_list) for x in range(characters))

print(create_random_string())