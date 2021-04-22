import discord
from discord.ext import commands
import asyncio
import datetime

sent_users = []
class ModMail(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def modmail(self,ctx):
        sent_users = []
        modmail_channel = discord.utils.get(self.bot.get_all_channels(),guild__name = "Neural Networked",name = "shadow-mail")
        embed = discord.Embed(color = 0xEAD2A2)
        embed.set_author(name=f"Blackshadow's modmail", icon_url=self.bot.user.avatar_url)
        embed.add_field(name="__**Report a member:**__", value=f"React with 1️⃣ if you want to report a member",inline=False)
        embed.add_field(name="__**Warn appeal:**__", value=f"React with 2️⃣ If you would like to appeal for a warn",inline = False)
        embed.add_field(name="__**Queries:**__", value=f"React with 3️⃣ if you would like to ask any queries about the server",inline = False)
        embed.set_footer(text ="**Note:** `misusing the modmail will be counted as mute/kick`")
        message = await ctx.author.send(embed = embed)
        await message.add_reaction("1️⃣")
        await message.add_reaction("2️⃣")
        await message.add_reaction("3️⃣")
        sent_users.append(ctx.author.id)
        try:
            def check(reactions,user):
                return user == ctx.author and str(reactions) in ['1️⃣', '2️⃣', '3️⃣']
            reactions,user = await self.bot.wait_for("reaction_add",timeout = 20,check = check)
            if str(reactions.emoji) == "1️⃣":
                try:
                    embed = discord.Embed(color=0xEAD2A2)

def setup(bot):
    bot.add_cog(ModMail(bot))
