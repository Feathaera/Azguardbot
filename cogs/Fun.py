import discord
from discord.ext import commands
import datetime

class fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        embed = discord.Embed(title="Pong!", description="You ran the ping command!", color=0xbe4dfb)
        await ctx.send(embed=embed)

    @commands.command()
    async def say(self, ctx, *args):
        message = ' '.join(args)
        if message == "@Everyone":
            await ctx.send("I will not mention everyone")
        elif message == "@here":
            await ctx.send("I will not mention everyone!")
        else:
            await ctx.channel.purge(limit=1)
            await ctx.send(message)



    @commands.command()
    async def changelog(self, ctx):
        embed = discord.Embed(title="Changelog", description="This displays the newest changes to the bot!",
                              color=0xf92828)
        embed.add_field(name="Version 1.2",value="Added the users stats command",inline=False)
        embed.add_field(name="Version 1.1", value="Changed permissions to ensure that certain commands are locked behind permissions", inline=False)
        embed.add_field(name="Version 1.0",
                        value="Base release of the bot!",
                        inline=True)
        await ctx.send(embed=embed)

    @commands.command()
    async def stats(self, ctx, member: discord.Member):
        roles = [role for role in member.roles]

        embed = discord.Embed(color=member.color, timestamp=datetime.datetime.utcnow())

        embed.set_author(name=f"{member}", icon_url=member.avatar_url)

        embed.set_image(url=member.avatar_url)

        embed.add_field(name="Joined at:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

        embed.add_field(name=f"Roles ({len(roles)})", value=" ".join([role.mention for role in roles]))

        embed.add_field(name="Top role:", value=member.top_role.mention)

        embed.add_field(name="Bot?", value=member.bot)
        embed.set_footer(text=f"Requested By: {ctx.author.name}")

        await ctx.send(embed=embed)



def setup(client):
    client.add_cog(fun(client))
