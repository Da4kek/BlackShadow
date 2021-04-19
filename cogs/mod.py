import discord
from discord.ext import commands
import os 
from discord.ext.commands import has_permissions, MissingPermissions

class Moderation(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.has_permissions(kick_members = True)
    @commands.command(name="kick",aliases=['k'])
    async def kick(self , ctx ,user:discord.Member,*,reason=None):
        if reason == None:
            reason = "No reason given"
        await user.kick(reason = reason)
        await user.send(f"Hey You have been kicked from **{user.guild.name}** for the reason `{reason}`")
        em = discord.Embed(title=f"Kicked",description = f"user: {user.mention} has been kicked :raised_back_of_hand:")
        em.add_field(name="Reason" , value = reason)
        em.set_author(name = ctx.author.display_name,icon_url=ctx.author.avatar_url)
        await ctx.send(embed = em)
        
            
    @commands.has_permissions(ban_members = True)
    @commands.command(name = "ban",aliases = ['b'])
    async def ban(self, ctx , user: discord.Member,*,reason = None):
        if reason == None:
            reason = "No reason given"
        await user.ban(reason = reason)
        await user.send(f"Hey You have been banned from **{user.guild.name}** for the reason `{reason}`")
        em = discord.Embed(
            title=f"Banned", description=f"user: {user.mention} has been banned :hammer:")
        em.add_field(name = "Reason",value = reason)
        em.set_author(name = ctx.author.display_name,icon_url=ctx.author.avatar_url)
        await ctx.send(embed = em)
    
    @commands.is_owner()
    @commands.command(name = "mass kick",aliases = ['mk','masskick'])
    async def mass_kick(self,ctx,user:discord.Member = [],*,reason = None):
        if reason == None:
            reason = "Indefinite"
        for i in user:
            await i.kick(reason = reason)
        await ctx.send(f"users: {user} have been kicked! with the reason of {reason}")
        

def setup(bot):
    bot.add_cog(Moderation(bot))
