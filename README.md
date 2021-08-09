I'm not sure what to put in here or whether what I'm going to write is the correct way to state these ideas, any help would be appreciated:
***


# Prologue
Please use this bot as you like, at the moment it is built to be hosted locally. But it is still a work in progress, so I would enjoy it if you provided some feedback and contributed a little. I am not sure what license to use, and I am not a lawyer nor do I have one, so I am just going with GPLv2

# Prerequisites
* _Optional:_
    *  Create a virtual python environment, while in the same directory as the bot do these commands:
        * `python3 -m venv venv`
        * `source ./venv/bin/activate`
* Must have the latest version of Python, and ffmpeg, install these with your distros package manager
* Libraries required, <span>discord.py<span>\[audio\], youtube_dl install with these commands:
    * `pip install 'discord.py[audio]' youtube_dl`

# Setup
You must first add the bot to your discord server first:
1. Add to tokens.json
    * In tokens.json format your tokens inside the json brackets: {} like this:
 "place any name here, this will be used to select your token when you start the bot" : "Your token here"
    * Example:
``` JSON 
{
 "John" : "5lnESOsUTRecipHaJU1epaDraFRadre4RLxldi",
 "Jack" : "QlnU2EspaTa4ocuplcResTUCho535Oc4LSpe6h"
}
```
2. Add to whitelist.json
    * If you want to use any of the whitelisted commands you will need to add your user id and server id to each appropriate section, these commands are volatile and are whitelisted for a reason.
    * These user and server ids should be placed in the square brackets: [] with commas in between each id
    * The users' whose ids are in the whitelist can use the whitelisted commands, and the servers' ids that are on the whitelist can have whitelisted commands used in them, **both need to apply for use**.
    * Example:
 ``` JSON
 {
  "users": [
      189338657417224217,
      438822908963068388
  ],
  "servers": [
      240274046286247816,
      992339590154758296
  ]
 }
 ```
3. Add songs to the music directory
    * Any songs added to the music directory manually must be mp3 and be in lowercase
4. View the Command List
    *  Use the .cl or .cls command
    * Or the .help command