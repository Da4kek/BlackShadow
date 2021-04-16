import discord
from discord.ext import commands
import pymysql.cursors
import os
import dotenv

dotenv.load_dotenv('/mnt/c/Users/infra/Desktop/desktop_folders/project-1/Black-shadow/BlackShadow/.env')
host = os.getenv("HOST")
port = os.getenv("PORT")
password = os.getenv("PASSWORD")
db = os.getenv("DB")

class Prefix(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def prefix(self,ctx,*,prefix):
        connection = pymysql.connect(
            host=host,
            port=int(port),
            user="root",
            password=password,
            db=db,
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor
        )
        prefixes = {}
        with connection.cursor() as cur:
            add_prefix_query = f'Insert into Botinfo(prefix) values({prefix})'
            cur.execute(add_prefix_query)
            cur.execute('select * from Botinfo')
            rows = cur.fetchall()
            for row_ in rows:
                prefixes['prefixes'] = str(row_['prefix'])
                print("the prefix  changed to {}".format(prefix))
                print("\n")
                print("the prefixes are: {}".format(prefixes))
        em = discord.Embed(title = f"Prefix changed!",description = f":white_check_mark: Sucessfully changed prefix to: **{prefix}**",color = discord.Color.red())
        await ctx.send(embed = em)

def setup(bot):
    bot.add_cog(Prefix(bot))

            
