import json, sys

def setup(token, token_name, whitelist_user=None, whitelist_server=None, whitelist_bool=False):
    with open('tokens.json', 'r') as file:
        tokens = json.load(file)
    tokens[token_name] = token
    with open('tokens.json', 'w') as file:
        json.dump(tokens, file, indent=5)
    if whitelist_bool is True:
        with open('whitelist.json', 'r') as file:
            whitelist = json.load(file)
        whitelist["users"] = [whitelist_user]
        whitelist["servers"] = [whitelist_server]
        with open('whitelist.json', 'w') as file:
            json.dump(whitelist, file, indent=5)
            return print('Thank you')
    else:
        return print('Thank you')

with open('bot_start', 'r') as file:
    DOOM = file.read()
    print(DOOM)
text = 'Setup'
final = text.center(61, '=')
print(f'{final}')
token_name = input('What name would you like for your token? ')
token = input('What is your token? ')
bool_whitelist = input('Would you like to configure the command whitelist? ')
correct_val = False
while correct_val is not True:
    if bool_whitelist.lower() == 'yes':
        whitelist_user = input('What is the user id you would like to whitelist? ')
        whitelist_server = input('What is the server id you would like to whitelist? ')
        setup(token=token, token_name=token_name, whitelist_user=whitelist_user, whitelist_server=whitelist_server, whitelist_bool=True)
        correct_val = True
        sys.exit()
    elif bool_whitelist.lower() == 'no':
        setup(token=token, token_name=token_name)
        correct_val = True
        sys.exit()
    else:
        print('Not a valid input')
        bool_whitelist = input('Would you like to configure the command whitelist? ')