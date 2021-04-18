import discord
from discord.ext import commands
import asyncio

class Utility(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command()
    async def code_help(self,ctx,desc = None , rep = None):
        user = ctx.author
        await ctx.author.send("`Explain about your bug/error`")
        response_desc = await self.bot.wait_for("message",check = lambda message:message.author == ctx.author , timeout = 300)
        description = response_desc.content
        await ctx.author.send("`Provide more information about the bug/error by providing a reference link`")
        response_Rep = await self.bot.wait_for("message",check = lambda message: message.author == ctx.author , timeout = 300)
        replicate = response_Rep.content
        embed = discord.Embed(title = "__**Report**__",color = discord.Color.blue())
        embed.add_field(name = "**Description**",value = description,inline = False)
        embed.add_field(name = "**Reference**",value = replicate,inline = True)
        embed.add_field(name = "**Reported by**",value = user , inline = True)
        await ctx.send(embed=embed)
        reactions = ['❎', '✔️', '‼️']
        for reaction in reactions:
            await ctx.message.add_reaction(reaction)
        def check(reaction,user):
            return user == ctx.author and str(reaction.emoji) in reactions
        try:
            reaction,user = await self.bot.wait_for("reaction_add",timeout = 30 , check = check)
            if reaction.emoji == "❎":
                em = discord.Embed(title = "**__Failed__**",color = discord.Color.red())
                em.add_field(name = "**Not enough details**",value = "`Please provide with more information`",inline = False)
                await ctx.author.send(embed=em)
                await ctx.send("Information not provided or help not served")
            elif reaction.emoji == "✔️":
                em = discord.Embed(title = "**__Success__**",color = discord.Color.green())
                em.add_field(name = "**Thank you**",value = "`help provided thank you for choosing me`",inline = False)
                await ctx.author.send(embed=em)
                await ctx.send("Help provided")
            elif reaction.emoji == "‼️":
                em = discord.Embed(title = "**__Failed__**",color = discord.Color.red())
                em.add_field(name = "**Error solved**",value = "`seems like the help has been already provided`",inline = False)
                await ctx.author.send(embed=em)
                await ctx.send("Help already provided or No help needed")
        except:
            await ctx.send("Try again")



def setup(bot):
    bot.add_cog(Utility(bot))
