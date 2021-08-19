import json, sys

def reset():
    with open('tokens.json', 'w') as file:
        text = {}
        json.dump(text, file)
    with open('whitelist.json', 'w') as file:
        text  = {}
        json.dump(text, file)
    return print('Reset')

assurance = input('You understand that by running this script you are erasing any configurations in the tokens.json and whitelist.json files? ')
correct_val = False
while correct_val is False:
    if assurance.lower() == 'yes':
        reset()
        sys.exit()
    elif assurance.lower() == 'no':
        sys.exit()
    else:
        print('Not valid input')
        assurance = input('You understand that by running this script you are erasing any configurations in the tokens.json and whitelist.json files? ')