import discord
from discord.ext import commands
from disputils import BotEmbedPaginator
from discord import Embed
import sys
import traceback
import pymysql.cursors
from dotenv import load_dotenv
import os

load_dotenv()
bot_token = os.getenv("BOT_TOKEN")
host = os.getenv("HOST")
port = os.getenv("PORT")
password = os.getenv("PASSWORD")
db = os.getenv("DB")

connection = pymysql.connect(
    host=host,
    port=int(port),
    user="root",
    password=password,
    db=db,
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor
)

bot_info = {}
with connection.cursor() as cur:
    cur.execute('Select * from Botinfo')
    rows = cur.fetchall()
    for row in rows:
        print(f"Prefix: {row['prefix']}\nNumber of Commands: {row['commands']}\nNumber of guilds: {row['guild']}\nNumber of users: {row['users']}\nVersion: {row['version']}")
        bot_info["prefix"] = row['prefix']
        bot_info['commands'] = row['commands']
        bot_info['guild'] = row['guild']
        bot_info['users'] = row['users']
        bot_info['version'] = row['version']
        
    


intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix=commands.when_mentioned_or(str(row['prefix'])),
                   intents=intents)
bot.remove_command('help')


# @bot.event
# async def on_command_error(self, ctx, error):
#     if isinstance(error, commands.MissingPermissions):
#         em = discord.Embed(
#             description=
#             "<a:Animated_Cross:809410957860143124> You Do not Have Permissions To Use This Command",
#             color=discord.Colour.red())
#         await ctx.send(embed=em)

#     elif isinstance(error, commands.MissingRequiredArgument):
#         em = discord.Embed(
#             description=
#             "<a:Animated_Cross:809410957860143124> Please Fill All The Arguments To Use This Command",
#             color=discord.Colour.red())
#         await ctx.send(embed=em)

#     elif isinstance(error, commands.MemberNotFound):
#         em = discord.Embed(
#             description="<a:Animated_Cross:809410957860143124> User Not Found",
#             color=discord.Colour.red())
#         await ctx.send(embed=em)

#     elif isinstance(error, commands.BadArgument):
#         em = discord.Embed(
#             description=
#             "<a:Animated_Cross:809410957860143124> Invalid Argument, Please Enter The Valid Argument",
#             color=discord.Colour.red())
#         await ctx.send(embed=em)

#     elif isinstance(error, commands.MissingRole):
#         em = discord.Embed(
#             description=
#             "<a:Animated_Cross:809410957860143124> You Do not Have Correct Permissions To Use This Command",
#             color=discord.Colour.red())
#         await ctx.send(embed=em)

#     elif isinstance(error, commands.CommandOnCooldown):
#         m, s = divmod(error.retry_after, 60)
#         h, m = divmod(m, 60)
#         if int(h) == 0 and int(m) == 0:
#             await ctx.send(
#                 f' You must wait {int(s)} seconds to use this command!')
#         elif int(h) == 0 and int(m) != 0:
#             await ctx.send(
#                 f' You must wait {int(m)} minutes and {int(s)} seconds to use this command!'
#             )
#         else:
#             await ctx.send(
#                 f' You must wait {int(h)} hours, {int(m)} minutes and {int(s)} seconds to use this command!'
#             )
#     elif isinstance(error, commands.CheckFailure):
#         await ctx.send("Hey! You lack permission to use this command.")

#     else:
#         raise error


@bot.event
async def on_ready():
    print(f'''
Logged in as [{bot.user}]
============================
ID: [{bot.user.id}]
============================
Default Prefix: [{bot_info['prefix']}}]
============================
Servers: [{len(bot.guilds)}]
============================
Members: [{len(set(bot.get_all_members()))}]
============================
  ''')



@bot.command()
async def hi(ctx):
    await ctx.reply("Hello!")


@bot.command()
async def paginate(ctx):
    embeds = [
        Embed(
            title="test page 1",
            description="This is just some test content!",
            color=0x115599,
        ),
        Embed(title="test page 2",
              description="Nothing interesting here.",
              color=0x5599FF),
        Embed(title="test page 3",
              description="Why are you still here?",
              color=0x191638),
    ]

    paginator = BotEmbedPaginator(ctx, embeds)
    await paginator.run()

extensions=[
    'cogs.avatar'
]

if __name__ == "__main__":
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as e: 
            print(f'Error Loading {extensions}', file=sys.stderr)
            traceback.print_exc()

# listes The Cog
@bot.command()
@commands.is_owner()
async def licog(ctx):
    await ctx.send(extensions)


bot.run(bot_token)
