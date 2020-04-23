import discord
from discord.ext import commands
import sqlite3

class levels(commands.Cog):
    def __init__(self, client):
        self.client = client



def setup(client):
    client.add_cog(levels(client))
