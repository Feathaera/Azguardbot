import discord
from discord.ext import commands
import os  # for cog loading
import time
import asyncio
from itertools import cycle
import os
from datetime import datetime, timedelta
import random


client = commands.Bot(command_prefix="?")
client.remove_command('help')
Guild = object()



@client.event  # bot starting tells me it exists
async def on_ready():
    global starter, Guild
    print("Bot is online bb")

statusmsg = ['?help for commands list', 'Watching chat']


def botowner(ctx):  # Checks to see if you are the bots owner or not!
    return ctx.author.id == 167647885033209856



@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name='welcomes')
    await channel.send(f"Welcome {member.mention} Please follow the rules!")
    role = discord.utils.get(member.guild.roles, name='Members')
    await member.add_roles(role)


@client.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(title="Commands",
                          description="Here are all if the help commands available. Please be aware some will require permissions!",
                          color=0x29c2ef)
    embed.add_field(name="Ping", value="Returns the Latency of the bot", inline=True)
    embed.add_field(name="Changelog", value="Displays the bots updates and changes!", inline=True)
    embed.add_field(name="say", value="The bot will repeat the message after you!", inline=True)
    embed.add_field(name="stats", value="The bot will display the users information", inline=True)
    embed.add_field(name="===============================================", value=".", inline=False)
    embed.add_field(name="Clear", value="Will clear the amount of messages specified", inline=True)
    embed.add_field(name="Kick", value="Will kick the specified user", inline=True)
    embed.add_field(name="Ban", value="Will ban the requested member", inline=True)
    embed.add_field(name="Unban", value="Will Unban the specified user", inline=True)
    embed.add_field(name="Mute", value="Will mute the user to stop them speaking in the server", inline=True)
    embed.add_field(name="Unmute", value="Will unmute the user", inline=True)
    await ctx.send(embed=embed)



@client.command()
async def suggest(ctx):
    embed = discord.Embed(
        colour=discord.Colour.blue()
    )
    embed.add_field(name='Suggestion!', value='Please Message Daybreak#6666 for any suggestions you have to the bot!', inline=True)
    await ctx.send(embed=embed)


@client.command()  # Unloads a cog
@commands.check(botowner)
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    embed = discord.Embed(
        colour=discord.Colour.blue()
    )
    embed.add_field(name='Success!', value='You have successfully unloaded a cog', inline=True)
    await ctx.send(embed=embed)

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')



for filename in os.listdir('./cogs'):  # Allows the loading of cogs
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


async def change_status():  # Changes status
    await client.wait_until_ready()
    messages = cycle(statusmsg)

    while not client.is_closed():
        current_status = next(messages)
        await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game(name=current_status))
        await asyncio.sleep(300)  # change time




client.loop.create_task(change_status())
client.run(os.environ['token'])
