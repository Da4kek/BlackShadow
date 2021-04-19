import discord
from discord.ext import commands
import random
import datetime
date = datetime.datetime.now()
version = "V-0.02"
class Info(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(aliases = ['stats','botinfo'])
    async def info(self,ctx):
        em = discord.Embed(title =f"__**Stats**__",color = random.randint(0,0xFFFFF))
        em.set_thumbnail(url = ctx.guild.me.avatar_url)
        em.add_field(name=f":small_blue_diamond: | **__Version:__**",
                     value=f"[`{version}`]", inline=False)
        em.add_field(name=f":books: | **__Library:__**",
                 value=f"[`discord.py`]", inline=False)
        em.add_field(name=f":keyboard: | **__Creator(s):__**",
                     value=f"`The-DarK-os  # 7290`\n`LegendLife101#5795`\n`MysT#9105`", inline=False)
        em.add_field(name=f":busts_in_silhouette: | **__Servers & Users:__**",
                    value=f"Total Servers: [`{len(self.bot.guilds)}`]\nTotal Users: [`{len(set(self.bot.get_all_members()))}`]", inline=False)
        em.add_field(name=":question: | **__Prefix:__**",
                    value=f"Default: [`-`]\nServer: [`{ctx.prefix}`]", inline=False)
        em.add_field(name=":bar_chart: | **__Ping:__**",value=f"Ping: [`{round(self.bot.latency * 1000)}`]", inline=False)
        em.add_field(name="__**Support Server**__", value="[Programmer's guild](https://discord.gg/hQywcDjZUT)", inline=False)
        em.add_field(name="__**Invite me**__", value="[to your server](https://discord.com/api/oauth2/authorize?client_id=796735541101854740&permissions=8&scope=bot)",inline=False)
        em.set_footer(text=f"Today at {date:%I}:{date:%M} {date:%p}.")
        await ctx.reply(embed = em)

def setup(bot):
    bot.add_cog(Info(bot))
