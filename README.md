# Doom - Bot
**A mulit-purpose discord bot, built to be hosted locally.**

I'm not sure what to put in here or whether what I'm going to write is the correct way to state these ideas, any help would be appreciated:
***

# Prerequisites

* You will need the latest version **Python** and **Ffmpeg** and the python libraries **<span>discord.py<span> youtube_dl and PyNaCl**. You may install the python libraries with pip and the other programs with your platforms package manager.

* _Optional_:
    * You may create a virtual environment for this bot with these commands while in the same directory as the bot:
        * `python3 -m venv venv`
        * `source ./venv/bin/activate`

## Windows Prerequisites

* If on Windows, you may download the latest version of python from the Windows Store, or from the [Python website](https://www.python.org/downloads/), and ffmpeg can be installed and configured with the setup.<nolink>py script which will be require you to follow the Change Execution Policies section, or by following [this video](https://youtu.be/M_6_GbDc39Q?t=129) or follwing the Manual ffmpeg Installation section.

* Once you have installed python you should install the required python libraries with this command:
    * `pip install "discord.py[audio]" youtube_dl PyNaCl`

* _Optional_:
    * This can only be done if you have done the Change Execution Policies section:
        * You may create a virtual environment with these commands, while in the same directory as the bot:
            * `python3 -m venv venv`
            * `./venv/Scripts/activate`

### Change Execution Policies
1. Before starting the setup script you will need to change some script policies, to do this open a powershell as administrator then type `Get-ExecutionPolicy -List` you should remember and save these policies and change them back to normal in the future. For more information about this please visit this [Microsfot Docs Page](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.security/get-executionpolicy?view=powershell-7.1).

2.  In order to allow the setup script to run do this command  `Set-ExecutionPolicy -ExecutionPolicy Unrestricted`.

* **Please note that this can make your computer unsafe, it is recommended that you return it to normal once the setup is finished.**

### Manual ffmpeg Installation
1.  Download ffmpeg from [here](https://github.com/BtbN/FFmpeg-Builds/releases/download/autobuild-2021-08-14-12-36/ffmpeg-n4.4-80-gbf87bdd3f6-win64-gpl-4.4.zip)

2. Extract this to somewhere and make sure it won't be deleted and **copy the path of the ffmpeg exes** in the bin directory of the ffmpeg extract.

3. Type the word **path** into the search bar on your desktop, or press the windows button on your keyboard and do the same. You will see **Edit environment variables**, open this.

4. A **System Properties** window will open, in the **Advanced tab** click on **Environment Variables** button towards the bottom of the window.

5. An **Environment Variables** window will open, under the **System Variables** section to the bottom of the window, scroll through this section until you see **Path**, double click this.

6. The **Edit environment variable** window will open, to the top right of the window there will be a button labelled **New**, click this and the paste the path of the ffmpeg exes you copied from earlier

7. You may test ffmeg by opening a command prompt(Type cmd into the windows search bar) and try running the command ffmpeg. If the first line reads the **ffmpeg version** then you have successfully installed ffmpeg.

# Create the Bot

1. Go to the [discord developer portal](https://discord.com/developers/applications) and sign in.

2. Then while in the **Applications Tab** click **New Application** in the top right of the window.

3. Name application whatever you'd like, preferably Doom(or a variation of it, as there are no similar names for apps), then click create.

4. Once in the application menu switch to the **Bot Tab** located on the left of the window.

5. Click the **Add Bot** button on the right of the window.

6. There will be a **Token** label copy this token with the correlated button labelled **Copy** and keep it temporarily, keep this safe as anyone can run code with your bot if they have it.

7. _Optional:_
    * You may customize the name and icon of the bot as you wish

* Keep this tab open you will need to return to it later.

# Setup

* If you do not plan on using the Setup Script please move to the Manual Setup section.
* You may use the script labeled setup<nolink>.py inorder to configure all of the json files it will direct you through the process, you should use the token retrieved in step 6 of the Create the Bot section when asked "What is your token?". When asked about the whitelist, you may input server ids and user ids for the people and servers that you want whitelisted commands to be used in and by. **These commands are volitile and a whitelist are required for them for a reason**.

## Windows Setup

* To use the setup script you will need to run powershell as administrator and change to the directory of the bot, the run the command:
    * `python setup.py`
* The script will move you through the configuration process view the text at the top of the the Setup section for more information on this process.
    * Then at the end the script will ask you if you would like to download and configure ffmpeg, if you have not already done this please do, **However do note that you will have to have done the Change Execution Policies section**.
    * Once this is finished please close and open powershell again, then try to run the command ffmpeg, if there is no error and in the output you see a version read, you will have successfully installed ffmpeg.
* **Once the setup is complete it is recommended that you return your Execution Policies to normal**
    * If you saved your Execution Policies before changing them, then you should use `Set-ExecutionPolicy` along with the correct corresponding arguments `-Scope` and `-ExecutionPolicy` **in an administrator powershell**. For more information on this command please visit this [Microsoft Docs Page](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.security/set-executionpolicy?view=powershell-7.1).
    * If you do not remember your Execution Policies or they were all **Undefined**, then you may just do this command:
        * `Set-ExecutionPolicy -ExecutionPolicy Undefined`
        * Then give a prompt, choose all, by entering `A`

## Manual Setup
* In the case that you are unable or do not want to use the setup script you may follow these steps to manually configure your json files.
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

# Invite Bot to Server

You will need to make sure that the **bot is running when it joins the server**:

1. Return to the [discord developer portal](https://discord.com/developers/applications).

2. Go to the **OAuth2 tab** on the left of the window.

3. In here you will see a **Scopes section** click the **bot** check box. 

4. Then a **Bot Premissions section** and click the **Adminstrator** check box (You may check specific boxes besides Administrator if you understand which are required and which aren't, but this may break the bot or some functionalities of it).

5. You will see under the **Scopes section** that there is a link generated, open this link and sign in with your discord, and add fill in the server that you would like the bot to be in, under the **Add to Server** tab. If the bot joins that server you have successfully added the bot and you use that token from earlier in the next **Setup** steps.

6. **Congrats your bot has been setup, if there are any issues please submit a ticket on the Github**

***

## Extra Notes

* You may add songs manually to the `Music` directory, however any songs added to the music directory manually **must be mp3 and names be in lowercase**.
* In Windows if you encounter any issues with ffmpeg in powershell, or the command is not recognized, make sure your Windows is up to date and try restarting Windows. If neither fix the issue please submit a ticket in the github, and attempt to follow the Manual ffmpeg Installation section along with the [video provided](https://youtu.be/M_6_GbDc39Q?t=129).