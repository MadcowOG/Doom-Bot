import json, sys, subprocess, platform

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
        return print('Token.json and whitelist.json configured')
    else:
        return print('Token.json configured')

def ffmpeg_setup():
    if platform.system() != 'Windows':
        print('Not on Windows -- If you are on windows and this appears please report a ticket at the github')
        sys.exit()
    print('!--Will now run a powershell script to download ffmpeg and set environment path--!')
    p = subprocess.Popen(['powershell.exe', './setup.ps1'], stdout=sys.stdout)
    p.communicate()
    return print('ffmpeg downloaded and configured')

with open('bot_start', 'r') as file:
    DOOM = file.read()
    print(DOOM)
text = 'Setup'
final = text.center(61, '=')
print(f'{final}')
text = 'NOTE'
final = text.center(200, '-')
print(final)
print('If you input incorrect information the bot will not work correctly use the reset script to return the files to their original state, if you know you may do it yourself')
print(final)
token_name = input('What name would you like for your token? ')
token = input('What is your token? ')
bool_whitelist = input('Would you like to configure the command whitelist?**Needed for whitelisted commands** ')
if platform.system() == 'Windows':
    bool_ffmpeg = input('Would you like to install and configure ffmpeg?**Recommended Unless already done** ')
correct_val = False
while correct_val is not True:
    if bool_whitelist.lower() == 'yes' or bool_whitelist.lower() == 'y':
        whitelist_user = input('What is the user id you would like to whitelist? ')
        whitelist_server = input('What is the server id you would like to whitelist? ')
        if platform.system() == 'Windows':
            correct_val_ffmpeg = False
            while correct_val_ffmpeg is not True:
                if bool_ffmpeg.lower() == 'yes' or bool_ffmpeg.lower() == 'y':
                    ffmpeg_setup()
                    correct_val_ffmpeg = True
                elif bool_ffmpeg.lower() == 'no' or bool_ffmpeg.lower() == 'n':
                    correct_val_ffmpeg = True
                else:
                    print('Not a valid input')
                    bool_ffmpeg = input('Would you like to install and configure ffmpeg?**Recommended Unless already done** ')
        setup(token=token, token_name=token_name, whitelist_user=whitelist_user, whitelist_server=whitelist_server, whitelist_bool=True)
        correct_val = True
        print('Thank you')
        sys.exit()
    elif bool_whitelist.lower() == 'no':
        setup(token=token, token_name=token_name)
        if platform.system() == 'Windows':
            correct_val_ffmpeg = False
            while correct_val_ffmpeg is not True:
                if bool_ffmpeg.lower() == 'yes' or bool_ffmpeg.lower() == 'y':
                    ffmpeg_setup()
                    correct_val_ffmpeg = True
                elif bool_ffmpeg.lower() == 'no' or bool_ffmpeg.lower() == 'n':
                    correct_val_ffmpeg = True
                else:
                    print('Not a valid input')
                    bool_ffmpeg = input('Would you like to install and configure ffmpeg?**Recommended Unless already done** ')
        correct_val = True
        print('Thank you')
        sys.exit()
    else:
        print('Not a valid input')
        bool_whitelist = input('Would you like to configure the command whitelist? ')