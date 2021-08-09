"""
                 DOOM Bot
https://soundcloud.com/ojmacoj/experiment-doom
              Work in Progress
"""

import discord
from discord.ext import commands, tasks
from discord.utils import get
from discord import FFmpegPCMAudio
from itertools import cycle
import random
import os
import json
import youtube_dl


# Queries server_prefixes.json file for prefixes based on guild id
def get_prefix(bot, message):
    with open('server_prefixes.json', 'r') as f:
        prefixes = json.load(f)
    return prefixes[str(message.guild.id)]


# Uses prefix gathered from server_prefixes.json
bot = commands.Bot(command_prefix=get_prefix)
# Activity cycle randomly chosen on bot run
Drebin = ['Eye', 'Have', 'You']
Nano = ['Nanomachines', 'Son']
choice = [Drebin, Nano]
game_activity = cycle(random.choice(choice))
# status = cycle(['online', 'idle', 'invisible'])


queues = {}
queue_list = {}
currently_play = {}


def check_queue(ctx, id, song):
    try:
        if queues[id]:
            voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
            source = queues[id].pop(0)
            player = voice.play(source, after=lambda x=None: (
            check_queue(ctx, ctx.message.guild.id, song=song), new_currently_playing(ctx.message.guild.id),
            print(f'{song} has finished playing')))
    except KeyError:
        return KeyError

    try:
        if queue_list[id] != []:
            queue_list[id].pop(0)
    except KeyError:
        return KeyError


def new_currently_playing(id):
    if currently_play[id] is not []:
        currently_play[id].pop(0)
    else:
        return


@bot.event
# starts activity and status cycle and displays ready message when ready
async def on_ready():
    change_activity.start()
    #   change_status.start()
    print('---------------------------------------')
    print(f"Bot signed in with {t_choice}'s token")
    print('---------------------------------------')
    print('Bot is ready')
    print('---------------------------------------\n')


@bot.event
# Adds new server to server_prefixes.json on join
async def on_guild_join(ctx, guild):
    # Opens server server_prefixes.json
    with open('server_prefixes.json', 'r') as f:
        prefixes = json.load(f)
    # Adds new server to json and makes prefix .
    prefixes[str(guild.id)] = '.'
    with open('server_prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=5)
    with open('INTRO.txt', 'r') as doom:
        DOOM = '\n'.join(doom.readlines())
        await ctx.send(f'> {DOOM.center(1)}')


@bot.event
async def on_command_error(ctx, error):
    print(error)
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('That is not a command')


@tasks.loop(seconds=3)
# Loops activity cycle
async def change_activity():
    await bot.change_presence(activity=discord.Game(next(game_activity)))


# @tasks.loop(seconds=2.5)
# async def change_status():
#    await bot.change_presence(status=discord.Status(next(status)))


@bot.command(aliases=['cpre'], help='Changes the server\'s command prefix', brief='Change server\'s command prefix')
@commands.has_permissions()
# Changes prefix for bot in server
async def change_prefix(ctx, prefix):
    # Loads server_prefixes.json
    with open('server_prefixes.json', 'r') as f:
        prefixes = json.load(f)
    # Changes prefix in json based on guild id
    prefixes[str(ctx.guild.id)] = prefix
    with open('server_prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=5)
    await ctx.send(f'Changed prefix for server {ctx.guild.name} to: {prefix}')
    print(f'Changed the prefix for server {ctx.guild.name} to: {prefix}')


@bot.command(aliases=['ctc'], help='Creates specified Text Channel', brief='Create Text Channel')
@commands.has_permissions(administrator=True)
# Creates Text Channel
async def create_tc(ctx, *, name):
    # Creates Text Channel with name from argument name
    await ctx.guild.create_text_channel(name=name)
    print(f'Created voice channel: {name}')


@bot.command(aliases=['dtc'], help='Deletes specified Text Channel', brief='Delete Text Channel')
@commands.has_permissions(administrator=True)
# Deletes Text Channel that message is in
async def delete_tc(ctx):
    # Deletes based on message location
    await ctx.channel.delete()
    print(f'{ctx.author} deleted channel {ctx.channel.name} in {ctx.guild.name}')


# Must be able to input multiple arguments for role and name
@bot.command(aliases=['ctc_s'], help='Does not work', brief='Does not work')
@commands.has_permissions(administrator=True)
# Creates a secret channel
async def create_tc_secret(ctx, *, name, role: discord.role = None):
    chosen_role = get(ctx.guild.roles, name=role)
    if role is None:
        overwrite = {
            ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
            ctx.author: discord.PermissionOverwrite(read_messages=True)

        }
        await ctx.guild.create_text_channel(name=name, overwrites=overwrite)
    if role is not None:
        overwrite = {
            ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
            ctx.guild.author: discord.PermissionOverwrite(read_messages=True),
            chosen_role: discord.PermissionOverwrite(read_messages=True)
        }
        await ctx.guild.create_text_channel(name=name, overwrites=overwrite)
    print(f'Create secret text channel {name} for the {role} role')


@bot.command(aliases=['cvc'], help='Creates specified Voice Channel', brief='Create Voice Channel')
@commands.has_permissions()
# Creates Voice Channel
async def create_vc(ctx, *, name):
    # Creates Voice Channel with name based on argument name
    await ctx.guild.create_voice_channel(name=name)
    print(f'Created voice channel {name}')


@bot.command(aliases=['dvc'], help='Delete specified Voice Channel', brief='Delete Voice Channel')
@commands.has_permissions()
# Deletes Voice Channel author is in
async def delete_vc(ctx, *, name):
    # Retrieves channel
    channel = discord.utils.get(ctx.guild.channels, name=name)
    # Deletes channel if that channel exists, informs the user if it does not
    if channel is not None:
        await channel.delete()
        print(f'{ctx.author.name} deleted a voice channel named {name}')
    else:
        await ctx.sent(f'{name} is not a channel that can be deleted')


@bot.command(aliases=['test'], help='Test command for input', brief='Test for input')
# Bot test
async def input_test(ctx):
    # When command used, outputs
    await ctx.send('Received input')
    print('input received')


@bot.command(aliases=['return'], help='Test command for returning input', brief='Returns input for test')
# Echos input
async def return_input(ctx, *, user_input):
    # Outputs user input based on argument user_input
    await ctx.send(f'You said {user_input}')
    print("Returned input")


@bot.command(aliases=['ca'], help='Clears all messages in the current channgel up to the buffer', brief='Clears all messages in current channel')
@commands.has_permissions()
# Clears all text in a given channel
async def clear_all(ctx):
    # Checks to seee if message author is whitelisted
    with open('whitelist.json') as f:
        data = json.load(f)
        if ctx.author.id not in data['users']:
            # await command not useful in practice / production environment
            await ctx.send(f'{ctx.author} cannot use wipe command')
            print(f'{ctx.author} does not have permission for wipe command')
        if ctx.guild.id not in data['servers']:
            # await command not useful in practice / production environment
            await ctx.send(f'Wipe command is not allowed to be used in {ctx.guild.name}')
            print(f'Wipe command is not allowed to be used in {ctx.guild.name}')
        if ctx.author.id in data['users'] and ctx.guild.id in data['servers']:
            # Purges all
            await ctx.channel.purge()
            print(f'{ctx.author} removed all messages on {ctx.channel.name} in {ctx.guild.name}')
            print('Removed all messages')


@bot.command(help='Clears specified amount of messages', brief='Clears specified messages')
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=1):
    await ctx.channel.purge(limit=amount + 1)
    print(f'{ctx.author} removed {amount} messages')


@bot.command(help='Kicks specified member', brief='Kicks member')
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'Kicked {member.mention}')
    print(f'Kicked {member}')


@bot.command(help='Bans specified member', brief='Bans member')
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Kicked {member.mention}')
    print(f'Banned {member}')


@bot.command()
async def wipe(ctx, *, reason=None):
    with open('whitelist.json') as f:
        data = json.load(f)
        # if ctx.author.id not in data['users'] or ctx.guild.id not in data['servers']:
        if ctx.author.id not in data['users']:
            # await command not useful in practice / production environment
            await ctx.send('User cannot use wipe command')
            print(f'{ctx.author} does not have permission for wipe command')
        if ctx.guild.id not in data['servers']:
            # await command not useful in practice / production environment
            await ctx.send(f'Wipe command is not allowed to be used in {ctx.guild.name}')
            print(f'Wipe command is not allowed to be used in {ctx.guild.name}')
            # await command not useful in practice / production environment
            # await ctx.send('Invalid Permissions')
            # print(f'{ctx.author} does not have permissions to use wipe command in {ctx.guild.name}')
        if ctx.author.id in data['users'] and ctx.guild.id in data['servers']:
            for member in ctx.guild.members:
                await ctx.guild.ban(member, reason=reason)
                print('Banned all members')
                print(f'Members banned {member}')


@bot.command()
@commands.has_permissions(administrator=True)
async def k_wipe(ctx, *, reason=None):
    with open('whitelist.json') as f:
        data = json.load(f)
        if ctx.author.id not in data['users']:
            # await command not useful in practice / production environment
            await ctx.send('User cannot use wipe command')
            print(f'{ctx.author} does not have permission for wipe command')
        if ctx.guild.id not in data['servers']:
            # await command not useful in practice / production environment
            await ctx.send(f'Wipe command is not allowed to be used in {ctx.guild.name}')
            print(f'Wipe command is not allowed to be used in {ctx.guild.name}')
        if ctx.author.id in data['users'] and ctx.guild.id in data['servers']:
            for member in ctx.guild.members:
                await ctx.guild.kick(member, reason=reason)
                print('Kick wiping all members')
                print(f'Kicked these members {member}')


@bot.command()
@commands.has_permissions(administrator=True)
async def c_wipe(ctx):
    with open('whitelist.json') as f:
        data = json.load(f)
        if ctx.author.id not in data['users']:
            # await command not useful in practice / production environment
            await ctx.send('User cannot use wipe command')
            print(f'{ctx.author} does not have permission for wipe command')
        if ctx.guild.id not in data['servers']:
            # await command not useful in practice / production environment
            await ctx.send(f'Wipe command is not allowed to be used in {ctx.guild.name}')
            print(f'Wipe command is not allowed to be used in {ctx.guild.name}')
        if ctx.author.id in data['users'] and ctx.guild.id in data['servers']:
            for channels in ctx.guild.channels:
                await channels.channel.delete()
                print('Wiping all channels')
                print(f'Wiped these channels {channels}')


@bot.command()
@commands.has_permissions(administrator=True)
async def cog_load(ctx, *, extension):
    bot.load_extension(f'Cogs.{extension}')
    await ctx.send(f'Loaded extension: {extension}')
    print(f'Loaded extension: {extension}')


@bot.command()
@commands.has_permissions(administrator=True)
async def cog_load_all(ctx):
    for filename in os.listdir('Cogs'):
        if filename.endswith('.py'):
            bot.load_extension(f'Cogs.{filename[:-3]}')
            await ctx.send(f'Loaded all extensions')
    print('Loaded all extensions')


@bot.command()
@commands.has_permissions(administrator=True)
async def cog_unload(ctx, *, extension):
    bot.unload_extension(f'Cogs.{extension}')
    await ctx.send(f'Unloaded extension: {extension}')
    print(f'Unloaded extension: {extension}')


@bot.command()
@commands.has_permissions(administrator=True)
async def cog_unload_all(ctx):
    for filename in os.listdir('Cogs'):
        if filename.endswith('.py'):
            bot.unload_extension(f'Cogs.{filename[:-3]}')
            await ctx.send(f'Unloaded all extensions')
            print(f'Unloaded all extensions')


@bot.command(help='Unbans specified member', brief='Unbans member')
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')
    for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return print(f'Unbanned {user}')


@bot.command(pass_context=True, aliases=['j'], help='Tells the bot to join the author\'s voice channel', brief='Bot joins author\'s voice channel')
# Joins voice channel of message author
async def join(ctx):
    # if and else statement checks if message author is in a voice channel, and responds if they are not
    if ctx.author.voice:
        # Use the message author's voice channel location to join voice channel
        channel = ctx.author.voice.channel
        await channel.connect()
        print(f'{ctx.author.name} asked the bot to join {ctx.message.guild}\'s {ctx.author.voice.channel}')
    else:
        await ctx.send('You must be in a voice channel for me to join')


@bot.command(pass_context=True, aliases=['l'], help='Tells the bot to leave the voice channel', brief='Bot leaves the voice channel')
# Leave current voice channel if in one
async def leave(ctx):
    # Use bot's voice client status to determine disconnect or error
    if ctx.voice_client:
        await ctx.guild.voice_client.disconnect()
        print(f'{ctx.author.name} asked the bot to leave {ctx.message.guild}\'s {ctx.author.voice.channel}')
    else:
        await ctx.send('I am not in a voice channel')


@bot.command(aliases=['p'], help='Plays a specified song from the local library', brief='Plays specified song')
# Plays songs from the locally downloaded library with ffmpeg
async def play(ctx, *, song=''):
    song = song.lower()
    guild_id = ctx.message.guild.id
    global voice

    # If statements to check if bot is already in a voice channel and if message author is in a voice channel to join
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    try:
        if voice.is_paused():
            print(f'{ctx.author} resumed the bot in {ctx.guild}')
            return voice.resume()
    except:
        print('Ignore: not paused')
    if not ctx.author.voice:
        await ctx.send('You need to be in a voice channel for me to join')
        return
    else:
        try:
            channel = ctx.message.author.voice.channel
            voice = await channel.connect()
        except discord.ClientException:
            print('Ignore: Already in Voice Channel')
            pass

        # Uses list to check for available songs and cross-references them with song given
        song_list = []
        for file in os.listdir('Music/'):
            if file.endswith('.mp3'):
                song_list.append(file[:-4])

        if song in song_list:

            if not voice.is_playing():
                if guild_id in currently_play:
                    currently_play[guild_id].append(song)
                else:
                    currently_play[guild_id] = [song]

            source = FFmpegPCMAudio(f'Music/{song}.mp3')

            if voice.is_playing():
                return await queue(ctx, name=song)
            player = voice.play(source, after=lambda x=None: (check_queue(ctx, ctx.message.guild.id, song=song), new_currently_playing(ctx.message.guild.id),
            print(f'{song} has finished playing')))
            await ctx.send(f'**Playing {song}** from the local library')
            print(f'{ctx.author.name} has played {song} from the local library in {ctx.message.guild.name}')

        else:
            await ctx.send(f'**{song} is not in the local library**')
            print(f'{song} is not in the local library: from {ctx.message.guild.name}')



@play.error
async def clear_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('You must include the song name')
    if isinstance(error, discord.ClientException):
        print('If in Play command: Try and except not working, supposed to pass this issue')
        pass


@bot.command(aliases=['d'], help='Downloads a song based on youtube url', brief='Downloads song based on url')
# Downloads and plays music with youtube_dl and ffmpeg
async def download(ctx, url: str, *, name):
    #    global voice
    name = name.lower()
    if name == '/' or name == '\\':
        return await ctx.send('**Name cannot include / or \\**')
    #    guild_id = ctx.message.guild.id
    # Config for youtube_dl
    ydl_opts = {
        'format': 'bestaudio',
        'noplaylist': 'True',
        # Names downloaded files as argument provided
        'outtmpl': f'Music/{name}.mp3',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    # Downloads video by url to local library then plays it based on the name argument
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        await ctx.send(f'Downloading **{name}** from youtube to local library')
        print(f'{ctx.author} is downloading {name} from {url}')
        ydl.download([url])
        await ctx.send(f'**{name}** has been downloaded to the local library')
        print(f'{ctx.author} downloaded {name} from {url}')
    # Given Timeout Error after download so the play after download was removed.


#    # Plays downloaded file based on name argument
#    song_list = []
#    for file in os.listdir('Music/'):
#        if file.endswith('.mp3'):
#            song_list.append(file[:-4])
#    if name in song_list:
#        if guild_id in currently_play:
#            currently_play[guild_id].append(name)
#        else:
#            currently_play[guild_id] = [name]
#        # Checks if bot and author is in voice channel and outputs accordingly
#        if not bot.voice_clients:
#            if ctx.author.voice:
#                channel = ctx.author.voice.channel
#                voice = await channel.connect()
#            else:
#                await ctx.send('You need to be in a voice channel for me to join')
#        source = FFmpegPCMAudio(f'Music/{name}.mp3')
#        if voice.is_playing():
#            return await queue(ctx, name=name)
#        else:
#            player = voice.play(source, after=lambda x=None: check_queue(ctx, ctx.message.guild.id))
#            await ctx.send(f'Playing {name}')
#            print(f'{ctx.author.name} is playing {name}')
#    else:
#        await ctx.send(f'{name} is not in the local library')
#        print(f'{name} is not in the local library')


@bot.command(aliases=['sch'], administrator=True, help='Takes the top search from youtube and outputs consist of, title, length, and the url, which can be put in the download command', brief='Search youtube based on keywords')
# This needs to be able to search up videos on youtube and then download them, or be used to output a url for other functions to call on
async def search(ctx, *, terms):
    ydl_opts = {
        'format': 'bestaudio', 'noplaylist': "True"
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            video = ydl.extract_info(f"ytsearch1:{terms}", download=False)['entries'][0]
        except:
            video = ydl.extract_info(terms, download=False)
    duration = int(video['duration']) / 60
    url = video['url']
    title = video['title']
    print(video)
    print(video['url'])
    print(video['duration'] / 60)
    print(video['title'])
    await ctx.message.channel.send(f'**Title**: {title}')
    await ctx.message.channel.send(f'**Duration**: {str(duration)}')
    await ctx.message.channel.send(f'**Url**: {url}')


@bot.command(aliases=['list_ls', 'lls'], help='List local songs in the music directory', brief='List songs')
# Lists all the local mp3 files that can be played with play_local
async def list_local_songs(ctx):
    # Moves through current directory of the script to search for files ending with .mp3
    song_list = []
    for file in os.listdir('Music/'):
        if file.endswith('.mp3'):
            # Outputs in current text channel all the songs found with .mp3 at the end through for and if statements
            song_list.append(file[:-4])
    await ctx.send('**------------ Start of Library --------------**')
    for song in song_list:
        await ctx.send(song)
    await ctx.send('**------------- End of Library ---------------**')
    print(f'{ctx.author.name} has listed songs in the local library')


@bot.command(aliases=['dls'], help='Delete local songs from the music directory', brief='Delete songs')
# Deletes a song from the local library
async def delete_local_song(ctx, *, name):
    # Checks if message author is one of the users that can use command
    with open('whitelist.json') as f:
        data = json.load(f)
        if ctx.author.id in data['users']:
            # Removes file from the argument name
            try:
                os.remove(f'Music/{name}.mp3')
                print(f'{ctx.author.name} has deleted {name} from the local library')
                await ctx.send(f'**Removed** {name} from the local library')
            # Outputs text if file cannot be found
            except FileNotFoundError:
                await ctx.send('This is not a proper filename in the library')
        else:
            # Outputs if author is not whitelisted for this command
            await ctx.send('You are not allowed to delete songs')
            print(f'{ctx.author.name} is not allowed to delete songs from the local library')


# This needs to be able to have multiple inputs for the multiple args, to rename a mp3 file in the music directory
@bot.command(help='Renames a song in the music directory, command must be formatted like: old name, new name', brief='Renames a song, format like: old name, new name')
async def rename(ctx, *args):
    pre = ''
    for word in args:
        pre += word + ' '
    str = pre.split(', ')
    if len(str) != 2:
        return await ctx.send(f'Invalid arguments: {get_prefix(bot, ctx.message)}rename old name, new name')
    name = str[0]
    new = str[1][0:-1]
    os.rename(f'Music/{name}.mp3', f'Music/{new}.mp3')
    await ctx.send(f'Changed {name} to {new}')
    print(f'{ctx.author.name} changed the name for {name} to {new}')


@bot.command(pass_context=True, aliases=['ps'], help='Pauses the bot from playing audio', brief='Pauses the bot')
async def pause(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
        await ctx.send('I paused')
        print(f'{ctx.author.name} paused the bot')
    else:
        await ctx.send('I am not playing anything at the moment')


@bot.command(pass_context=True, aliases=['r'], help='Resume the bot\'s audio', brief='Resume the bot')
async def resume(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
        await ctx.send('I resumed')
        print(f'{ctx.author.name} resumed the bot')
    else:
        await ctx.send('I am not paused at the moment')


@bot.command(pass_context=True, aliases=['s'], help='Stop the bot from playing audio', brief='Stop the bot\'s audio')
async def stop(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if bot.voice_clients:
        voice.stop()
        queues.clear()
        queue_list.clear()
        currently_play.clear()
        await ctx.send('I stopped playing')
        print(f'{ctx.author.name} stopped music from the bot')
    if not bot.voice_clients:
        await ctx.send('I am not in a voice channel')


@bot.command(pass_context=True, aliases=['sp'], help='Skips the bot\'s current audio', brief='Skip current audio')
async def skip(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if bot.voice_clients:
        voice.stop()
        await ctx.send('I skipped the current song')
        print(f'{ctx.author.name} skipped the current song')
    else:
        await ctx.send('I am not in a voice channel')


@bot.command(pass_context=True, aliases=['q'], help='Queues a specified song', brief='Queues a song')
async def queue(ctx, *, name):
    try:
        source = FFmpegPCMAudio(f'Music/{name}.mp3')
    except:
        return await ctx.send(f'**{name}** is **not** a song')

    guild_id = ctx.message.guild.id

    if guild_id in queues:
        queues[guild_id].append(source)
    else:
        queues[guild_id] = [source]

    if guild_id in queue_list:
        queue_list[guild_id].append(name)
    else:
        queue_list[guild_id] = [name]

    if guild_id in currently_play:
        currently_play[guild_id].append(name)
    else:
        currently_play[guild_id] = [name]
    await ctx.send(f'**Added {name}** to queue')
    print(f'{ctx.author.name} added {name} to the queue')


@bot.command(aliases=['dq'], help='Displays the songs in the queue', brief='Displays the queue')
async def display_queue(ctx):
    try:
        if queue_list[ctx.message.guild.id] is []:
            await ctx.send('The queue is empty')
        else:
            song_list = []
            for songs in queue_list[ctx.message.guild.id]:
                song_list.append(songs)
            if song_list == []:
                await ctx.send('No Songs in Queue')
            else:
                await ctx.send('**---------- Current Songs in Queue ----------**')
                for song in song_list:
                    await ctx.send(song)
                await ctx.send('**--------------- End of Queue -----------------**')
    except KeyError:
        await ctx.send('**The queue is empty**')


@bot.command(aliases=['cp'], help='Displays the currently playing song', brief='Displays currently playing song')
async def currently_playing(ctx):
    guild_id = ctx.message.guild.id
    if currently_play[guild_id] is not []:
        await ctx.send(f'**{currently_play[guild_id][0]} is playing**')
        print(f'{ctx.author} asked what was currently playing: {currently_play[guild_id][0]}')


@currently_playing.error
async def clear_error(ctx, error):
    print(error)
    if isinstance(error, commands.CommandInvokeError):
        await ctx.send('There is nothing playing')


@bot.command(aliases=['flip', 'fc'], brief='Flip a coin?')
async def flip_coin(ctx):
    coin = ['Heads', 'Tails']
    flip = random.choice(coin)
    await ctx.send(flip)
    print(f'{ctx.author} flipped a coin with a result of {flip}')


@bot.command(brief='Slap someone')
async def slap(ctx, member: discord.Member, *, reason=None):
    if reason is not None:
        await ctx.send(f'{ctx.author.mention} slapped {member.mention} for {reason}')
        print(f'{ctx.author.mention} slapped {member.mention} for {reason}')
    else:
        await ctx.send(f'{ctx.author.mention} slapped {member.mention}')
        print(f'{ctx.author.mention} slapped {member.mention}')


@bot.command(aliases=['8ball'], brief='Consult the 8ball')
async def _8ball(ctx, *, question):
    positive = ['It is certain',
                'Without a doubt',
                'You may rely on it',
                'Yes definitely',
                'It is decidedly so',
                'As I see it, yes',
                'Most likely',
                'Yes',
                'Outlook good',
                'Signs point to yes',
    ]
    neutral = [
        'Reply hazy try again',
        'Ask again later',
        'Cannot predict now',
    ]
    negative = [
        'Better not tell you now',
        'Concentrate and ask again',
        'Don’t count on it',
        'Outlook not so good',
        'My sources say no',
        'Very doubtful',
        'My reply is no',
    ]
    response = random.choice([positive, neutral, negative])
    answer = random.choice(response)
    await ctx.send(f'Your question was: {question}')
    await ctx.send(f'Answer: {answer}')
    print(f'{ctx.author} asked 8ball: **{question}** and was answered with with: **{answer}**')


@bot.command(brief='Ping the bot\'s server')
async def ping(ctx):
    await ctx.send(f'Pong, {round(bot.latency * 1000)}ms')
    print(f'Responded to bot latency request of {round(bot.latency * 1000)}ms')


#@bot.command(aliases=['cl'])
# Displays all commands
#async def command_list(ctx):
#    with open('commands.txt', 'rb') as commands:
#        await ctx.author.send(file=discord.File(commands, 'commands.txt'))
#        print(f'{ctx.author} asked for a command list')


#@bot.command(aliases=['cls'])
#async def command_list_short(ctx):
#    with open('commands_short.txt', 'rb') as commands:
#        await ctx.author.send(file=discord.File(commands, 'commands_short.txt'))
#        print(f'{ctx.author} asked for a short command')


@bot.command(brief='Displays the intro text')
async def intro(ctx):
    with open('INTRO.txt', 'r') as doom:
        DOOM = '\n'.join(doom.readlines())
        await ctx.send(f'> {DOOM.center(1)}')


# @bot.command()
# async def ping_me(ctx):
#    await ctx.send(f'Pong, {round(ctx.author.latency * 1000)}ms')
#    print(f'Responded to author latency request of {round(ctx.author.latency * 1000)}ms')


# Provides prompt before bot run, for token to be used, and forces while loop until correct answer
with open('bot_start', 'r') as file:
    DOOM = file.read()
    print(DOOM)
text = 'Discord Bot'
final_text = text.center(61, '=')
print(f'{final_text}')
another_text = 'An Animated House Musical'
extra_text = another_text.center(61,'=')
print(f'{extra_text}\n')
print('---------------------------------------')
t_choice = input('What token do you want to run? ')
with open('tokens.json', 'r') as file:
    tokens = json.load(file)
    correct_val = False
    while correct_val is False:
        try:
            bot.run(tokens[t_choice])
            correct_val = True
        except KeyError:
            print('!!Not valid input!!')
            t_choice = input('What token do you want to run? ')