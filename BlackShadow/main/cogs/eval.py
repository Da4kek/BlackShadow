import discord 
from discord.ext import commands
import contextlib
import io
class Eval(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @commands.command()
    async def eval(self,ctx,*,code):
        str_obj = io.StringIO()
        try:
            with contextlib.redirect_stdout(str_obj):
                exec(code)
        except Exception as e:
            return await ctx.send(f"```{e.__class__.__name__}: {e}```")
        try:
            em = discord.Embed(color= discord.Color.light_grey())
            em.add_field(
                name=f"Ran your {eval(code)} code", value=f"```{str_obj.getvalue()}```")
            em.set_footer(icon_url=ctx.author.avatar_url)
        except:
            await ctx.send("An error occured")

        await ctx.send(embed = em)

def setup(bot):
    bot.add_cog(Eval(bot))
