# Doom - Bot
**A mulit-purpose discord bot, built to be hosted locally.**

I'm not sure what to put in here or whether what I'm going to write is the correct way to state these ideas, any help would be appreciated:
***


# Prologue
Please use this bot as you like, at the moment it is built to be hosted locally. But it is still a work in progress, so I would enjoy it if you provided some feedback and contributed a little. I am not sure what license to use, so I am going with GPLv2. I have not tested this version posted, on Windows yet, although I used previous versions on Windows. But this does not mean it works, any help with this would be appreciated.

# Windows Prerequisites
 * Install the latest version of Python (As of August 14th, 2021 it is 3.9) through the Windows Store(This is recommended), or the [Python website](https://www.python.org/downloads/), and ffmpeg can be installed with these steps or by following [this video](https://youtu.be/M_6_GbDc39Q?t=129):
1.  Download ffmpeg from [here](https://github.com/BtbN/FFmpeg-Builds/releases/download/autobuild-2021-08-14-12-36/ffmpeg-n4.4-80-gbf87bdd3f6-win64-gpl-4.4.zip)

2. Extract this to somewhere and make sure it won't be deleted and **copy the path of the ffmpeg exes** in the bin directory of the ffmpeg extract.

3. Type the word **path** into the search bar on your desktop, or press the windows button on your keyboard and do the same. You will see **Edit environment variables**, open this.

4. A **System Properties** window will open, in the **Advanced tab** click on **Environment Variables** button towards the bottom of the window.

5. An **Environment Variables** window will open, under the **System Variables** section to the bottom of the window, scroll through this section until you see **Path**, double click this.

6. The **Edit environment variable** window will open, to the top right of the window there will be a button labelled **New**, click this and the paste the path of the ffmpeg exes you copied from earlier

7. You may test ffmeg by opening a command prompt(Type cmd into the windows search bar) and typing ffmpeg. If the first line reads the **ffmpeg version** then you have successfully installed ffmpeg.

* Libraries required, <span>discord.py<span>\[audio\], youtube_dl install with this command:
    * `pip install "discord.py[audio]" youtube_dl`

# Prerequisites on other platforms
* Must have the latest version of Python, and ffmpeg, these may be intalled with your OS's package manager.
* _Optional:_
    *  Create a virtual python environment, while in the same directory as the bot do these commands:
        * `python3 -m venv venv`
        * `source ./venv/bin/activate`

* Libraries required, <span>discord.py<span>\[audio\], youtube_dl install with this command:
    * `pip install 'discord.py[audio]' youtube_dl`

# Invite Bot to Server

You will need to invite the bot to your server before being able to run it:

1. Go to the [discord developer portal](https://discord.com/developers/applications) and sign in.

2. Then while in the **Applications Tab** click **New Application** in the top right of the window.

3. Name application whatever you'd like, preferably Doom(or a variation of it, as there are no similar names for apps), then click create.

4. Once in the application menu switch to the **Bot Tab** located on the left of the window.

5. Click the **Add Bot** button on the right of the window.

6. There will be a **Token** label copy this token with the correlated button labelled **Copy** and keep it temporarily, keep this safe as anyone can run code with your bot if they have it.

7. _Optional:_
    * You may customize the name and icon of the bot as you wish

8. Go to the **OAuth2 tab** on the left of the window.

9. In here you will see a **Scopes section** click the **bot** check box. 

10. Then a **Bot Premissions section** and click the **Adminstrator** check box (You may check specific boxes besides Administrator if you understand which are required and which aren't, but this may break the bot or some functionalities of it).

11. You will see under the **Scopes section** that there is a link generated, open this link and sign in with your discord, and add fill in the server that you would like the bot to be in, under the **Add to Server** tab. If the bot joins that server you have successfully added the bot and you use that token from earlier in the next **Setup** steps.

# Setup
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