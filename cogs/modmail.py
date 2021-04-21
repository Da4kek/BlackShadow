import discord
from discord.ext import commands
import asyncio

sent_users = []
class ModMail(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self,message):
        empty_array = []
        mod_mail_channel = discord.utils.get(
            self.bot.get_all_channels(), name="shadow-mail")
        if message.author == self.bot.user:
            return
        if str(message.channel.type) == "private":
            if message.attachments != empty_array:
                files = message.attachments
                em = discord.Embed(color=0xEAD2A2)
                em.add_field(name = message.author.display_name,value =files[0].url)
                await mod_mail_channel.send(embed = em)
                for file in files:
                    await mod_mail_channel.send(file.url)
            else:
                em = discord.Embed(color=0xEAD2A2)
                em.add_field(name = message.author.display_name,value = message.content)
                await mod_mail_channel.send(embed = em)

        elif str(message.channel) == "shadow-mail" and message.content.startswith("<"):
            try:
                member_object = message.mentions[0]
                if message.attachments != empty_array:
                    files = message.attachments
                    em.add_field(name=message.author.display_name,value = files[0].url)
                    await mod_mail_channel.send(embed=em)
                    for file in files:
                        await member_object.send(file.url)
                else:
                    index = message.content.index(" ")
                    string = message.content
                    mod_message = string[index:]
                    em = discord.Embed(color=0xEAD2A2)
                    em.add_field(name = message.author.display_name,value = mod_message)
                    await member_object.send(embed = em)
            except IndexError:
                em = discord.Embed(color=0xfa4e3e)
                em.add_field(name = "Error",value = "write your reply followed by a mention of the user")


def setup(bot):
    bot.add_cog(ModMail(bot))
