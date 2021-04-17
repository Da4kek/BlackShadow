import discord 
from discord.ext import commands
import contextlib
import io
import re
from discord import Color, Embed


class CodeExec(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        # TODO: Improve this further
        self.regex = re.compile(r"(\w*)\s*(?:```)(\w*)?([\s\S]*)(?:```$)")

    @property
    def session(self):
        return self.bot.http._HTTPClient__session

    async def _run_code(self, *, lang: str, code: str):
        res = await self.session.post(
            "https://emkc.org/api/v1/piston/execute",
            json={"language": lang, "source": code},
        )
        return await res.json()

    @commands.command()
    async def run(self, ctx: commands.Context, *, codeblock: str):
        matches = self.regex.findall(codeblock)
        if not matches:
            return await ctx.send(
                embed=Embed(
                    title="__Error!:negative_squared_cross_mark:__", description="Try again with **Code blocks**"
                ,color=Color.red())
            )
        lang = matches[0][0] or matches[0][1]
        if not lang:
            return await ctx.send(
                embed=Embed(
                    title="__Error!:negative_squared_cross_mark:__",
                    description="Try again with **valid language**",
                )
            )
        code = matches[0][2]
        result = await self._run_code(lang=lang, code=code)

        await self._send_result(ctx, result)



    async def _send_result(self, ctx: commands.Context, result: dict):
        if "message" in result:
            return await ctx.send(
                embed=Embed(
                    title="__Error!:negative_squared_cross_mark:__", description=result["message"], color=Color.red()
                )
            )
        output = result["output"]
        
        output = output[:500]
        shortened = len(output) > 500
        lines = output.splitlines()
        shortened = shortened or (len(lines) > 15)
        output = "\n".join(lines[:15])
        output += shortened * "\n\n**Short output**"
        embed = Embed(
            title=f"**__Output__**", color=Color.green(),description = output or "**No Output**")
        await ctx.reply(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(CodeExec(bot))
