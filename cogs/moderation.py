import discord
from discord.ext import commands

class moderation(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_command_error(self,ctx, error):
        if isinstance(error, commands.CommandNotFound):
            embed = discord.Embed(  # Allows for the text to be embedded!
                colour=discord.Colour.blue()
            )
            embed.add_field(name='Error', value='The command you entered does not exist. Please type ?help for the full list', inline=True)

            await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount)

    @clear.error #Error message for the clear command being entered incorrectly
    async def clear_error(self, ctx, error):
        embed = discord.Embed(  # Allows for the text to be embedded!
            colour=discord.Colour.red()
        )
        embed.add_field(name='Error', value='Please enter an amount of messages to clear! Or you do not have the correct access!',inline=True)
        await ctx.send(embed=embed)


    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
      await member.kick(reason=reason)

    @kick.error #Error message for the kick command being entered incorrectly
    async def kick_error(self, ctx, error):
        embed = discord.Embed(  # Allows for the text to be embedded!
            colour=discord.Colour.red()
        )
        embed.add_field(name='Error', value='Please enter the user you want to kick! Or you do not have the correct access!',inline=True)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'Banned {member.mention}')

    @ban.error #Error message for the ban command being used incorrectly
    async def ban_error(self,ctx, error):
        embed = discord.Embed(  # Allows for the text to be embedded!
            colour=discord.Colour.red()
        )
        embed.add_field(name='Error', value='Please enter the user you want to ban! Or you do not have the correct access!',inline=True)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}')
                return

    @unban.error #error message for using the ban command incorrectly
    async def unban_error(self, ctx, error):
        embed = discord.Embed(  # Allows for the text to be embedded!
            colour=discord.Colour.red()
        )
        embed.add_field(name='Error', value='Please enter the user you want to unban! Or you do not have the correct access!',inline=True)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def mute(self, ctx, member : discord.Member=None):
        remrole = discord.utils.get(ctx.guild.roles, name='Members')
        role = discord.utils.get(ctx.guild.roles, name='Muted')
        if not member:
            await ctx.send("Please specify a user")
            return
        await member.add_roles(role)
        await member.remove_roles(remrole)
        await ctx.send('User has been muted!')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unmute(self, ctx, member : discord.Member=None):
        remrole = discord.utils.get(ctx.guild.roles, name='Muted')
        role = discord.utils.get(ctx.guild.roles, name='Members')
        if not member:
            await ctx.send("Please specify a user")
            return
        await member.remove_roles(remrole)
        await member.add_roles(role)
        await ctx.send('User has been unmuted!')


def setup(client):
    client.add_cog(moderation(client))
